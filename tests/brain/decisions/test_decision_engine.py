from atlas.brain.decisions import DecisionEngine
from atlas.brain.trust import TrustScore


def test_high_trust_returns_pursue() -> None:

    trust = TrustScore(
        score=1.0,
        confidence="high",
    )

    decision = DecisionEngine().compute(trust)

    assert decision.action == "pursue"
    assert decision.reason == "High confidence."
