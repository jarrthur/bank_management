import pytest

from contracts.contract import Contract
from contracts.adapters import ContractOpenFilter, ContractDebtSorter
from services.contract import ContractOpenService


def create_contract_list(n):
    return [Contract(i, i * 100) for i in range(1, n + 1)]


def create_contract_open_service(
    contract_filter=ContractOpenFilter, contract_sorter=ContractDebtSorter
):
    return ContractOpenService(
        contract_filter=contract_filter(), contract_sorter=contract_sorter()
    )


@pytest.mark.parametrize(
    "open_contracts, renegotiated_contracts, top_n, expected",
    [
        (create_contract_list(5), [3], 3, [5, 4, 2]),
        (create_contract_list(3), [2], 2, [3, 1]),
        (create_contract_list(2), [1, 2], 1, []),  # All contracts renegotiated
        ([], [], 0, []),  # Empty list
        (create_contract_list(1), [], 1, [1]),  # One contract, empty renegotiated list
        (create_contract_list(1), [], 0, []),  # top_n = 0
    ],
)
def test_get_top_n_open_contracts(
    open_contracts, renegotiated_contracts, top_n, expected
):
    contract_service = create_contract_open_service()
    assert (
        contract_service.get_top_n_open_contracts(
            open_contracts, renegotiated_contracts, top_n
        )
        == expected
    )


@pytest.mark.parametrize(
    "open_contracts, renegotiated_contracts, top_n",
    [
        (create_contract_list(1), [], -1),  # top_n negative
        (
            create_contract_list(1),
            [],
            2,
        ),  # top_n greater than the total number of contracts
        ([], [], 1),  # Empty list, top_n > open_contracts
    ],
)
def test_get_top_n_open_contracts_invalid(
    open_contracts, renegotiated_contracts, top_n
):
    contract_service = create_contract_open_service()
    with pytest.raises(ValueError):
        contract_service.get_top_n_open_contracts(
            open_contracts, renegotiated_contracts, top_n
        )


# TODO: Implement tests for performance with pytest-benchmark
