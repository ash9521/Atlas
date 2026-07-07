from pathlib import Path

from atlas.brain.models import Company
from atlas.brain.repositories import CompanyRepository
from atlas.discovery.connectors import ExcelConnector
from atlas.discovery.ingestion import EvidenceFactory
from atlas.discovery.models import InputSource
from atlas.discovery.normalization import ObservationNormalizer
from atlas.discovery.resolution import CompanyResolver
from atlas.discovery.services import DiscoveryPipelineService


class Application:
    """
    Atlas application entry point.
    """

    def run(
        self,
        argv: list[str],
    ) -> int:
        print("=" * 37)
        print("Atlas Export Intelligence")
        print("Version 0.1")
        print("=" * 37)
        print()

        if not argv:
            print("Usage:")
            print("  python -m atlas <excel-file>")
            return 1

        filename = Path(argv[0])

        if not filename.exists():
            print(f"Error: File not found: {filename}")
            return 1

        print(f"Loading: {filename}")
        print()

        repository = CompanyRepository(
            [
                Company.create(
                    legal_name="ABC Imports",
                ),
                Company.create(
                    legal_name="Nordic Foods",
                ),
                Company.create(
                    legal_name="Global Spice Trading",
                ),
                Company.create(
                    legal_name="Bharat Foods",
                ),
                Company.create(
                    legal_name="Sunrise Imports",
                ),
            ]
        )

        pipeline = DiscoveryPipelineService(
            connector=ExcelConnector(),
            normalizer=ObservationNormalizer(),
            resolver=CompanyResolver(
                repository,
            ),
            evidence_factory=EvidenceFactory(),
        )

        source = InputSource.create(
            source_type="file",
            location=str(filename),
        )

        evidence = pipeline.run(source)

        print(f"Evidence Created: {len(evidence)}")
        print()
        print("Completed successfully.")

        return 0
