"""4. получить от пользователя список чисел, вывести их на экран, поделить пополам и поменять первую половину на вторую 
"""
num_list = input("Enter a list of numbers. Ex: 2,4,...8 ").split(",")
half_1 = num_list[:((len(num_list)//2))]
half_2 = num_list[(len(num_list)//2):]
print(half_1,half_2)
half_1,half_2 = half_2,half_1
print(half_1,half_2)