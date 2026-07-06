from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from types import MappingProxyType
from typing import Any, Mapping
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Observation:
    """
    A source-independent commercial observation.
    """

    id: UUID
    connector: str
    acquired_at: datetime
    payload: Mapping[str, Any]
    metadata: Mapping[str, Any]
    confidence: float

    @classmethod
    def create(
        cls,
        *,
        connector: str,
        payload: Mapping[str, Any],
        metadata: Mapping[str, Any] | None = None,
        confidence: float = 1.0,
    ) -> "Observation":
        connector = connector.strip()

        if not connector:
            raise ValueError("connector cannot be empty")

        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")

        return cls(
            id=uuid4(),
            connector=connector,
            acquired_at=datetime.now(UTC),
            payload=MappingProxyType(dict(payload)),
            metadata=MappingProxyType(dict(metadata or {})),
            confidence=confidence,
        )
