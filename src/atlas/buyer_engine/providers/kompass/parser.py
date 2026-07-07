from __future__ import annotations

from bs4 import BeautifulSoup

from atlas.buyer_engine.models import BuyerRecord


class KompassParser:
    """
    Parses Kompass HTML into BuyerRecord objects.
    """

    def parse(
        self,
        payload: str,
    ) -> tuple[BuyerRecord, ...]:

        soup = BeautifulSoup(
            payload,
            "lxml",
        )

        buyers: list[BuyerRecord] = []

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

            buyers.append(
                BuyerRecord(
                    company=company_name,
                    country=country,
                    website=website,
                    source="kompass",
                    source_id=source_id,
                )
            )

        return tuple(buyers)
