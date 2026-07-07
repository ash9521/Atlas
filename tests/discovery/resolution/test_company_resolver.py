from atlas.brain.models import Company
from atlas.brain.repositories import CompanyRepository
from atlas.discovery.models import Observation
from atlas.discovery.normalization import (
    ObservationNormalizer,
)
from atlas.discovery.resolution import CompanyResolver
from atlas.discovery.resolution.models import (
    CompanyResolutionStatus,
)


def test_resolve_existing_company() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    repository = CompanyRepository([company])

    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "ABC Imports",
        },
    )

    normalized = ObservationNormalizer().normalize(
        observation,
    )

    result = CompanyResolver(
        repository,
    ).resolve(
        normalized,
    )

    assert result.status is CompanyResolutionStatus.MATCHED
    assert result.company == company


def test_company_not_found() -> None:
    repository = CompanyRepository()

    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "Unknown Company",
        },
    )

    normalized = ObservationNormalizer().normalize(
        observation,
    )

    result = CompanyResolver(
        repository,
    ).resolve(
        normalized,
    )

    assert result.status is CompanyResolutionStatus.NOT_FOUND
    assert result.company is None


def test_missing_company_field() -> None:
    repository = CompanyRepository()

    observation = Observation.create(
        connector="excel",
        payload={
            "Country": "Germany",
        },
    )

    normalized = ObservationNormalizer().normalize(
        observation,
    )

    result = CompanyResolver(
        repository,
    ).resolve(
        normalized,
    )

    assert result.status is CompanyResolutionStatus.NOT_FOUND
