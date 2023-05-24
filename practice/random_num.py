# 随机数

import random

# 生成 0 ~ 1 之间的随机数
print(random.random())

# 生成 0 ~ 100 之间的随机数
print(random.randint(0, 100))

# 生成 0 ~ 100 之间的随机数，每次增加 2
print(random.randrange(0, 100, 2))

# 生成 0 ~ 1 之间的随机数，每次增加 0.5
print(random.uniform(0, 1))

# 从序列中随机选取一个元素
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 从序列中随机选取多个元素
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# 将序列中的元素随机排序
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list1)
print(list1)

# 生成随机验证码
code = ''
for i in range(4):
    # 随机生成 0 ~ 9 的数字
    num = random.randint(0, 9)
    code += str(num)
print(code)