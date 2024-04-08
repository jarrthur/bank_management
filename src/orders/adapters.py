from typing import List

from orders.ports import IOrderCombinationStrategy


class TwoPointerOrderCombinationStrategy(IOrderCombinationStrategy):
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        if not requests:
            return 0
        self._valid_n_max(n_max)

        requests.sort(reverse=True)
        trips = 0
        left, right = 0, len(requests) - 1

        while left <= right:
            if left == right:
                trips += 1
                break
            if requests[left] + requests[right] <= n_max:
                right -= 1
            left += 1
            trips += 1

        return trips

    def _valid_n_max(self, n_max: int) -> None:
        if n_max <= 0:
            raise ValueError("n_max must be greater than 0.")

    def _valid_requests(self, requests: List[int], n_max: int) -> None:
        if any(request < 0 or request > n_max for request in requests):
            raise ValueError("Invalid request.")
