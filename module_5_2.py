import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
