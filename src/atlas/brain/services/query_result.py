"""
High-level Brain query result.
"""

from __future__ import annotations

from dataclasses import dataclass

from atlas.brain.models import Company, Evidence


@dataclass(slots=True, frozen=True)
class QueryResult:
    """
    Immutable result returned from Brain queries.
    """

    company: Company
    evidence: tuple[Evidence, ...]
