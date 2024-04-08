from abc import ABC, abstractmethod
from typing import List
from .contract import Contract


class IContractFilter(ABC):
    """
    Implemention for filtering contracts.
    Aiming for future filtering implementations in ETL processes
    """

    @abstractmethod
    def filter_contracts(
        self, contracts: List[Contract], contracts_ids_filter: List[int]
    ) -> List[Contract]:
        """Abstract method for filtering contracts.

        Args:
            contracts (List[Contract]): List of contracts.
            contracts_ids_filter (List[int]): List of IDs to be filtered

        Returns:
            List[Contract]: List of filtered contracts.
        """


class IContractSorter(ABC):
    """
    Implemention for sorting contracts.
    Aiming for future sorting implementations in ETL processes
    """

    @staticmethod
    @abstractmethod
    def sort_contracts(contracts: List[Contract], desc=True) -> List[Contract]:
        """Abstract method for ordering contracts.

        Args:
            contracts (List[Contract]): List of contracts.
            desc (bool, optional): Descending ordering. Defaults to True.

        Returns:
            List[Contract]: List of ordered contracts.
        """
