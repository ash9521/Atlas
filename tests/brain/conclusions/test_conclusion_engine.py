from datetime import datetime, timezone

from atlas.brain.conclusions import ConclusionEngine
from atlas.brain.facts.company_facts import CompanyFacts


def test_compute_company_conclusions() -> None:
    facts = CompanyFacts(
        evidence_count=2,
        evidence_types=(
            "government.registration",
            "website",
        ),
        latest_observation=datetime.now(timezone.utc),
    )

    conclusions = ConclusionEngine().compute(facts)

    assert conclusions.has_evidence
    assert conclusions.evidence_is_diverse
    assert conclusions.latest_data_available
