import random
import string

char_list = []
for el in (string.ascii_uppercase + string.ascii_lowercase):
    char_list.append(el)

random_list = random.choices(char_list, k = int(input("what length shod be?")))
rand_string = "".join(random_list)


print(f"Random string >>> {rand_string}\n\
Reversed random string {rand_string[::-1]}")
