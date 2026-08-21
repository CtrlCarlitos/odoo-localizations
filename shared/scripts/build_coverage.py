#!/usr/bin/env python3
"""Regenerate <country>/requirements/COVERAGE.md from the sources registry
and an LB-citation scan of the requirements corpus.

Curated content (status overrides + note fragments) lives in
<country>/requirements/COVERAGE_NOTES.md and is merged into the matrix.
Usage:
    build_coverage.py <country> [--check]
--check regenerates to memory and diffs against the committed matrix;
exit 1 with a unified diff on drift (wave-close gate).
"""
from __future__ import annotations
import re, sys
from pathlib import Path

SOURCE_RE = re.compile(r"^\| `([^`]+\.(?:pdf|xlsx|xls|docx|zip|md))` \|")
LBROW_RE = re.compile(r"^\|\s*(?:\d+_)?LB-\d+")
TOPIC_FILE_RE = re.compile(r"^\d{2}_.*\.md$")

def parse_registry(registry: Path):
    rows = []
    for line in registry.read_text(encoding="utf-8").splitlines():
        m = SOURCE_RE.match(line)
        if m:
            rows.append(m.group(1))
    return rows

def parse_notes(notes: Path):
    overrides, fragments, section = {}, {}, None
    for line in notes.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("## "):
            section = s[3:].strip().lower()
        elif s.startswith("|") and not set(s) <= set("|- ~\t "):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 2 and cells[0] and not cells[0].startswith("Source"):
                if section and section.startswith("status"):
                    overrides[cells[0]] = cells[1]
                elif section and section.startswith("note"):
                    fragments[cells[0]] = cells[1]
    return overrides, fragments

def scan_citations(req_dir: Path, sources):
    # {source: {topic_file_dir/file.md: lb_row_count}}
    reg = set(sources)

    def resolve(src):
        # a truncated citation stem resolves to the registry file when
        # stem prefix + extension match exactly one (e.g. 63_F930v3.pdf)
        if src in reg:
            return src
        stem, _, ext = src.rpartition(".")
        matches = [s for s in reg if s.rpartition(".")[0].startswith(stem)
                   and s.endswith("." + ext)]
        return matches[0] if len(matches) == 1 else src

    hits = {}
    for topic in sorted(req_dir.iterdir()):
        if not topic.is_dir():
            continue
        for f in sorted(topic.glob("*.md")):
            if not TOPIC_FILE_RE.match(f.name):
                continue
            for line in f.read_text(encoding="utf-8").splitlines():
                for raw in re.findall(r"`sv/sources/([^`]+)`", line):
                    src = resolve(raw)
                    if LBROW_RE.match(line) or "`sv/sources/" in line and line.startswith("|") and "LB-" in line:
                        hits.setdefault(src, {}).setdefault(
                            f"{topic.name}/{f.name}", 0)
                        if LBROW_RE.match(line):
                            hits[src][f"{topic.name}/{f.name}"] += 1
    return hits

def build_matrix(sources, hits, overrides, fragments, req_dir: Path):
    lines = ["| Source | Status | Cited in / note |",
             "|--------|--------|-----------------|"]
    for src in sources:
        per_file = hits.get(src, {})
        cited = [f"`{k}` ({v} LB rows)" if v else f"`{k}`"
                 for k, v in sorted(per_file.items())]
        status = overrides.get(src, "cited-as-LB" if per_file else "pending-S2+")
        note = fragments.get(src, "")
        cell = "; ".join(cited)
        if note:
            cell = (cell + " — " + note) if cell else note
        lines.append(f"| {src} | {status} | {cell} |")
    # synthetic schemas row (status/note curated in the notes file)
    key = "schemas/ (dir)"
    status = overrides.get(key, "cited-as-LB")
    note = fragments.get(key, "direct JSON schema reads (e-invoicing "
                             "waves) — see `sv/sources/schemas/`")
    lines.append(f"| {key} | {status} | {note} |")
    return "\n".join(lines) + "\n"

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    country = sys.argv[1]
    check = "--check" in sys.argv
    root = Path(__file__).resolve().parent.parent.parent
    req_dir = root / country / "requirements"
    cov = req_dir / "COVERAGE.md"
    sources = parse_registry(root / country / "sources" / "README.md")
    overrides, fragments = ({}, {})
    notes = req_dir / "COVERAGE_NOTES.md"
    if notes.exists():
        overrides, fragments = parse_notes(notes)
    matrix = build_matrix(sources, scan_citations(req_dir, sources),
                          overrides, fragments, req_dir)
    text = cov.read_text(encoding="utf-8")
    marker = "## Matrix"
    idx = text.index(marker)
    head = text[:idx + len(marker)]
    new = head + "\n" + matrix
    if check:
        import difflib
        diff = list(difflib.unified_diff(
            text.splitlines(True), new.splitlines(True),
            fromfile="COVERAGE.md", tofile="regenerated"))
        if diff:
            sys.stdout.writelines(diff)
            sys.exit(1)
        print("COVERAGE.md: no drift")
        sys.exit(0)
    cov.write_text(new, encoding="utf-8")
    print(f"COVERAGE.md matrix regenerated ({len(sources)} sources)")

if __name__ == "__main__":
    main()
