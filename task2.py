from typing import Callable
import re
from decimal import Decimal

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    number_matches = re.findall(r'-?\d+\.?\d*', text)
    
    for match in number_matches:
        try:
            yield float(match)
        except ValueError:
            
            continue
        


def sum_profit(text: str, func: Callable):
    incomes = func(text)
    profit = sum(incomes)
    return profit         
    

def main():
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == '__main__':
    main()