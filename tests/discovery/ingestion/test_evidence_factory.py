from atlas.brain.models import Company
from atlas.discovery.ingestion import EvidenceFactory
from atlas.discovery.models import Observation
from atlas.discovery.normalization import ObservationNormalizer


def test_create_evidence() -> None:
    company = Company.create(
        legal_name="ABC Imports",
    )

    observation = Observation.create(
        connector="excel",
        payload={
            "Company": "ABC Imports",
            "Country": "Germany",
        },
    )

    normalized = ObservationNormalizer().normalize(
        observation,
    )

    evidence = EvidenceFactory().create(
        company=company,
        observation=normalized,
    )

    assert evidence.company_id == company.id
    assert evidence.evidence_type == "buyer.discovery"
    assert evidence.source.source_type == "connector"
    assert evidence.source.name == "excel"
    assert evidence.payload["Company"] == "ABC Imports"
    assert evidence.payload["Country"] == "Germany"
    assert evidence.observed_at == normalized.acquired_at
