from __future__ import annotations

from schema_sample_check.models import Rule

PROJECT_NAME = 'schema-sample-check'
SUMMARY = 'Validate schema examples for placeholder data and missing required samples.'
SAMPLE_RISK = 'required field missing example foo bar id 123'
SAMPLE_CLEAN = 'required field customer_id example cus_123 realistic true'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-required',
        severity='high',
        pattern='required field missing',
        message='required example is missing',
        recommendation='add sample for required field',
    ),
    Rule(
        code='placeholder-data',
        severity='medium',
        pattern='\\b(foo|bar|lorem|id 123)\\b',
        message='placeholder example detected',
        recommendation='use realistic example data',
    ),
    Rule(
        code='unrealistic-flag',
        severity='low',
        pattern='realistic\\s+false',
        message='example marked unrealistic',
        recommendation='replace with representative sample',
    ),
)
