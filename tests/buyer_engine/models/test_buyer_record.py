from atlas.buyer_engine.models import BuyerRecord


def test_create_buyer_record() -> None:
    record = BuyerRecord(
        company="ABC Imports GmbH",
        country="Germany",
        website="https://example.com",
        source="opencorporates",
    )

    assert record.company == "ABC Imports GmbH"
    assert record.country == "Germany"
    assert record.source == "opencorporates"
