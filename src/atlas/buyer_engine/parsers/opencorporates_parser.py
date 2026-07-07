from __future__ import annotations

import json

from atlas.buyer_engine.models import BuyerRecord


class OpenCorporatesParser:
    """
    Parses OpenCorporates responses into BuyerRecord objects.
    """

    def parse(
        self,
        payload: str,
    ) -> tuple[BuyerRecord, ...]:

        document = json.loads(payload)

        companies = (
            document
            .get("results", {})
            .get("companies", [])
        )

        records: list[BuyerRecord] = []

        for item in companies:

            company = item.get("company", {})

            records.append(
                BuyerRecord(
                    company=company.get("name", ""),
                    country=company.get(
                        "current_jurisdiction",
                        "",
                    ),
                    website=None,
                    source="opencorporates",
                    source_id=company.get(
                        "company_number",
                    ),
                )
            )

        return tuple(records)
