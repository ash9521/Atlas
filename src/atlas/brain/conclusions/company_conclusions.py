"""
Computed conclusions.

Conclusions are derived from facts and are never persisted.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CompanyConclusions:
    """
    High-level conclusions about a company.
    """

    has_evidence: bool
    evidence_is_diverse: bool
    latest_data_available: bool
