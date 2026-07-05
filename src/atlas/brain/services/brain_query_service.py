"""
Brain query service.

Provides read-only access to the Atlas Brain while preserving
the public API established during Sprint 2.
"""

from __future__ import annotations

from uuid import UUID

from atlas.brain.models import Company, Evidence
from atlas.brain.repositories import (
    CompanyRepository,
    EvidenceRepository,
)
from atlas.brain.services.query_result import QueryResult


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
        company = self.get_company(company_id)

        if company is None:
            return None

        return QueryResult(
            company=company,
            evidence=self.evidence_for_company(company_id),
        )
