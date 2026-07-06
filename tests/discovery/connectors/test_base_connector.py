from atlas.discovery.connectors import BaseConnector
from atlas.discovery.models import InputSource, Observation


class DummyConnector(BaseConnector):
    @property
    def name(self) -> str:
        return "dummy"

    def acquire(
        self,
        source: InputSource,
    ) -> list[Observation]:
        return [
            Observation.create(
                connector=self.name,
                payload={"location": source.location},
            ),
        ]


def test_connector_name():
    connector = DummyConnector()

    assert connector.name == "dummy"


def test_connector_returns_observations():
    connector = DummyConnector()

    source = InputSource.create(
        source_type="file",
        location="buyers.xlsx",
    )

    observations = connector.acquire(source)

    assert len(observations) == 1
    assert observations[0].connector == "dummy"
    assert observations[0].payload["location"] == "buyers.xlsx"
