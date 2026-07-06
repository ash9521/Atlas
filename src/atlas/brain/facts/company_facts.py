"""
Computed facts about a company.

Produced by the Fact Engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class CompanyFacts:
    """
    Immutable computed facts.
    """

    evidence_count: int
    evidence_types: tuple[str, ...]
    latest_observation: datetime | None
