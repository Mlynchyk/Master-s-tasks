"""
7. объединить два числовых массива, повтояющиеся числа не должны входить в финальный массив 
"""
# first var
arr_1 = [1,2,3,4,5,6,7,8,9]
arr_2 = [2,4,6,8,0,11,13,15]
print(f"Uniq numbers: {set(arr_1 + arr_2)}")
# second var
sum_arr = arr_1 + arr_2
final_arr = []
for i in sum_arr:
    if i not in final_arr:
        final_arr.append(i)
print(f"Uniq numbers: {final_arr}")
