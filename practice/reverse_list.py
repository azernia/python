# 翻转列表
def reverse_1(lst):
    return [ele for ele in reversed(lst)]

def reverse_2(lst):
    lst.reverse()
    return lst

def reverse_3(lst):
    new_lst = lst[::-1]
    return new_lst
     
lst = [10, 11, 12, 13, 14, 15]
print(reverse_1(lst))
print(reverse_2(lst))
print(reverse_3(lst))
