from datetime import datetime, timezone
from uuid import uuid4

from atlas.brain.models import Evidence, EvidenceSource
from atlas.brain.repositories import EvidenceRepository


def create_source() -> EvidenceSource:
    return EvidenceSource.create(
        source_type="government_api",
        name="DGFT API",
    )


def create_evidence(
    *,
    company_id=None,
    evidence_type="government.registration",
    source=None,
) -> Evidence:
    return Evidence.create(
        company_id=company_id or uuid4(),
        evidence_type=evidence_type,
        source=source or create_source(),
        observed_at=datetime.now(timezone.utc),
        payload={"status": "active"},
    )


def test_repository_is_empty() -> None:
    repository = EvidenceRepository()

    assert repository.list_all() == ()


def test_find_by_company() -> None:
    company_id = uuid4()

    evidence = create_evidence(company_id=company_id)

    repository = EvidenceRepository([evidence])

    assert repository.find_by_company(company_id) == (evidence,)


def test_find_by_type() -> None:
    evidence = create_evidence(
        evidence_type="financial.statement",
    )

    repository = EvidenceRepository([evidence])

    assert repository.find_by_type(
        "financial.statement"
    ) == (evidence,)


def test_find_by_source() -> None:
    source = create_source()

    evidence = create_evidence(source=source)

    repository = EvidenceRepository([evidence])

    assert repository.find_by_source(
        source
    ) == (evidence,)


def test_missing_company_returns_empty_tuple() -> None:
    repository = EvidenceRepository()

    assert repository.find_by_company(
        uuid4()
    ) == ()
