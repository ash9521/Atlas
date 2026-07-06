"""
Discovery task service.

Converts search queries into discovery tasks.
"""

from atlas.buyer_engine.models.discovery_task import DiscoveryTask


class DiscoveryTaskService:
    """
    Creates discovery tasks from search queries.
    """

    @staticmethod
    def create_tasks(
        queries: list[str],
    ) -> list[DiscoveryTask]:
        """
        Convert search queries into immutable discovery tasks.
        """

        return [
            DiscoveryTask.create(
                query=query,
            )
            for query in queries
        ]
