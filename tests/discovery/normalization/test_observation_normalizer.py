from atlas.discovery.models import Observation
from atlas.discovery.normalization import (
    ObservationNormalizer,
)


def test_normalizer_preserves_origin() -> None:
    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "  ABC   Imports  ",
            "Country": " Germany ",
        },
        metadata={
            "sheet": "Buyers",
        },
    )

    normalized = ObservationNormalizer().normalize(observation)

    assert normalized.observation_id == observation.id
    assert normalized.connector == observation.connector
    assert normalized.acquired_at == observation.acquired_at
    assert normalized.metadata == observation.metadata
    assert normalized.confidence == observation.confidence


def test_normalizer_trims_strings() -> None:
    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "  ABC   Imports  ",
        },
    )

    normalized = ObservationNormalizer().normalize(observation)

    assert normalized.payload["Company"] == "ABC Imports"


def test_normalizer_removes_empty_values() -> None:
    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "ABC",
            "Email": "",
            "Phone": "   ",
            "Website": None,
        },
    )

    normalized = ObservationNormalizer().normalize(observation)

    assert normalized.payload == {
        "Company": "ABC",
    }
