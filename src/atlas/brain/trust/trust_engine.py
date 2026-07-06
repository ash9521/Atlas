"""
Trust Engine.

Computes trust from conclusions.
"""

from __future__ import annotations

from atlas.brain.conclusions import CompanyConclusions
from atlas.brain.trust.trust_score import TrustScore


class TrustEngine:
    """
    Stateless trust engine.

    Produces a deterministic trust score from computed conclusions.
    """

    def compute(
        self,
        conclusions: CompanyConclusions,
    ) -> TrustScore:

        score = 0.0

        if conclusions.has_evidence:
            score += 0.5

        if conclusions.evidence_is_diverse:
            score += 0.3

        if conclusions.latest_data_available:
            score += 0.2

        if score >= 0.90:
            confidence = "high"
        elif score >= 0.60:
            confidence = "medium"
        else:
            confidence = "low"

        return TrustScore(
            score=score,
            confidence=confidence,
        )
