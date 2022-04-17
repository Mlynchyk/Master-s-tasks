"""2. сгенерировать список целых чисел и посчитать их сумму """

import string
import random

num_list = []
for i in string.digits:
    num_list.append(int(i))

print(sum(random.choices(num_list, k = int(input("enter quantity of digits to sum")))))