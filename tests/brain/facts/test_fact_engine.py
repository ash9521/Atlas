from datetime import datetime, timezone

from atlas.brain.facts import FactEngine
from atlas.brain.models import (
    Company,
    Evidence,
    EvidenceSource,
)
from atlas.brain.queries import QueryResult


def test_compute_company_facts() -> None:
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

    result = QueryResult(
        company=company,
        evidence=(evidence,),
    )

    facts = FactEngine().compute(result)

    assert facts.evidence_count == 1
    assert facts.evidence_types == (
        "government.registration",
    )

