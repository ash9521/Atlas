"""
Acceptance tests for Company Brain Report.
"""

from datetime import datetime, timezone
from uuid import uuid4

from atlas.brain.models import (
    Company,
    Evidence,
    EvidenceSource,
)
from atlas.brain.repositories import (
    CompanyRepository,
    EvidenceRepository,
)
from atlas.brain.services.brain_query_service import (
    BrainQueryService,
)


def test_company_brain_report_returns_complete_snapshot() -> None:

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
                "registration": "ABC123",
            },
        ),
    )

    service = BrainQueryService(
        CompanyRepository((company,)),
        EvidenceRepository(evidence),
    )

    report = service.company_brain_report(
        company.id,
    )

    assert report is not None

    assert report.company == company
    assert report.evidence == evidence

    assert report.facts.evidence_count == 2
    assert report.facts.evidence_types == (
        "trade_registry",
        "website",
    )

    assert report.conclusions.has_evidence
    assert report.conclusions.evidence_is_diverse
    assert report.conclusions.latest_data_available

    assert report.trust.score == 1.0
    assert report.trust.confidence == "high"

    assert report.decision.action == "pursue"
