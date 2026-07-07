from atlas.buyer_engine.acquisition import PublicDirectoryClient
from atlas.buyer_engine.adapters import OpenCorporatesAdapter


class FakeClient(PublicDirectoryClient):

    def get(
        self,
        url: str,
    ) -> str:

        return """
{
  "results": {
    "companies": [
      {
        "company": {
          "name":"ABC Imports GmbH",
          "current_jurisdiction":"Germany",
          "company_number":"HRB12345"
        }
      }
    ]
  }
}
"""


def test_search_returns_observation():

    adapter = OpenCorporatesAdapter(
        FakeClient(),
    )

    observations = adapter.search(
        "turmeric germany",
    )

    assert len(observations) == 1

    observation = observations[0]

    assert observation.payload["Company"] == "ABC Imports GmbH"
    assert observation.payload["Country"] == "Germany"
    assert observation.payload["SourceId"] == "HRB12345"
