"""
3. сгенерировать список чисел от -Х од Х и найти максимальное и минимальное число в списке 
"""
import random
import random
a = "Enter the first digit of the list:  "
z = "Enter the last digit of the list:  "
lst = [ i for i in range(int(input(a)), int(input(z))+1)]
print(lst)
print(max(lst), min(lst))