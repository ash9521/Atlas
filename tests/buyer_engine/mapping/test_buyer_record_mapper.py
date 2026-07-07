from atlas.buyer_engine.mapping import BuyerRecordMapper
from atlas.buyer_engine.models import BuyerRecord


def test_map_buyer_record_to_observation() -> None:
    record = BuyerRecord(
        company="ABC Imports GmbH",
        country="Germany",
        website="https://abc.example",
        source="opencorporates",
        source_id="12345",
    )

    mapper = BuyerRecordMapper()

    observation = mapper.map(record)

    assert observation.connector == "opencorporates"
    assert observation.payload["Company"] == "ABC Imports GmbH"
    assert observation.payload["Country"] == "Germany"
    assert observation.payload["Website"] == "https://abc.example"
    assert observation.payload["SourceId"] == "12345"
