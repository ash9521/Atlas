"""
Unit tests for the EvidenceSource domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from atlas.brain.models.evidence_source import EvidenceSource


def test_create_valid_evidence_source() -> None:
    source = EvidenceSource.create(
        source_type="government_api",
        name="DGFT API",
        version="v1",
    )

    assert source.source_type == "government_api"
    assert source.name == "DGFT API"
    assert source.version == "v1"


def test_empty_source_type_raises_value_error() -> None:
    with pytest.raises(ValueError):
        EvidenceSource.create(
            source_type="",
            name="DGFT API",
        )


def test_empty_name_raises_value_error() -> None:
    with pytest.raises(ValueError):
        EvidenceSource.create(
            source_type="government_api",
            name="",
        )


def test_empty_version_becomes_none() -> None:
    source = EvidenceSource.create(
        source_type="government_api",
        name="DGFT API",
        version="   ",
    )

    assert source.version is None


def test_evidence_source_is_immutable() -> None:
    source = EvidenceSource.create(
        source_type="government_api",
        name="DGFT API",
    )

    with pytest.raises(FrozenInstanceError):
        source.name = "Changed"
