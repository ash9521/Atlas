"""
Shared helpers for Brain query services.
"""

from __future__ import annotations

from atlas.brain.queries.query_result import QueryResult


def evidence_count(
    result: QueryResult,
) -> int:
    """
    Return the number of evidence records in a query result.
    """

    return len(result.evidence)
