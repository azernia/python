"""
Python 循环
"""

# for in
for i in range(5):  # 遍历一个范围内的数字
    print(i, end=" ")

# 正向/反向遍历一个集合
colors = ["red", "yellow", "blue", "green"]
# 正向
for i in range(len(colors)):
    print(colors[i], end=" ")

# 反向
for i in range(len(colors) - 1, -1, -1):
    print(colors[i], end=" ")

# 遍历一个集合及其下标
for i, color in enumerate(colors):
    print(i, '--->', color)

# 遍历两个集合
students = ["a", "b"]
genders = ["male", "female"]
# 方式一
length = min(len(students), len(genders))
for i in range(length):
    print(students[i], "--->", genders[i])

# 方式二
for student, gender in zip(students, genders):
    print(student, "--->", gender)

# 有序遍历
grades = [
    (1, "6"),
    (2, "8")
]
# 正序
for grade in sorted(grades):
    print(grade)