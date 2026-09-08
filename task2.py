from typing import Callable
import re
from decimal import Decimal

text = "income 1000.05 , 333.33"

def generator_numbers(text: str):
    if len(text)>0:
        number_matches = re.findall(r'\s-?\d+\.?\d*\s', text)
        
        for match in number_matches:
            try:
                yield Decimal(match)
            except ValueError:
                
                continue
    else:
        return 0
        


def sum_profit(text: str, func: Callable):
    incomes = func(text)
    profit = sum(incomes)
    return profit         
    

def main():
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == '__main__':
    main()