"""
3. сгенерировать список чисел от -Х од Х и найти максимальное и минимальное число в списке 
"""
import random
a = "Enter the first number of the list:  "
z = "Enter the last numver of the list:  "
lst = [ i for i in range(int(input(a)), int(input(z))+1)]
print(lst)
print(max(lst), min(lst))