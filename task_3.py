"""
3. сгенерировать список чисел от -Х од Х и найти максимальное и минимальное число в списке 
"""
import random
lst = [ i for i in range(int(input("Enter the first number of the list:  ")), int(input("Enter the last numver of the list:  "))+1)]
print(f"Generated list: {lst}")
print(f" Max number in the list: {max(lst)} , min number: {min(lst)}")

