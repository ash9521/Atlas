from atlas.brain.models import Company, Evidence
from atlas.brain.repositories import CompanyRepository
from atlas.buyer_engine.models import (
    BuyerSearchRequest,
    Product,
)
from atlas.buyer_engine.services import (
    AutonomousBuyerDiscoveryService,
)
from atlas.discovery.connectors import ExcelConnector
from atlas.discovery.ingestion import EvidenceFactory
from atlas.discovery.normalization import (
    ObservationNormalizer,
)
from atlas.discovery.resolution import CompanyResolver
from atlas.discovery.services import (
    DiscoveryPipelineService,
)


class DummyConnector(ExcelConnector):
    def acquire(self, source):
        return []


def test_execute_returns_evidence() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    pipeline = DiscoveryPipelineService(
        connector=DummyConnector(),
        normalizer=ObservationNormalizer(),
        resolver=CompanyResolver(
            CompanyRepository([company]),
        ),
        evidence_factory=EvidenceFactory(),
    )

    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
        country="Germany",
        buyer_type="Importer",
    )

    evidence = AutonomousBuyerDiscoveryService(
        pipeline,
    ).execute(
        request,
    )

    assert isinstance(evidence, tuple)
    assert len(evidence) == 1
    assert isinstance(evidence[0], Evidence)
