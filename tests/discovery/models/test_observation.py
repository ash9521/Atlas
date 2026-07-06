from dataclasses import FrozenInstanceError
from datetime import UTC
from uuid import UUID

import pytest

from atlas.discovery.models import Observation


def test_create_observation():
    observation = Observation.create(
        connector="excel",
        payload={"company": "ABC Imports"},
        metadata={"file": "buyers.xlsx"},
        confidence=0.85,
    )

    assert isinstance(observation.id, UUID)
    assert observation.connector == "excel"
    assert observation.acquired_at.tzinfo == UTC
    assert observation.payload["company"] == "ABC Imports"
    assert observation.metadata["file"] == "buyers.xlsx"
    assert observation.confidence == 0.85


@pytest.mark.parametrize(
    "connector",
    [
        "",
        "   ",
    ],
)
def test_connector_cannot_be_empty(connector: str):
    with pytest.raises(ValueError):
        Observation.create(
            connector=connector,
            payload={},
        )


@pytest.mark.parametrize(
    "confidence",
    [
        -0.1,
        1.1,
    ],
)
def test_invalid_confidence(confidence: float):
    with pytest.raises(ValueError):
        Observation.create(
            connector="excel",
            payload={},
            confidence=confidence,
        )


def test_observation_is_immutable():
    observation = Observation.create(
        connector="excel",
        payload={"company": "ABC"},
    )

    with pytest.raises(FrozenInstanceError):
        observation.connector = "google"
