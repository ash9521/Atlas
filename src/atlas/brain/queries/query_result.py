"""
Result returned by Brain queries.
"""

from __future__ import annotations

from dataclasses import dataclass

from atlas.brain.models import Company, Evidence


@dataclass(slots=True, frozen=True)
class QueryResult:
    """
    Immutable query result.
    """

    company: Company
    evidence: tuple[Evidence, ...]
