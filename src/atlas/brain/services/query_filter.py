"""
Brain query filters.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class QueryFilter:
    """
    Optional filters for Brain queries.
    """

    evidence_type: str | None = None
