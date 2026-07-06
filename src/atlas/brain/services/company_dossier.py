"""
Company dossier returned by the Brain.

A dossier is Atlas's current view of everything it knows
about a company.
"""

from __future__ import annotations

from dataclasses import dataclass

from atlas.brain.models import Company, Evidence


@dataclass(slots=True, frozen=True)
class CompanyDossier:
    """
    Computed company view.
    """

    company: Company
    evidence: tuple[Evidence, ...]

    @property
    def evidence_count(self) -> int:
        return len(self.evidence)
