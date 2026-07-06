from dataclasses import FrozenInstanceError

import pytest

from atlas.buyer_engine.models.discovery_task import DiscoveryTask


def test_create_discovery_task():
    task = DiscoveryTask.create(
        query="turmeric importer germany",
    )

    assert task.query == "turmeric importer germany"


def test_query_cannot_be_empty():
    with pytest.raises(ValueError):
        DiscoveryTask.create(
            query="",
        )


def test_discovery_task_is_immutable():
    task = DiscoveryTask.create(
        query="turmeric importer germany",
    )

    with pytest.raises(FrozenInstanceError):
        task.query = "another query"
