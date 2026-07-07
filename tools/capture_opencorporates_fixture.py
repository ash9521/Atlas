from __future__ import annotations

import json
from pathlib import Path

import httpx


URL = (
    "https://api.opencorporates.com/v0.4/companies/search"
    "?q=turmeric"
)


def main() -> None:

    response = httpx.get(
        URL,
        timeout=30,
        headers={
            "User-Agent": (
                "Atlas/0.1 "
                "(Commercial Intelligence Engine)"
            ),
        },
    )

    response.raise_for_status()

    payload = response.json()

    production = Path(
        "production/responses/opencorporates_search.json"
    )

    fixture = Path(
        "tests/fixtures/providers/opencorporates/search_turmeric.json"
    )

    production.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fixture.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    text = json.dumps(
        payload,
        indent=2,
        ensure_ascii=False,
    )

    production.write_text(
        text,
        encoding="utf-8",
    )

    fixture.write_text(
        text,
        encoding="utf-8",
    )

    print("=" * 60)
    print("SUCCESS")
    print("=" * 60)
    print(f"Saved: {production}")
    print(f"Saved: {fixture}")


if __name__ == "__main__":
    main()
