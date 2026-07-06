"""
Computed facts about a company.

Facts are derived from immutable evidence and are never stored.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class CompanyFacts:
    """
    Computed facts for a company.
    """

    evidence_count: int
    evidence_types: tuple[str, ...]
    latest_observation: datetime | None
