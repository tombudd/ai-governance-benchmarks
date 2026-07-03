from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from evaluation.report import build_report
from evaluation.scorer import score_case


def load_cases(input_path: Path) -> list[dict]:
    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Input file must contain a JSON array of benchmark cases.")
    return data


def write_report(output_path: Path, report: dict) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)
        file.write("\n")


def run(input_path: Path, output_path: Path) -> dict:
    cases = load_cases(input_path)
    results = [score_case(case) for case in cases]
    report = build_report(results)
    write_report(output_path, report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a synthetic AI governance benchmark."
    )
    parser.add_argument("--input", required=True, help="Path to input benchmark JSON.")
    parser.add_argument("--output", required=True, help="Path to output report JSON.")
    args = parser.parse_args()

    report = run(Path(args.input), Path(args.output))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
