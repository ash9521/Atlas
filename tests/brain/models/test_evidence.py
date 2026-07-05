"""
Unit tests for the Evidence domain model.
"""

from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
from types import MappingProxyType
from uuid import uuid4

import pytest

from atlas.brain.models.evidence import Evidence
from atlas.brain.models.evidence_source import EvidenceSource


def create_source() -> EvidenceSource:
    return EvidenceSource.create(
        source_type="government_api",
        name="DGFT API",
    )


def test_create_evidence() -> None:
    evidence = Evidence.create(
        company_id=uuid4(),
        evidence_type="government.registration",
        source=create_source(),
        observed_at=datetime.now(timezone.utc),
        payload={"status": "active"},
    )

    assert evidence.evidence_type == "government.registration"
    assert isinstance(evidence.payload, MappingProxyType)
    assert evidence.recorded_at.tzinfo == timezone.utc


def test_empty_evidence_type_raises() -> None:
    with pytest.raises(ValueError):
        Evidence.create(
            company_id=uuid4(),
            evidence_type="",
            source=create_source(),
            observed_at=datetime.now(timezone.utc),
            payload={"status": "active"},
        )


def test_observed_at_must_be_timezone_aware() -> None:
    with pytest.raises(ValueError):
        Evidence.create(
            company_id=uuid4(),
            evidence_type="government.registration",
            source=create_source(),
            observed_at=datetime.now(),
            payload={"status": "active"},
        )


def test_payload_is_deeply_immutable() -> None:
    evidence = Evidence.create(
        company_id=uuid4(),
        evidence_type="government.registration",
        source=create_source(),
        observed_at=datetime.now(timezone.utc),
        payload={
            "nested": {
                "countries": ["India"]
            }
        },
    )

    with pytest.raises(TypeError):
        evidence.payload["nested"]["country"] = "Germany"

    with pytest.raises(AttributeError):
        evidence.payload["nested"]["countries"].append("Germany")


def test_evidence_is_immutable() -> None:
    evidence = Evidence.create(
        company_id=uuid4(),
        evidence_type="government.registration",
        source=create_source(),
        observed_at=datetime.now(timezone.utc),
        payload={"status": "active"},
    )

    with pytest.raises(FrozenInstanceError):
        evidence.evidence_type = "changed"

def test_payload_is_defensively_copied() -> None:
    original_payload = {
        "status": "active",
    }

    evidence = Evidence.create(
        company_id=uuid4(),
        evidence_type="government.registration",
        source=create_source(),
        observed_at=datetime.now(timezone.utc),
        payload=original_payload,
    )

    assert evidence.payload is not original_payload

    original_payload["status"] = "inactive"

    assert evidence.payload["status"] == "active"
