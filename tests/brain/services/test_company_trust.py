from uuid import uuid4

from atlas.brain.models import Company
from atlas.brain.repositories import (
    CompanyRepository,
    EvidenceRepository,
)
from atlas.brain.services.brain_query_service import BrainQueryService


def test_company_trust_returns_none_for_missing_company() -> None:
    service = BrainQueryService(
        CompanyRepository(()),
        EvidenceRepository(()),
    )

    assert service.company_trust(uuid4()) is None


def test_company_trust_returns_score() -> None:
    company = Company(
        id=uuid4(),
        legal_name="Atlas",
    )

    service = BrainQueryService(
        CompanyRepository((company,)),
        EvidenceRepository(()),
    )

    trust = service.company_trust(company.id)

    assert trust is not None
    assert trust.score == 0.0
    assert trust.confidence == "low"
