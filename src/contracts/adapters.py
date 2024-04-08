from typing import List
from operator import attrgetter

from .contract import Contract
from .ports import IContractFilter, IContractSorter


class ContractOpenFilter(IContractFilter):
    """Filters open contracts"""

    def filter_contracts(
        self, contracts: List[Contract], contracts_ids_filter: List[int]
    ) -> List[Contract]:
        if not contracts_ids_filter:
            return contracts

        contracts_index, contracts_ids_filter_set = self._filter_strategy(
            contracts, contracts_ids_filter
        )
        return [
            contract
            for contract_id, contract in contracts_index.items()
            if contract_id not in contracts_ids_filter_set
        ]

    def _filter_strategy(
        self, contracts: List[Contract], contracts_ids_filter: List[int]
    ) -> tuple[dict[int, Contract], set[int]]:
        """
        Using a set and dictionary for pre-indexing
        to improve the performance of the filter
        """
        contracts_index = {contract.contract_id: contract for contract in contracts}
        contracts_ids_filter_set = set(contracts_ids_filter)
        return contracts_index, contracts_ids_filter_set


class ContractDebtSorter(IContractSorter):
    """Order contracts by debt"""

    @staticmethod
    def sort_contracts(contracts: List[Contract], desc=True) -> List[Contract]:
        """Using .sort() to not need to create a new list"""
        contracts.sort(key=attrgetter("debt"), reverse=desc)
        return contracts
