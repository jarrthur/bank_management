from typing import List

from contracts.contract import Contract
from contracts.ports import IContractFilter, IContractSorter


class ContractOpenService:
    """Service responsible for the open contracts use case"""

    def __init__(
        self, contract_filter: IContractFilter, contract_sorter: IContractSorter
    ):
        self.filter = contract_filter
        self.sorter = contract_sorter
        # TODO: Inject a contract validator

    def get_top_n_open_contracts(
        self,
        open_contracts: List[Contract],
        renegotiated_contracts: List[int],
        top_n: int,
    ) -> List[int]:
        """Get the top n open contracts with the highest debt"""
        self._valid_top_n(top_n, open_contracts)

        filtered_contracts = self.filter.filter_contracts(
            open_contracts, renegotiated_contracts
        )
        sorted_contracts = self.sorter.sort_contracts(filtered_contracts, desc=True)
        return self._get_top_n_debtors(sorted_contracts, top_n)

    def _get_top_n_debtors(self, contracts: List[Contract], top_n: int) -> List[int]:
        return [contract.contract_id for contract in contracts[:top_n]]

    def _valid_top_n(self, top_n: int, open_contracts: List[Contract]) -> None:
        if not (0 <= top_n <= len(open_contracts)):
            raise ValueError("Invalid top_n value")

    def _valid_renovated_contracts(
        self, open_contracts: List[Contract], renegotiated_contracts: List[int]
    ) -> None:
        """Check if all renegotiated contracts ids are in the open contracts list"""
        if not all(
            contract_id in open_contracts for contract_id in renegotiated_contracts
        ):
            raise ValueError("Invalid renovated contracts")
