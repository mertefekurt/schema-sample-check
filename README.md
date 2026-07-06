# Schema Sample Check

![Schema Sample Check cover](assets/readme-cover.svg)

> Validate schema examples for placeholder data and missing required samples

![stack](https://img.shields.io/badge/stack-Python-b45309?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-be185d?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-4b5563?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-2563eb?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | schema hygiene |
| Command | `schema-sample-check` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-required` | high | required example is missing |
| `placeholder-data` | medium | placeholder example detected |
| `unrealistic-flag` | low | example marked unrealistic |

## Try it locally

```bash
python -m pip install -e ".[dev]"
schema-sample-check examples/sample.txt
schema-sample-check examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m schema_sample_check --help
```
