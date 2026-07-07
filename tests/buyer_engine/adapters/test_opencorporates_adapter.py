from atlas.buyer_engine.acquisition import PublicDirectoryClient
from atlas.buyer_engine.adapters import OpenCorporatesAdapter


class FakeClient(PublicDirectoryClient):
    def get(
        self,
        url: str,
    ) -> str:
        assert "companies/search" in url
        return '{"results": []}'


def test_search_returns_raw_observation() -> None:
    adapter = OpenCorporatesAdapter(
        FakeClient(),
    )

    observations = adapter.search(
        "turmeric germany",
    )

    assert len(observations) == 1

    observation = observations[0]

    assert observation.connector == "opencorporates"
    assert observation.payload["Query"] == "turmeric germany"
