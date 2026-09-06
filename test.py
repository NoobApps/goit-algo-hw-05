import re
from decimal import Decimal

pattern = r'^\d+(?:\.\d{2})?$'
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    text=text.split()
    incomes = re.match(r'^\d+(?:\.\d{2})?$',text)
    for income in incomes:
        yield float(income)

def main():
    total_income = generator_numbers(text)
    for i in total_income:
        print(f"Загальний дохід: {i}")

if __name__ == '__main__':
    main()