"""
Brain query service.

Provides read-only query capabilities over the Atlas Brain.
"""

from __future__ import annotations

from uuid import UUID

from atlas.brain.conclusions import ConclusionEngine, CompanyConclusions
from atlas.brain.facts import FactEngine
from atlas.brain.models import Company, Evidence
from atlas.brain.queries import BrainQuery, QueryResult
from atlas.brain.repositories import (
    CompanyRepository,
    EvidenceRepository,
)
from atlas.brain.services.company_dossier import CompanyDossier
from atlas.brain.services.company_facts import CompanyFacts


class BrainQueryService:
    """
    Read-only query service over the Atlas Brain.
    """

    def __init__(
        self,
        company_repository: CompanyRepository,
        evidence_repository: EvidenceRepository,
    ) -> None:
        self._companies = company_repository
        self._evidence = evidence_repository
        self._fact_engine = FactEngine()
        self._conclusion_engine = ConclusionEngine()

    def company_exists(
        self,
        company_id: UUID,
    ) -> bool:
        return self._companies.exists(company_id)

    def get_company(
        self,
        company_id: UUID,
    ) -> Company | None:
        return self._companies.get(company_id)

    def evidence_for_company(
        self,
        company_id: UUID,
    ) -> tuple[Evidence, ...]:
        return self._evidence.find_by_company(company_id)

    def evidence_by_type(
        self,
        evidence_type: str,
    ) -> tuple[Evidence, ...]:
        return self._evidence.find_by_type(evidence_type)

    def query_company(
        self,
        company_id: UUID,
    ) -> QueryResult | None:
        return self.query(
            BrainQuery(
                company_id=company_id,
            )
        )

    def query(
        self,
        query: BrainQuery,
    ) -> QueryResult | None:

        company = self.get_company(query.company_id)

        if company is None:
            return None

        evidence = self.evidence_for_company(query.company_id)

        if query.evidence_type is not None:
            evidence = tuple(
                item
                for item in evidence
                if item.evidence_type == query.evidence_type
            )

        return QueryResult(
            company=company,
            evidence=evidence,
        )

    def company_dossier(
        self,
        company_id: UUID,
    ) -> CompanyDossier | None:

        result = self.query_company(company_id)

        if result is None:
            return None

        return CompanyDossier(
            company=result.company,
            evidence=result.evidence,
        )

    def company_facts(
        self,
        company_id: UUID,
    ) -> CompanyFacts | None:

        result = self.query_company(company_id)

        if result is None:
            return None

        return self._fact_engine.compute(result)

    def company_conclusions(
        self,
        company_id: UUID,
    ) -> CompanyConclusions | None:

        facts = self.company_facts(company_id)

        if facts is None:
            return None

        return self._conclusion_engine.compute(facts)
