from atlas.brain.conclusions import CompanyConclusions
from atlas.brain.trust import TrustEngine


def test_compute_trust_score() -> None:
    conclusions = CompanyConclusions(
        has_evidence=True,
        evidence_is_diverse=True,
        latest_data_available=True,
    )

    trust = TrustEngine().compute(conclusions)

    assert trust.score == 1.0
    assert trust.confidence == "high"
