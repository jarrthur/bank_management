from contracts.adapters import ContractOpenFilter, ContractDebtSorter
from contracts.contract import Contract
from services.contract import ContractOpenService
from orders.adapters import TwoPointerOrderCombinationStrategy
from services.order import OrderService


def get_top_debtors() -> None:
    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5),
    ]
    renegotiated = [3]
    top_n = 3
    contract_service = ContractOpenService(
        contract_filter=ContractOpenFilter(), contract_sorter=ContractDebtSorter()
    )
    top_debtors: list[int] = contract_service.get_top_n_open_contracts(
        contracts, renegotiated, top_n
    )
    print("Top N Debtors:", top_debtors)


def combine_orders() -> None:
    orders = [70, 30, 10]
    n_max = 100
    order_service = OrderService(
        combination_strategy=TwoPointerOrderCombinationStrategy()
    )
    how_many = order_service.combine_orders(orders, n_max)
    print("How many trips:", how_many)


def main():
    print("Select an option:")
    print("1 - Get top N debtors")
    print("2 - Combine orders")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        get_top_debtors()
    elif choice == "2":
        combine_orders()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
