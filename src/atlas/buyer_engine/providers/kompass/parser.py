from __future__ import annotations

from bs4 import BeautifulSoup

from atlas.buyer_engine.providers.kompass.models import (
    KompassParsedCompany,
)


class KompassParser:
    """
    Parses Kompass HTML into provider-native models.
    """

    def parse(
        self,
        payload: str,
    ) -> tuple[KompassParsedCompany, ...]:

        soup = BeautifulSoup(
            payload,
            "lxml",
        )

        companies: list[KompassParsedCompany] = []

        for company in soup.select("div.prod_list"):

            name_element = company.select_one(
                "span.titleSpan"
            )

            if name_element is None:
                continue

            company_name = " ".join(
                name_element.get_text().split()
            )

            location_element = company.select_one(
                "span.placeText"
            )

            country = ""

            if location_element is not None:

                location = " ".join(
                    location_element.get_text().split()
                )

                if "-" in location:
                    country = (
                        location.split("-")[-1].strip()
                    )
                else:
                    country = location

            link = company.select_one("a[href]")

            website: str | None = None

            if link is not None:
                href = link.get("href")

                if isinstance(href, str):
                    website = href

            source_id: str | None = None

            identifier = company.get("id")

            if isinstance(identifier, str):
                source_id = identifier

            companies.append(
                KompassParsedCompany(
                    company=company_name,
                    country=country,
                    website=website,
                    source_id=source_id,
                )
            )

        return tuple(companies)
