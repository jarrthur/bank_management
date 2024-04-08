import pytest

from orders.adapters import TwoPointerOrderCombinationStrategy
from services.order import OrderService


def create_order_service(combine_strategy=TwoPointerOrderCombinationStrategy):
    return OrderService(combination_strategy=combine_strategy())


def test_combine_orders_with_negative_n_max():
    order_service = create_order_service()
    requests = [70, 30, 10]
    n_max = -100
    with pytest.raises(ValueError):
        order_service.combine_orders(requests, n_max)


@pytest.mark.parametrize(
    "requests, n_max, expected_orders",
    [
        ([70, 30, 10], 100, 2),  # Default test case
        (
            [50, 50],
            100,
            1,
        ),  # A trip, with an exact combination, exactly on the limit
        ([80, 20, 20], 100, 2),  # Two trips, with an exact combination
        ([], 100, 0),  # Empty list of requests
        ([100], 100, 1),  # Single request, equal to maximum
        ([20], 100, 1),  # Single request, less than maximum
    ],
)
def test_valid_combine_orders(requests, n_max, expected_orders):
    order_service = create_order_service()
    assert order_service.combine_orders(requests, n_max) == expected_orders


@pytest.mark.parametrize(
    "requests, n_max, expected_orders",
    [
        ([70, 30, 10], 100, 2),
        ([100] * 100, 100, 100),  # 100 orders of 100
        ([10] * 100 + [90] * 10, 100, 55),  # 100 orders of 10 and 10 orders of 90
        (
            [1] * 1000,
            2,
            500,
        ),  # 1000 orders of 1, each trip takes exactly 2 orders,
        # probably heavier due to the initial ordering and loops of the algorithm
    ],
)
def test_valid_combine_orders_benchmark(benchmark, requests, n_max, expected_orders):
    order_service = create_order_service()
    result = benchmark(order_service.combine_orders, requests, n_max)
    assert result == expected_orders


# TODO: Implement tests to raise exceptions if one of the request values is negative
# TODO: Implement tests to raise exceptions if one of the request values is greater than n_max
