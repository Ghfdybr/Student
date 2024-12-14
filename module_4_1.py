from fake_math import divide
from true_math import divide as d_true
print("Введи делимое:")
first = int(input())
print("Введи делитель:")
second = int(input())
print("Применяем школьные знания, результат деления  ", first, " на ",second, " равно ",divide(first, second))
print("Согласно высшей матеиатике, результат деления  ", first, " на ",second, " равно ",d_true(first, second))
