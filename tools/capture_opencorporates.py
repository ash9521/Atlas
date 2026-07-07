from pathlib import Path

from atlas.networking.http_client import HttpClient

URL = (
    "https://api.opencorporates.com/v0.4/companies/search"
    "?q=turmeric"
)


def main() -> None:
    client = HttpClient()

    response = client.get(URL)

    response.raise_for_status()

    output = Path(
        "production/responses/opencorporates-search.json"
    )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output.write_text(
        response.text,
        encoding="utf-8",
    )

    print(f"Saved response to {output}")


if __name__ == "__main__":
    main()
