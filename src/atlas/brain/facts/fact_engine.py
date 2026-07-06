"""
Fact Engine.

Computes facts from immutable evidence.
"""

from __future__ import annotations

from atlas.brain.queries import QueryResult
from atlas.brain.facts.company_facts import CompanyFacts


class FactEngine:
    """
    Stateless computation engine.

    Converts query results into computed facts.
    """

    def compute(
        self,
        result: QueryResult,
    ) -> CompanyFacts:

        evidence = result.evidence

        latest = (
            max(item.observed_at for item in evidence)
            if evidence
            else None
        )

        evidence_types = tuple(
            sorted(
                {
                    item.evidence_type
                    for item in evidence
                }
            )
        )

        return CompanyFacts(
            evidence_count=len(evidence),
            evidence_types=evidence_types,
            latest_observation=latest,
        )
