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
from atlas.brain.services import BrainQueryService


def test_company_facts() -> None:
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

    facts = service.company_facts(company.id)

    assert facts is not None
    assert facts.evidence_count == 1
    assert facts.evidence_types == (
        "government.registration",
    )
    assert facts.latest_observation == evidence.observed_at
