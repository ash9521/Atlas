from __future__ import annotations

from typing import Any

from atlas.discovery.models import Observation
from atlas.discovery.normalization.models import (
    NormalizedObservation,
)


class ObservationNormalizer:
    """
    Produces a normalized observation using deterministic rules only.
    """

    def normalize(
        self,
        observation: Observation,
    ) -> NormalizedObservation:
        payload = {
            self._normalize_key(key): self._normalize_value(value)
            for key, value in observation.payload.items()
            if self._keep_value(value)
        }

        return NormalizedObservation.create(
            observation=observation,
            payload=payload,
        )

    def _normalize_key(
        self,
        key: str,
    ) -> str:
        return " ".join(key.strip().split())

    def _normalize_value(
        self,
        value: Any,
    ) -> Any:
        if isinstance(value, str):
            return " ".join(value.strip().split())

        return value

    def _keep_value(
        self,
        value: Any,
    ) -> bool:
        if value is None:
            return False

        if isinstance(value, str):
            return value.strip() != ""

        return True
