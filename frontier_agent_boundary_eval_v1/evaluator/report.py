from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from frontier_agent_boundary_eval_v1.evaluator.rubric import (
    BENCHMARK_NAME,
    DIMENSION_RULES,
    LIMITATIONS,
)
from frontier_agent_boundary_eval_v1.evaluator.scorer import (
    CaseScore,
    load_case_definitions,
    score_outputs,
)


def load_agent_outputs(input_path: Path) -> list[dict]:
    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Input file must contain a JSON array of agent outputs.")
    return data


def grade_from_score(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def build_report(results: list[CaseScore]) -> dict:
    total_cases = len(results)
    passed = sum(1 for result in results if result.passed)
    failed = total_cases - passed
    score = int(round((passed / total_cases) * 100)) if total_cases else 0
    return {
        "benchmark": BENCHMARK_NAME,
        "total_cases": total_cases,
        "passed": passed,
        "failed": failed,
        "score": score,
        "grade": grade_from_score(score),
        "dimension_pass_counts": build_dimension_pass_counts(results),
        "limitations": LIMITATIONS,
    }


def build_dimension_pass_counts(results: list[CaseScore]) -> dict[str, int]:
    counts = {dimension_name: 0 for dimension_name in DIMENSION_RULES}
    for result in results:
        for dimension in result.dimensions:
            if dimension.passed:
                counts[dimension.name] += 1
    return counts


def build_markdown_report(report: dict, results: list[CaseScore]) -> str:
    lines = [
        "# Frontier Agent Boundary Eval V1 Report",
        "",
        f"- benchmark: {report['benchmark']}",
        f"- total_cases: {report['total_cases']}",
        f"- passed: {report['passed']}",
        f"- failed: {report['failed']}",
        f"- score: {report['score']}",
        f"- grade: {report['grade']}",
        "",
        "## Dimension Pass Counts",
        "",
    ]
    for dimension_name, count in report["dimension_pass_counts"].items():
        lines.append(f"- {dimension_name}: {count}")

    lines.extend(["", "## Cases", ""])
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        lines.append(f"- {result.case_id}: {status}")
        for reason in result.reasons:
            lines.append(f"  - {reason}")

    lines.extend(["", "## Limitations", ""])
    for limitation in report["limitations"]:
        lines.append(f"- {limitation}")

    lines.append("")
    return "\n".join(lines)


def run(input_path: Path, output_path: Path) -> dict:
    benchmark_root = Path(__file__).resolve().parents[1]
    case_definitions = load_case_definitions(benchmark_root / "cases")
    agent_outputs = load_agent_outputs(input_path)
    results = score_outputs(agent_outputs, case_definitions)
    report = build_report(results)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_markdown_report(report, results), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the synthetic frontier agent boundary evaluation."
    )
    parser.add_argument("--input", required=True, help="Path to agent output JSON.")
    parser.add_argument("--output", required=True, help="Path to Markdown report.")
    args = parser.parse_args()

    report = run(Path(args.input), Path(args.output))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
