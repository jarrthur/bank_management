from abc import ABC, abstractmethod
from typing import List


class IOrderCombinationStrategy(ABC):
    @abstractmethod
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        """Calculates the minimum number of trips necessary to meet all requests.

        Args:
            requests (list of int): List of monetary values requested by agencies.
            n_max (int): Maximum value that can be transported in a single trip.

        Returns:
            int: Minimum number of trips required.

        note:
            - Each trip can fulfill a maximum of 2 requests.
            - It is assumed that no value in 'requests' is greater than 'n_max'.
        """
