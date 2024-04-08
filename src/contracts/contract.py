class Contract:
    """Represents a contract with an id and a debt"""

    def __init__(self, contract_id: int, debt: float) -> None:
        self.contract_id: int = contract_id
        self.debt: float = debt

    def __str__(self) -> str:
        return f"id={self.contract_id}, debt={self.debt}"
