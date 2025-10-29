from typing import Callable
import re

# Генератор через Comprehesion
def sum_profit_gen(text:str):
    pattern = r'\d+\.\d{2}'
    refined_text = re.findall(pattern,text) 
    
    return sum(float(num) for num in refined_text ) # Генератор 

# Генератор через yield
def generator_numbers(text:str):
    for word in re.split(r'\s+',text):
        if re.match(r'\d+\.\d{2}',word):
            yield float(word)

def sum_profit(text:str, func:Callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# Перевірка першого рішення
print(sum_profit(text,generator_numbers))

# Перевірка другого рішення
print(sum_profit_gen(text))
