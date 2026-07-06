from unittest.mock import MagicMock, patch

import httpx
import pytest

from atlas.networking.http_client import HttpClient


def test_http_is_rejected():
    client = HttpClient()

    with pytest.raises(ValueError):
        client.get("http://example.com")


@patch("atlas.networking.http_client.httpx.Client")
def test_https_request_uses_secure_defaults(mock_client):
    response = MagicMock(spec=httpx.Response)

    mock_instance = MagicMock()
    mock_instance.get.return_value = response

    mock_client.return_value.__enter__.return_value = mock_instance

    client = HttpClient(timeout=5.0)

    result = client.get("https://example.com")

    assert result is response

    mock_client.assert_called_once_with(
        timeout=5.0,
        follow_redirects=False,
    )

    mock_instance.get.assert_called_once()

    args, kwargs = mock_instance.get.call_args

    assert args[0] == "https://example.com"

    assert kwargs["headers"]["User-Agent"].startswith("Atlas/")
