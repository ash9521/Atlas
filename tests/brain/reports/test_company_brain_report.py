"""
Brain report service tests.
"""

from datetime import datetime, timezone
from uuid import uuid4

from atlas.brain.decisions import CompanyDecision
from atlas.brain.models import (
    Company,
    Evidence,
    EvidenceSource,
)
from atlas.brain.reports import CompanyBrainReport
from atlas.brain.facts.company_facts import CompanyFacts
from atlas.brain.conclusions import CompanyConclusions
from atlas.brain.trust import TrustScore


def test_company_brain_report_is_immutable() -> None:

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
    )

    report = CompanyBrainReport(
        company=company,
        evidence=evidence,
        facts=CompanyFacts(
            evidence_count=1,
            evidence_types=("website",),
            latest_observation=evidence[0].observed_at,
        ),
        conclusions=CompanyConclusions(
            has_evidence=True,
            evidence_is_diverse=False,
            latest_data_available=True,
        ),
        trust=TrustScore(
            score=0.7,
            confidence="medium",
        ),
        decision=CompanyDecision(
            action="research",
            reason="Gather additional evidence.",
        ),
    )

    assert report.company == company
    assert report.evidence == evidence
    assert report.trust.score == 0.7
    assert report.decision.action == "research"
