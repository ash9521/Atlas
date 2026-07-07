from __future__ import annotations

from pathlib import Path
from urllib.parse import urlencode

from atlas.networking.http_client import HttpClient


class KompassClient:
    """
    Retrieves Kompass search pages.
    """

    BASE_URL = "https://in.kompass.com/searchCompanies"

    def __init__(
        self,
        http_client: HttpClient | None = None,
    ) -> None:
        self._http = http_client or HttpClient()

    def build_search_url(
        self,
        product: str,
        country: str | None = None,
    ) -> str:

        search = product

        if country:
            search = f"{product} {country}"

        query = urlencode(
            {
                "text": search,
                "searchType": "PRODUCT",
            }
        )

        return f"{self.BASE_URL}?{query}"

    def load_fixture(
        self,
    ) -> str:

        return Path(
            "tests/fixtures/providers/kompass/search_turmeric_germany.html"
        ).read_text(
            encoding="utf-8",
        )

    def load_live(
        self,
        product: str,
        country: str | None = None,
    ) -> str:

        response = self._http.get(
            self.build_search_url(
                product=product,
                country=country,
            ),
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/138.0.0.0 Safari/537.36"
                ),
                "Accept": (
                    "text/html,"
                    "application/xhtml+xml,"
                    "application/xml;q=0.9,*/*;q=0.8"
                ),
            },
        )

        response.raise_for_status()

        payload = response.text

        self.validate_response(
            payload,
        )

        return payload

    @staticmethod
    def validate_response(
        payload: str,
    ) -> None:

        if not payload.strip():
            raise ValueError(
                "Empty response."
            )

        lower = payload.lower()

        if "<html" not in lower:
            raise ValueError(
                "Not HTML."
            )

        if "captcha" in lower:
            raise ValueError(
                "Captcha detected."
            )

        if "access denied" in lower:
            raise ValueError(
                "Access denied."
            )
