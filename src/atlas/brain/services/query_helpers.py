"""
Common Brain query helpers.
"""

from __future__ import annotations

from atlas.brain.services.query_result import QueryResult


def has_evidence(result: QueryResult) -> bool:
    """
    Returns True when at least one evidence record exists.
    """
    return len(result.evidence) > 0
