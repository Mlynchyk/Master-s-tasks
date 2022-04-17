"""2. сгенерировать список целых чисел и посчитать их сумму """

import random 

num_list = [i for i in range(0,9+1)]
random_numlist = [random.choice(num_list) for n in range(int(input("enter number")))]

print(sum(random_numlist))