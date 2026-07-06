from atlas.brain.services import CompanyDossier


def test_dossier_evidence_count() -> None:
    dossier = CompanyDossier(
        company=None,  # type: ignore[arg-type]
        evidence=(),
    )

    assert dossier.evidence_count == 0
