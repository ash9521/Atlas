from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from types import MappingProxyType
from typing import Any, Mapping
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class InputSource:
    """
    Represents the origin of commercial intelligence.
    """

    id: UUID
    source_type: str
    location: str
    acquired_at: datetime
    metadata: Mapping[str, Any]

    @classmethod
    def create(
        cls,
        *,
        source_type: str,
        location: str,
        metadata: Mapping[str, Any] | None = None,
    ) -> "InputSource":
        source_type = source_type.strip().lower()
        location = location.strip()

        if not source_type:
            raise ValueError("source_type cannot be empty")

        if not location:
            raise ValueError("location cannot be empty")

        return cls(
            id=uuid4(),
            source_type=source_type,
            location=location,
            acquired_at=datetime.now(UTC),
            metadata=MappingProxyType(dict(metadata or {})),
        )
