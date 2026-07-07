from atlas.brain.models import Company
from atlas.brain.repositories import CompanyRepository
from atlas.discovery.connectors import BaseConnector
from atlas.discovery.ingestion import EvidenceFactory
from atlas.discovery.models import InputSource, Observation
from atlas.discovery.normalization import ObservationNormalizer
from atlas.discovery.resolution import CompanyResolver
from atlas.discovery.services import DiscoveryPipelineService


class DummyConnector(BaseConnector):
    @property
    def name(self) -> str:
        return "dummy"

    def acquire(
        self,
        source: InputSource,
    ) -> list[Observation]:
        return [
            Observation.create(
                connector=self.name,
                payload={
                    "Company": "ABC Imports",
                },
            ),
        ]


class UnknownCompanyConnector(BaseConnector):
    @property
    def name(self) -> str:
        return "dummy"

    def acquire(
        self,
        source: InputSource,
    ) -> list[Observation]:
        return [
            Observation.create(
                connector=self.name,
                payload={
                    "Company": "Unknown Company",
                },
            ),
        ]


def create_source() -> InputSource:
    return InputSource.create(
        source_type="file",
        location="buyers.xlsx",
    )


def test_pipeline_returns_evidence() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    service = DiscoveryPipelineService(
        connector=DummyConnector(),
        normalizer=ObservationNormalizer(),
        resolver=CompanyResolver(
            CompanyRepository([company]),
        ),
        evidence_factory=EvidenceFactory(),
    )

    evidence = service.run(
        create_source(),
    )

    assert len(evidence) == 1
    assert evidence[0].company_id == company.id


def test_pipeline_skips_unknown_company() -> None:
    service = DiscoveryPipelineService(
        connector=UnknownCompanyConnector(),
        normalizer=ObservationNormalizer(),
        resolver=CompanyResolver(
            CompanyRepository(),
        ),
        evidence_factory=EvidenceFactory(),
    )

    evidence = service.run(
        create_source(),
    )

    assert evidence == ()
