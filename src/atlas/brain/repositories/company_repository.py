"""
Read-only repository for Company entities.
"""

from __future__ import annotations

from collections.abc import Iterable
from uuid import UUID

from atlas.brain.models import Company


class CompanyRepository:
    """
    Read-only access to Company entities.
    """

    def __init__(self, companies: Iterable[Company] = ()) -> None:
        self._companies: dict[UUID, Company] = {
            company.id: company
            for company in companies
        }

    def get(self, company_id: UUID) -> Company | None:
        return self._companies.get(company_id)

    def exists(self, company_id: UUID) -> bool:
        return company_id in self._companies

    def list_all(self) -> tuple[Company, ...]:
        return tuple(self._companies.values())
