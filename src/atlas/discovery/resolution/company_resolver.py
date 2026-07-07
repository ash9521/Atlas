from __future__ import annotations

from atlas.brain.repositories import CompanyRepository
from atlas.discovery.normalization.models import (
    NormalizedObservation,
)
from atlas.discovery.resolution.models import (
    CompanyResolutionResult,
)


class CompanyResolver:
    """
    Resolves a normalized observation to an existing Company using
    an exact legal-name match.
    """

    def __init__(
        self,
        repository: CompanyRepository,
    ) -> None:
        self._repository = repository

    def resolve(
        self,
        observation: NormalizedObservation,
    ) -> CompanyResolutionResult:
        legal_name = observation.payload.get("Company")

        if not isinstance(legal_name, str):
            return CompanyResolutionResult.not_found()

        company = self._repository.find_by_legal_name(
            legal_name,
        )

        if company is None:
            return CompanyResolutionResult.not_found()

        return CompanyResolutionResult.matched(
            company,
        )
