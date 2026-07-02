# schema-sample-check

> Validate schema examples for placeholder data and missing required samples.

## Spec sheet Overview

Validate schema examples for placeholder data and missing required samples. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts schema examples text. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
schema-sample-check examples/sample.txt
schema-sample-check examples/sample.txt --json --fail-on medium
python -m schema_sample_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-required` | high | required example is missing |
| `placeholder-data` | medium | placeholder example detected |
| `unrealistic-flag` | low | example marked unrealistic |

## Validation Notes

```bash
ruff check .
pytest
python -m schema_sample_check --help
```

Example risky input:

```text
required field missing example foo bar id 123
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
