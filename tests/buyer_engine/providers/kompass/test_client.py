import pytest

from atlas.buyer_engine.providers.kompass import (
    KompassClient,
)


def test_load_fixture() -> None:

    client = KompassClient()

    payload = client.load_fixture()

    assert payload != ""
    assert "<html" in payload.lower()


def test_build_search_url_product() -> None:

    client = KompassClient()

    url = client.build_search_url(
        product="turmeric",
    )

    assert url.startswith("https://")
    assert "turmeric" in url


def test_build_search_url_product_country() -> None:

    client = KompassClient()

    url = client.build_search_url(
        product="turmeric",
        country="Germany",
    )

    assert "turmeric" in url
    assert "Germany" in url


def test_validate_empty_response() -> None:

    with pytest.raises(ValueError):
        KompassClient.validate_response("")


def test_validate_non_html() -> None:

    with pytest.raises(ValueError):
        KompassClient.validate_response("plain text")


def test_validate_access_denied() -> None:

    with pytest.raises(ValueError):
        KompassClient.validate_response(
            "<html>Access Denied</html>"
        )


def test_validate_captcha() -> None:

    with pytest.raises(ValueError):
        KompassClient.validate_response(
            "<html>captcha</html>"
        )
