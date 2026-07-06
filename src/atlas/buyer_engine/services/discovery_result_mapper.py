"""
Discovery result mapper.

Converts raw discovery results into CandidateCompany objects.
"""

from atlas.buyer_engine.models.candidate_company import CandidateCompany


class DiscoveryResultMapper:
    """
    Maps raw discovery results to CandidateCompany objects.
    """

    @staticmethod
    def map(
        result: dict[str, str],
    ) -> CandidateCompany:
        """
        Convert a raw discovery result into a CandidateCompany.
        """

        return CandidateCompany.create(
            name=result["name"],
            source=result["source"],
            query=result["query"],
        )
