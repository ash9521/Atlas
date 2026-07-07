from atlas.buyer_engine.contracts import PublicSourceAdapter
from atlas.discovery.models import Observation


class DummyAdapter(PublicSourceAdapter):

    @property
    def name(self) -> str:
        return "dummy"

    def search(
        self,
        query: str,
    ) -> tuple[Observation, ...]:
        return ()


def test_adapter_contract() -> None:
    adapter = DummyAdapter()

    assert adapter.name == "dummy"
    assert adapter.search("turmeric") == ()
