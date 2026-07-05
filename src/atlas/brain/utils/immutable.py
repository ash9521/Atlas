"""
Utilities for creating deeply immutable data structures.
"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import date, datetime
from types import MappingProxyType
from typing import Any
from uuid import UUID


_IMMUTABLE_TYPES = (
    str,
    int,
    float,
    bool,
    bytes,
    type(None),
    UUID,
    datetime,
    date,
)


def freeze(value: Any) -> Any:
    """
    Recursively convert supported mutable Python objects into immutable
    equivalents.

    Rules:

    - Mapping keys must be strings.
    - dict  -> MappingProxyType
    - list  -> tuple
    - tuple -> tuple
    - set   -> frozenset

    Unsupported mutable objects raise TypeError.
    """

    if isinstance(value, _IMMUTABLE_TYPES):
        return value

    if isinstance(value, MappingProxyType):
        return value

    if isinstance(value, Mapping):
        frozen = {}

        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError(
                    f"Payload keys must be strings. Got {type(key).__name__}."
                )

            frozen[key] = freeze(item)

        return MappingProxyType(frozen)

    if isinstance(value, list):
        return tuple(freeze(item) for item in value)

    if isinstance(value, tuple):
        return tuple(freeze(item) for item in value)

    if isinstance(value, set):
        return frozenset(freeze(item) for item in value)

    raise TypeError(
        f"Unsupported payload value type: {type(value).__name__}"
    )
