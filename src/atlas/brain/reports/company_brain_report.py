"""
Immutable Company Brain Report.

Aggregates every stage of the Brain pipeline into a single
read-only snapshot.
"""

from __future__ import annotations

from dataclasses import dataclass

from atlas.brain.conclusions import CompanyConclusions
from atlas.brain.decisions import CompanyDecision
from atlas.brain.facts import CompanyFacts
from atlas.brain.models import (
    Company,
    Evidence,
)
from atlas.brain.trust import TrustScore


@dataclass(slots=True, frozen=True)
class CompanyBrainReport:
    """
    Complete immutable Brain snapshot.
    """

    company: Company
    evidence: tuple[Evidence, ...]
    facts: CompanyFacts
    conclusions: CompanyConclusions
    trust: TrustScore
    decision: CompanyDecision
