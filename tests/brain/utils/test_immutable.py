"""
Unit tests for immutable utilities.
"""

from types import MappingProxyType

import pytest

from atlas.brain.utils.immutable import freeze


def test_freeze_creates_deeply_immutable_structure() -> None:
    payload = {
        "company": {
            "name": "Atlas",
            "countries": ["India", "Germany"],
        }
    }

    frozen = freeze(payload)

    assert isinstance(frozen, MappingProxyType)
    assert frozen["company"]["name"] == "Atlas"

    with pytest.raises(TypeError):
        frozen["company"]["name"] = "Changed"

    with pytest.raises(AttributeError):
        frozen["company"]["countries"].append("USA")


def test_freeze_rejects_non_string_keys() -> None:
    with pytest.raises(TypeError):
        freeze({1: "value"})


def test_freeze_rejects_unsupported_types() -> None:
    class Dummy:
        pass

    with pytest.raises(TypeError):
        freeze({"dummy": Dummy()})
