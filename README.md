# Bank Management

## Description

This project aims to provide a solution for optimizing the distribution of monetary requests across bank agencies via armored car deliveries. It incorporates two main functionalities: determining the top N debtors from a list of contracts and optimizing the combination of orders to minimize the number of trips required under certain constraints.

## Features and how it works

- **Top N Debtors**: Identify the top N debtors who have not renegotiated their debts, sorted by the amount owed. The system filters out renegotiated contracts and sorts the remaining contracts by the debt amount. It then selects the top N debtors based on the sorted list.
- **Order Combination**: Combine nearby agency requests to minimize the number of delivery trips, adhering to security and capacity constraints. Each trip can serve a maximum of two orders without exceeding a predefined monetary limit

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

Follow these steps to set up your development environment:

1. Clone the repository:
    ```bash
    git clone [git@github.com:jarrthur/bank_management.git](https://github.com/jarrthur/bank_management.git)
    ```

2. Navigate to the project directory:
   ```cmd
   cd bank_management
   ```

3. Create and activate a virtual environment:
    - **Linux/macOS**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - **Windows**:
      ```cmd
      python -m venv venv
      .\venv\Scripts\activate
      ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


### Usage

To use the program, run the main script and follow the on-screen prompts to select a functionality:

1. Navigate to the project's root directory
    ```cmd
    cd src/
    ```
2. Execute the `main.py` script using Python:
    ```
    python main.py
    ```
3. Select an option:
    Upon execution, the script will prompt you to choose one of the functionalities by entering a corresponding number:

    * Enter 1 to retrieve the top N debtors.
    * Enter 2 to combine orders and calculate the minimum number of required trips

## Tests
With pytest installed, you can execute all tests in the project from the root directory with the following command:
```
pytest
```
