from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from atlas.brain.models import Company


class CompanyResolutionStatus(str, Enum):
    MATCHED = "matched"
    NOT_FOUND = "not_found"


@dataclass(frozen=True, slots=True)
class CompanyResolutionResult:
    """
    Result of resolving a company from a normalized observation.
    """

    status: CompanyResolutionStatus
    company: Company | None

    @classmethod
    def matched(
        cls,
        company: Company,
    ) -> "CompanyResolutionResult":
        return cls(
            status=CompanyResolutionStatus.MATCHED,
            company=company,
        )

    @classmethod
    def not_found(
        cls,
    ) -> "CompanyResolutionResult":
        return cls(
            status=CompanyResolutionStatus.NOT_FOUND,
            company=None,
        )
