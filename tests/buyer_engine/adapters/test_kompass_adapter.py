from atlas.buyer_engine.acquisition import (
    PublicDirectoryClient,
)
from atlas.buyer_engine.adapters import (
    KompassAdapter,
)


class FakeDirectoryClient(PublicDirectoryClient):
    def get(
        self,
        url: str,
    ) -> str:
        assert "Turmeric+Germany" in url
        return "<html>OK</html>"


def test_search_downloads_html() -> None:
    adapter = KompassAdapter(
        FakeDirectoryClient(),
    )

    html = adapter.search(
        "Turmeric Germany",
    )

    assert html == "<html>OK</html>"
