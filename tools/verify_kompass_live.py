from pathlib import Path

from atlas.buyer_engine.providers.kompass import KompassClient


def main() -> None:
    client = KompassClient()

    html = client.load_live(
        product="turmeric",
        country="Germany",
    )

    output = Path(
        "production/responses/kompass_live.html"
    )

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output.write_text(
        html,
        encoding="utf-8",
    )

    print("=" * 60)
    print("SUCCESS")
    print("=" * 60)
    print(f"Saved to: {output}")
    print(f"Characters: {len(html):,}")


if __name__ == "__main__":
    main()
