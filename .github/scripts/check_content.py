#!/usr/bin/env python3
"""
PhysicsSelfStudy content quality checker.

Validates that course README.md files follow the standard format:
  - 5 core mental models
  - 3 fundamental disagreements
  - 10 deep questions
  - 5 deep dives (one per mental model)
  - 10 detailed self-test solutions
  - 5+ Mermaid diagram sections
  - Closing 5-point "deep insights" summary
  - Bilingual content (中英對照)
"""

import os
import re
import sys
from pathlib import Path


def check_bilingual(content: str) -> tuple[bool, int, int]:
    """Check for Chinese + English markers. Returns (is_bilingual, zh_count, en_count)."""
    zh_count = len(re.findall(r"[\u4e00-\u9fff]", content))
    en_count = len(re.findall(r"\b[A-Za-z]{3,}\b", content))
    return (zh_count > 50 and en_count > 100, zh_count, en_count)


def analyze_readme(path: Path) -> dict:
    """Analyze a single README.md for content quality."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"path": path, "error": str(e)}

    lines = text.splitlines()
    line_count = len(lines)

    # 5 mental models: look for "5 個核心心智模型" or 5-row table after "問題 1"
    has_5mm = bool(re.search(r"5\s*個核心心智模型|core mental models", text, re.IGNORECASE))

    # 3 disagreements: look for "3 個地方存在根本分歧" or "3 fundamental disagreements"
    has_3dg = bool(re.search(r"3\s*個(地方存在)?根本分歧|3\s*個.*分歧|3 fundamental disagreements", text, re.IGNORECASE))

    # 10 deep questions
    has_10q = bool(re.search(r"10\s*個(.*?)?問題|10\s*個.*?深度|10 questions|10\s*個能區分", text, re.IGNORECASE))

    # 5 deep dives: count "深入 N" or "Deep Dive N" headers
    dive_count = sum(1 for m in re.finditer(
        r"##\s*深入\s*([1-9]|10)|##\s*Deep Dive\s*([1-9]|10)|##\s*Deep Dive\s*([IVX]+)",
        text
    ))

    # Mermaid diagrams: count opening fences
    mermaid_count = sum(1 for line in lines if line.strip() == "```mermaid")

    # 10 self-test solutions
    solution_count = sum(1 for m in re.finditer(
        r"##\s*自測\s*([1-9]|1[0-9])|##\s*Self-?[Tt]est\s*([1-9]|1[0-9])",
        text
    ))

    # Deep insights summary
    has_summary = bool(re.search(
        r"## 深度總結|## Deep Insights|深度洞察",
        text
    ))

    is_bilingual, zh_count, en_count = check_bilingual(text)

    return {
        "path": path,
        "lines": line_count,
        "has_5mm": has_5mm,
        "has_3dg": has_3dg,
        "has_10q": has_10q,
        "deep_dives": dive_count,
        "mermaid": mermaid_count,
        "solutions": solution_count,
        "has_summary": has_summary,
        "is_bilingual": is_bilingual,
        "zh_chars": zh_count,
        "en_words": en_count,
    }


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent.parent
    if not (repo_root / "01_BSc_Physics").exists():
        repo_root = Path.cwd()

    readmes = sorted(repo_root.rglob("README.md"))
    readmes = [
        r for r in readmes
        if not any(part.startswith(".") or part == "old_archive"
                   for part in r.parts)
    ]

    print(f"📚 PhysicsSelfStudy content quality check")
    print(f"   Scanning {len(readmes)} README files\n")
    print(f"{'File':<70} {'Lines':>6} {'5MM':>4} {'3DG':>4} {'10Q':>4} {'5DD':>4} {'5MR':>4} {'10SL':>5} {'Bi':>3} {'Summary':>8} {'Status'}")
    print("─" * 140)

    hard_failures = []
    stubs = []
    complete = []

    for readme in readmes:
        result = analyze_readme(readme)
        if "error" in result:
            print(f"❌ {readme.relative_to(repo_root)}: {result['error']}")
            hard_failures.append(readme)
            continue

        rel = str(readme.relative_to(repo_root))
        if len(rel) > 67:
            rel = "..." + rel[-64:]

        is_complete = (
            result["has_5mm"]
            and result["has_3dg"]
            and result["has_10q"]
            and result["deep_dives"] >= 5
            and result["mermaid"] >= 5
            and result["solutions"] >= 10
            and result["has_summary"]
            and result["lines"] >= 200
            and result["is_bilingual"]
        )
        is_stub = result["lines"] < 100

        if is_complete:
            status = "✅ COMPLETE"
            complete.append(rel)
        elif is_stub:
            status = "📄 STUB"
            stubs.append(rel)
        else:
            status = "⚠️  PARTIAL"
            stubs.append(rel)

        print(
            f"{rel:<70} {result['lines']:>6} "
            f"{'✓' if result['has_5mm'] else '✗':>4} "
            f"{'✓' if result['has_3dg'] else '✗':>4} "
            f"{'✓' if result['has_10q'] else '✗':>4} "
            f"{result['deep_dives']:>4} "
            f"{result['mermaid']:>4} "
            f"{result['solutions']:>5} "
            f"{'✓' if result['is_bilingual'] else '✗':>3} "
            f"{'✓' if result['has_summary'] else '✗':>8} "
            f"{status}"
        )

    print("\n" + "─" * 140)
    print(f"✅ Complete courses (full new format): {len(complete)}")
    print(f"⚠️  Stubs / partial courses: {len(stubs)}")
    print(f"❌ Hard failures: {len(hard_failures)}")

    if complete:
        print(f"\n✅ Courses in full new format:")
        for c in complete:
            print(f"   - {c}")

    if not complete:
        print(f"\n⚠️  No course is in the full new format yet.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
