#!/usr/bin/env python3
"""Render Digital DM character sheets (Markdown + YAML frontmatter) as ASCII.

Usage:
  python charsheet.py render <sheet.md>
  python charsheet.py render <sheet.md> --width 64
  python charsheet.py init <sheet.md> --name "Ada" --class Vanguard --level 1

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any


def mod(score: int) -> int:
    return (score - 10) // 2


def fmt_mod(score: int) -> str:
    m = mod(score)
    return f"{m:+d}"


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Minimal YAML-ish frontmatter: key: value, and key:\\n  - list items."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    raw, body = parts[1], parts[2]
    data: dict[str, Any] = {}
    lines = raw.strip("\n").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in ("", "|", ">"):
            # list or block
            items: list[str] = []
            i += 1
            while i < len(lines):
                ln = lines[i]
                if re.match(r"^[A-Za-z0-9_]+:", ln):
                    break
                lm = re.match(r"^\s+-\s+(.*)$", ln)
                if lm:
                    items.append(lm.group(1).strip())
                    i += 1
                    continue
                if val in ("|", ">") and ln.startswith("  "):
                    items.append(ln[2:])
                    i += 1
                    continue
                if not ln.strip():
                    i += 1
                    continue
                break
            data[key] = "\n".join(items) if val in ("|", ">") else items
            continue
        # strip quotes
        if (val.startswith('"') and val.endswith('"')) or (
            val.startswith("'") and val.endswith("'")
        ):
            val = val[1:-1]
        # int?
        if re.fullmatch(r"-?\d+", val):
            data[key] = int(val)
        elif val.lower() in ("true", "false"):
            data[key] = val.lower() == "true"
        else:
            data[key] = val
        i += 1
    return data, body.lstrip("\n")


def as_list(val: Any) -> list[str]:
    if val is None:
        return []
    if isinstance(val, list):
        return [str(x) for x in val]
    return [str(val)]


def box(lines: list[str], width: int) -> str:
    inner = width - 2
    out = ["┌" + "─" * inner + "┐"]
    for line in lines:
        # visible width approx (ASCII/box)
        visible = line
        if len(visible) > inner:
            visible = visible[: inner - 1] + "…"
        out.append("│" + visible.ljust(inner) + "│")
    out.append("└" + "─" * inner + "┘")
    return "\n".join(out)


def section(title: str, width: int) -> list[str]:
    inner = width - 2
    bar = "─" * max(0, inner - len(title) - 2)
    return [f" {title} {bar}"[:inner]]


def render_ascii(data: dict[str, Any], width: int = 62) -> str:
    name = str(data.get("name", "Unknown"))
    level = data.get("level", "?")
    klass = str(data.get("class", data.get("role", "—")))
    ancestry = str(data.get("ancestry", data.get("species", "—")))
    background = str(data.get("background", "—"))
    player = str(data.get("player", ""))
    align = str(data.get("alignment", data.get("ethos", "")))

    hp = data.get("hp", data.get("hp_current", "?"))
    hp_max = data.get("hp_max", hp)
    ac = data.get("ac", "?")
    speed = data.get("speed", 30)
    prof = data.get("proficiency", data.get("proficiency_bonus", "?"))
    init = data.get("initiative", "")

    def score(key: str) -> int:
        v = data.get(key, 10)
        try:
            return int(v)
        except (TypeError, ValueError):
            return 10

    abilities = [
        ("STR", score("str")),
        ("DEX", score("dex")),
        ("CON", score("con")),
        ("INT", score("int")),
        ("WIS", score("wis")),
        ("CHA", score("cha")),
    ]

    lines: list[str] = []
    head = f" {name.upper()}"
    right = f"Level {level} "
    pad = max(1, (width - 2) - len(head) - len(right))
    lines.append(head + " " * pad + right)
    sub = f" {ancestry} {klass}"
    if background and background != "—":
        sub += f"  ·  {background}"
    lines.append(sub[: width - 2])
    meta = []
    if player:
        meta.append(f"Player: {player}")
    if align:
        meta.append(align)
    if meta:
        lines.append(" " + "  ·  ".join(meta))

    lines.append("─" * (width - 2))
    combat = f" HP {hp}/{hp_max}   AC {ac}   Speed {speed}   Prof +{prof}"
    if init != "" and init is not None:
        combat += f"   Init {init:+d}" if isinstance(init, int) else f"   Init {init}"
    lines.append(combat[: width - 2])

    lines.append("─" * (width - 2))
    # ability row 1-3 and 4-6
    def abil_line(chunk: list[tuple[str, int]]) -> str:
        parts = [f"{n} {s:2d} ({fmt_mod(s)})" for n, s in chunk]
        return " " + "   ".join(parts)

    lines.append(abil_line(abilities[:3]))
    lines.append(abil_line(abilities[3:]))

    skills = as_list(data.get("skills"))
    if skills:
        lines.append("─" * (width - 2))
        lines.extend(section("SKILLS", width))
        row = " " + ", ".join(skills)
        # wrap
        while row:
            lines.append(row[: width - 2])
            row = (" " + row[width - 2 :].lstrip()) if len(row) > width - 2 else ""

    weapons = as_list(data.get("weapons"))
    armor = data.get("armor")
    if weapons or armor:
        lines.append("─" * (width - 2))
        lines.extend(section("COMBAT GEAR", width))
        if armor:
            lines.append(f" Armor: {armor}"[: width - 2])
        for w in weapons:
            lines.append(f" • {w}"[: width - 2])

    inv = as_list(data.get("inventory"))
    if inv:
        lines.append("─" * (width - 2))
        lines.extend(section("INVENTORY", width))
        for item in inv[:12]:
            lines.append(f" • {item}"[: width - 2])
        if len(inv) > 12:
            lines.append(f" … +{len(inv) - 12} more")

    features = as_list(data.get("features"))
    if features:
        lines.append("─" * (width - 2))
        lines.extend(section("FEATURES", width))
        for f in features[:8]:
            lines.append(f" • {f}"[: width - 2])

    notes = data.get("notes")
    if notes:
        lines.append("─" * (width - 2))
        lines.extend(section("NOTES", width))
        for nl in str(notes).splitlines()[:4]:
            lines.append(" " + nl[: width - 3])

    return box(lines, width)


def default_markdown(data: dict[str, Any]) -> str:
    """Build a human-readable Markdown body under frontmatter."""
    name = data.get("name", "Character")
    lines = [
        f"# {name}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Name | {data.get('name', '')} |",
        f"| Player | {data.get('player', '')} |",
        f"| Ancestry | {data.get('ancestry', '')} |",
        f"| Class | {data.get('class', '')} |",
        f"| Level | {data.get('level', '')} |",
        f"| Background | {data.get('background', '')} |",
        f"| Alignment | {data.get('alignment', '')} |",
        "",
        "## Combat",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| HP | {data.get('hp', '')}/{data.get('hp_max', data.get('hp', ''))} |",
        f"| AC | {data.get('ac', '')} |",
        f"| Speed | {data.get('speed', 30)} |",
        f"| Proficiency | +{data.get('proficiency', '')} |",
        "",
        "## Ability scores",
        "",
        "| Stat | Score | Mod |",
        "|------|-------|-----|",
    ]
    for key, label in (
        ("str", "STR"),
        ("dex", "DEX"),
        ("con", "CON"),
        ("int", "INT"),
        ("wis", "WIS"),
        ("cha", "CHA"),
    ):
        s = int(data.get(key, 10))
        lines.append(f"| {label} | {s} | {fmt_mod(s)} |")
    lines += ["", "## Skills", ""]
    for s in as_list(data.get("skills")):
        lines.append(f"- {s}")
    lines += ["", "## Inventory", ""]
    for s in as_list(data.get("inventory")):
        lines.append(f"- {s}")
    lines += ["", "## Notes", "", str(data.get("notes", "")), ""]
    return "\n".join(lines)


def dump_frontmatter(data: dict[str, Any]) -> str:
    order = [
        "name",
        "player",
        "ancestry",
        "class",
        "level",
        "background",
        "alignment",
        "hp",
        "hp_max",
        "ac",
        "speed",
        "proficiency",
        "initiative",
        "str",
        "dex",
        "con",
        "int",
        "wis",
        "cha",
        "armor",
        "skills",
        "weapons",
        "features",
        "inventory",
        "notes",
    ]
    lines = ["---"]
    seen = set()
    for key in order:
        if key not in data:
            continue
        seen.add(key)
        val = data[key]
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        elif isinstance(val, str) and "\n" in val:
            lines.append(f"{key}: |")
            for nl in val.splitlines():
                lines.append(f"  {nl}")
        elif isinstance(val, bool):
            lines.append(f"{key}: {'true' if val else 'false'}")
        elif isinstance(val, str) and (":" in val or val.startswith(" ")):
            lines.append(f'{key}: "{val}"')
        else:
            lines.append(f"{key}: {val}")
    for key, val in data.items():
        if key in seen:
            continue
        lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def cmd_render(path: Path, width: int) -> int:
    text = path.read_text(encoding="utf-8")
    data, _ = parse_frontmatter(text)
    if not data:
        print(f"error: no YAML frontmatter found in {path}", file=sys.stderr)
        print("hint: use `charsheet.py init` or add a --- frontmatter block", file=sys.stderr)
        return 1
    print(render_ascii(data, width=width))
    return 0


def cmd_init(path: Path, args: argparse.Namespace) -> int:
    data: dict[str, Any] = {
        "name": args.name or path.stem.replace("-", " ").title(),
        "player": args.player or "",
        "ancestry": args.ancestry or "Human",
        "class": args.class_name or "Vanguard",
        "level": args.level or 1,
        "background": args.background or "Frontier Scout",
        "alignment": args.alignment or "",
        "hp": args.hp or 12,
        "hp_max": args.hp_max or args.hp or 12,
        "ac": args.ac or 14,
        "speed": 30,
        "proficiency": 2 if (args.level or 1) < 5 else 3,
        "str": 15,
        "dex": 14,
        "con": 13,
        "int": 10,
        "wis": 12,
        "cha": 8,
        "skills": ["Athletics", "Perception"],
        "weapons": ["Longsword +5 (1d8+3)"],
        "armor": "Chain shirt",
        "inventory": ["Explorer's pack", "Rations (5)", "10 gp"],
        "features": ["Second Wind"],
        "notes": "",
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_frontmatter(data) + default_markdown(data), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    print(render_ascii(data, width=args.width))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Digital DM character sheet renderer")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("render", help="Print ASCII sheet from Markdown+YAML")
    r.add_argument("path", type=Path)
    r.add_argument("--width", type=int, default=62)

    i = sub.add_parser("init", help="Create a sheet file and print ASCII")
    i.add_argument("path", type=Path)
    i.add_argument("--name")
    i.add_argument("--player")
    i.add_argument("--ancestry")
    i.add_argument("--class", dest="class_name")
    i.add_argument("--level", type=int)
    i.add_argument("--background")
    i.add_argument("--alignment")
    i.add_argument("--hp", type=int)
    i.add_argument("--hp-max", dest="hp_max", type=int)
    i.add_argument("--ac", type=int)
    i.add_argument("--width", type=int, default=62)

    args = p.parse_args(argv)
    if args.cmd == "render":
        return cmd_render(args.path, args.width)
    if args.cmd == "init":
        return cmd_init(args.path, args)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
