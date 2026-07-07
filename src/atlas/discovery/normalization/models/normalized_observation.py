from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from types import MappingProxyType
from typing import Any, Mapping
from uuid import UUID, uuid4

from atlas.brain.utils.immutable import freeze
from atlas.discovery.models import Observation


@dataclass(frozen=True, slots=True)
class NormalizedObservation:
    """
    A normalized, immutable observation.

    This object preserves a link to the original Observation while
    containing only deterministic transformations.
    """

    id: UUID
    observation_id: UUID
    connector: str
    acquired_at: datetime
    normalized_at: datetime
    payload: Mapping[str, Any]
    metadata: Mapping[str, Any]
    confidence: float

    @classmethod
    def create(
        cls,
        *,
        observation: Observation,
        payload: Mapping[str, Any],
    ) -> "NormalizedObservation":

        return cls(
            id=uuid4(),
            observation_id=observation.id,
            connector=observation.connector,
            acquired_at=observation.acquired_at,
            normalized_at=datetime.now(UTC),
            payload=freeze(payload),
            metadata=MappingProxyType(dict(observation.metadata)),
            confidence=observation.confidence,
        )
