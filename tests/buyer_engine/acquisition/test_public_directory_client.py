from unittest.mock import MagicMock

import httpx

from atlas.buyer_engine.acquisition import (
    PublicDirectoryClient,
)
from atlas.networking.http_client import HttpClient


class FakeHttpClient(HttpClient):
    def get(
        self,
        url: str,
    ) -> httpx.Response:
        response = MagicMock(spec=httpx.Response)

        response.raise_for_status.return_value = None
        response.text = "<html>directory page</html>"

        return response


def test_get_returns_html() -> None:
    client = PublicDirectoryClient(
        FakeHttpClient(),
    )

    html = client.get(
        "https://example.com",
    )

    assert html == "<html>directory page</html>"
