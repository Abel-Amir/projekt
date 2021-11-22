# my_list = [3, 4, 81, 35, 22]

# def buble_sort(my_list):
#     lenght = len(my_list)
#     for i in range(lenght):
#         for b in range(lenght - i - 1):
#             if my_list[b] > my_list[b+1]:
#                 temp = my_list[b]
#                 my_list[b] = my_list[b + 1]
#                 my_list[b+1] = temp
#
# buble_sort(my_list)
# print(my_list)

# 2 вариант
# def buble_sort(my_list):
#     swapped = False
#     for i in range(len(my_list) - 1, 0, - 1):
#         for j in range(i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break
#     return my_list
# print(f"sort list: {buble_sort(my_list = my_list)}")

#быстрая сортировка
my_list = [12, 4, 35, 23, 55, 44]

def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    element = my_list[0]
    left = list(filter(lambda num: num < element, my_list))
    center = [num for num in my_list if num == element]
    right = list(filter(lambda num: num > element, my_list))
    return quick_sort(left) + center + quick_sort(right)

print(f"sorted list: {quick_sort(my_list)}")