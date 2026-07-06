from datetime import datetime, timezone

from atlas.brain.models import (
    Company,
    Evidence,
    EvidenceSource,
)
from atlas.brain.repositories import (
    CompanyRepository,
    EvidenceRepository,
)
from atlas.brain.services.brain_query_service import BrainQueryService


def create_service() -> tuple[BrainQueryService, Company]:
    company = Company.create("Acme Foods")

    source = EvidenceSource.create(
        source_type="government_api",
        name="DGFT API",
    )

    evidence = Evidence.create(
        company_id=company.id,
        evidence_type="government.registration",
        source=source,
        observed_at=datetime.now(timezone.utc),
        payload={"status": "active"},
    )

    service = BrainQueryService(
        CompanyRepository([company]),
        EvidenceRepository([evidence]),
    )

    return service, company


def test_company_exists() -> None:
    service, company = create_service()

    assert service.company_exists(company.id)


def test_get_company() -> None:
    service, company = create_service()

    assert service.get_company(company.id) == company


def test_company_evidence() -> None:
    service, company = create_service()

    assert len(service.evidence_for_company(company.id)) == 1


def test_evidence_by_type() -> None:
    service, _ = create_service()

    assert len(
        service.evidence_by_type(
            "government.registration"
        )
    ) == 1


def test_query_company_returns_query_result() -> None:
    service, company = create_service()

    result = service.query_company(company.id)

    assert result is not None
    assert result.company == company
    assert result.evidence[0].company_id == company.id

