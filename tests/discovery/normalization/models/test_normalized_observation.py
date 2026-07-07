from atlas.discovery.models import Observation
from atlas.discovery.normalization.models import (
    NormalizedObservation,
)


def test_normalized_observation_preserves_origin() -> None:
    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "ABC Imports",
        },
    )

    normalized = NormalizedObservation.create(
        observation=observation,
        payload=observation.payload,
    )

    assert normalized.observation_id == observation.id
    assert normalized.connector == observation.connector
    assert normalized.acquired_at == observation.acquired_at
    assert normalized.payload == observation.payload
    assert normalized.metadata == observation.metadata
    assert normalized.confidence == observation.confidence
