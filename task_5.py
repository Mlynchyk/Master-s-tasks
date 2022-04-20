"""
5. получить от пользователя список символов и поднять их в верхний регистр 
"""
user_list = input("Enter letter, sepatared with whitespaces. Ex: a b c d... :").split(" ")
mod_list = [i.upper() for i in user_list]
print(f"Your list:        {user_list}")
print(f"Modified list is: {mod_list}")