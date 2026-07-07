from atlas.buyer_engine.parsers import (
    OpenCorporatesParser,
)


def test_parse_company() -> None:

    parser = OpenCorporatesParser()

    payload = """
{
  "results": {
    "companies": [
      {
        "company": {
          "name": "ABC Imports GmbH",
          "current_jurisdiction": "Germany",
          "company_number": "HRB12345"
        }
      }
    ]
  }
}
"""

    records = parser.parse(payload)

    assert len(records) == 1

    assert records[0].company == "ABC Imports GmbH"
    assert records[0].country == "Germany"
    assert records[0].source == "opencorporates"
    assert records[0].source_id == "HRB12345"
