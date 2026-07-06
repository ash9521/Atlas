"""
Decision Engine.

Computes a recommended action from trust.
"""

from __future__ import annotations

from atlas.brain.trust import TrustScore

from .company_decision import CompanyDecision


class DecisionEngine:
    """
    Stateless decision engine.
    """

    def compute(
        self,
        trust: TrustScore,
    ) -> CompanyDecision:

        if trust.score >= 0.90:
            return CompanyDecision(
                action="pursue",
                reason="High confidence.",
            )

        if trust.score >= 0.60:
            return CompanyDecision(
                action="research",
                reason="Gather additional evidence.",
            )

        return CompanyDecision(
            action="reject",
            reason="Insufficient confidence.",
        )
