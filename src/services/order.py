from typing import List
from orders.ports import IOrderCombinationStrategy
from orders.adapters import TwoPointerOrderCombinationStrategy


class OrderService:
    """
    Class responsible for calculating the minimum number of trips required
    to meet all order requests, considering a maximum value per trip
    and a maximum of 2 orders per trip.
    """

    def __init__(
        self,
        combination_strategy: IOrderCombinationStrategy = TwoPointerOrderCombinationStrategy(),
    ):
        self.combination_strategy = combination_strategy

    def combine_orders(self, requests: List[int], n_max: int) -> int:
        return self.combination_strategy.combine_orders(requests, n_max)
