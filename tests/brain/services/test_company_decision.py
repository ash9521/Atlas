"""
Decision service tests.
"""

from datetime import datetime, timezone
from uuid import uuid4

from atlas.brain.decisions import CompanyDecision
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


def test_company_decision_returns_pursue() -> None:

    company = Company(
        id=uuid4(),
        legal_name="Atlas Industries",
    )

    source = EvidenceSource.create(
        source_type="website",
        name="Atlas Test",
    )

    evidence = (
        Evidence.create(
            company_id=company.id,
            evidence_type="website",
            source=source,
            observed_at=datetime.now(timezone.utc),
            payload={
                "url": "https://atlas.test",
            },
        ),
        Evidence.create(
            company_id=company.id,
            evidence_type="trade_registry",
            source=source,
            observed_at=datetime.now(timezone.utc),
            payload={
                "registry": "Atlas",
            },
        ),
    )

    service = BrainQueryService(
        CompanyRepository((company,)),
        EvidenceRepository(evidence),
    )

    decision = service.company_decision(company.id)

    assert decision == CompanyDecision(
        action="pursue",
        reason="High confidence.",
    )


def test_company_decision_returns_none_for_unknown_company() -> None:

    service = BrainQueryService(
        CompanyRepository(()),
        EvidenceRepository(()),
    )

    assert service.company_decision(uuid4()) is None
