"""
6. отсортировать массив чисел 
"""

lst = [2,4,5,6,7,8,990,0,-17,3.14]
print(lst)
lst_sort = sorted(lst)
print(lst_sort)
# print(f"sorted list: {lst}")

"""
7. объединить два числовых массива, повтояющиеся числа не должны входить в финальный массив 
"""

# first var
arr_1 = [1,2,3,4,5,6,7,8,9]
arr_2 = [2,4,6,8,0,11,13,15]
print(set(arr_1 + arr_2))
# second var
sum_arr = arr_1 + arr_2
final_arr = []
for i in sum_arr:
    if i not in final_arr:
        final_arr.append(i)
print(final_arr)

"""
8. найти в массиве два максимальных числа. например [1,4,5,8,2,4,6] -> 6,8 
"""
# var 1
arr_1 = [1,2,9,3,4,5,6,7,8]
sorted_arr = sorted(arr_1)
print(f"max elements are  {sorted_arr[-2]} -> {sorted_arr[-1]}")

# var 2
arr_1 = [1,2,9,3,4,5,6,7,8]
max_value = max(arr_1)
max_index = arr_1.index(max_value)
for i in arr_1:
    if i <= max_value and arr_1.index(i) != max_index: i
print(f"max elements are  {max_value} -> {i}")
    