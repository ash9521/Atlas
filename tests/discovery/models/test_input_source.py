from dataclasses import FrozenInstanceError
from datetime import UTC
from uuid import UUID

import pytest

from atlas.discovery.models import InputSource


def test_create_input_source():
    source = InputSource.create(
        source_type="file",
        location="buyers.xlsx",
        metadata={"size": 1024},
    )

    assert isinstance(source.id, UUID)
    assert source.source_type == "file"
    assert source.location == "buyers.xlsx"
    assert source.acquired_at.tzinfo == UTC
    assert source.metadata["size"] == 1024


@pytest.mark.parametrize(
    "source_type",
    [
        "",
        "   ",
    ],
)
def test_source_type_cannot_be_empty(source_type: str):
    with pytest.raises(ValueError):
        InputSource.create(
            source_type=source_type,
            location="buyers.xlsx",
        )


@pytest.mark.parametrize(
    "location",
    [
        "",
        "   ",
    ],
)
def test_location_cannot_be_empty(location: str):
    with pytest.raises(ValueError):
        InputSource.create(
            source_type="file",
            location=location,
        )


def test_input_source_is_immutable():
    source = InputSource.create(
        source_type="file",
        location="buyers.xlsx",
    )

    with pytest.raises(FrozenInstanceError):
        source.location = "other.xlsx"
