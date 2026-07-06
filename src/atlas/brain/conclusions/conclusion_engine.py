"""
Conclusion Engine.

Computes conclusions from CompanyFacts.
"""

from __future__ import annotations

from atlas.brain.conclusions.company_conclusions import CompanyConclusions
from atlas.brain.facts.company_facts import CompanyFacts


class ConclusionEngine:
    """
    Stateless conclusion engine.
    """

    def compute(
        self,
        facts: CompanyFacts,
    ) -> CompanyConclusions:

        return CompanyConclusions(
            has_evidence=facts.evidence_count > 0,
            evidence_is_diverse=len(facts.evidence_types) > 1,
            latest_data_available=facts.latest_observation is not None,
        )
