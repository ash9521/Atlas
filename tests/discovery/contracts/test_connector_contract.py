from atlas.discovery.connectors import BaseConnector
from atlas.discovery.models import InputSource, Observation


class ContractConnector(BaseConnector):
    @property
    def name(self) -> str:
        return "contract"

    def acquire(
        self,
        source: InputSource,
    ) -> list[Observation]:
        return [
            Observation.create(
                connector=self.name,
                payload={
                    "location": source.location,
                    "source_type": source.source_type,
                },
            ),
        ]


def test_connector_returns_observations():
    connector = ContractConnector()

    source = InputSource.create(
        source_type="file",
        location="buyers.xlsx",
    )

    observations = connector.acquire(source)

    assert isinstance(observations, list)
    assert len(observations) == 1
    assert isinstance(observations[0], Observation)


def test_connector_does_not_modify_input_source():
    connector = ContractConnector()

    source = InputSource.create(
        source_type="file",
        location="buyers.xlsx",
    )

    original_location = source.location
    original_type = source.source_type

    connector.acquire(source)

    assert source.location == original_location
    assert source.source_type == original_type


def test_connector_name_is_not_empty():
    connector = ContractConnector()

    assert connector.name
    assert connector.name.strip()


def test_connector_sets_observation_connector():
    connector = ContractConnector()

    source = InputSource.create(
        source_type="file",
        location="buyers.xlsx",
    )

    observation = connector.acquire(source)[0]

    assert observation.connector == connector.name
