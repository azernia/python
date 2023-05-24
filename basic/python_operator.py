# 算数运算符
num1 = 10
num2 = 5
# 加法
print(num1 + num2)
# 减法
print(num1 - num2)
# 乘法
print(num1 * num2)
# 除法
print(num1 / num2)
# 取模
print(num1 % num2)
# 幂 返回x的y次幂
print(num1 ** num2)
# 取整除
print(num1 // num2)
# 比较运算符
# 等于
print(num1 == num2)
# 不等于
print(num1 != num2)
# 大于
print(num1 > num2)
# 小于
print(num1 < num2)
# 大于等于
print(num1 >= num2)
# 小于等于
print(num1 <= num2)
# 赋值运算符
# 简单赋值
num3 = num1 + num2
print(num3)
# 加法赋值
num3 += num1
print(num3)
# 减法赋值
num3 -= num1
print(num3)
# 乘法赋值
num3 *= num1
print(num3)
# 除法赋值
num3 /= num1
print(num3)
# 取模赋值
num3 %= num1
print(num3)
# 幂赋值
num3 **= num1
print(num3)
# 取整除赋值
num3 //= num1
print(num3)
# 位运算符
# 按位与
print(num1 & num2)
# 按位或
print(num1 | num2)
# 按位异或
print(num1 ^ num2)
# 按位取反
print(~num1)
# 左移动
print(num1 << 2)
# 右移动
print(num1 >> 2)
# 逻辑运算符 if 中使用
# 逻辑与
print(num1 and num2)
# 逻辑或
print(num1 or num2)
# 逻辑非
print(not num1)
# 成员运算符
# in
print(num1 in [1, 2, 3, 4, 5])
# not in
print(num1 not in [1, 2, 3, 4, 5])
# 身份运算符 判断两个标识符是不是引用自一个对象
# is
print(num1 is num2)
# is not
print(num1 is not num2)
# 运算符优先级
# ** 指数 (最高优先级)
# ~ + - 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % // 乘，除，取模和取整除
# + - 加法减法
# >> << 右移，左移运算符
# & 位 'AND'
# ^ | 位运算符
# <= < > >= 比较运算符
# <> == != 等于运算符
# = %= /= //= -= += *= **= 赋值运算符
# is is not 身份运算符
# in not in 成员运算符
# not or and 逻辑运算符
# 例子
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d
print("(a + b) * c / d 运算结果为：", e)
e = ((a + b) * c) / d
print("((a + b) * c) / d 运算结果为：", e)
e = (a + b) * (c / d)
print("(a + b) * (c / d) 运算结果为：", e)
e = a + (b * c) / d
print("a + (b * c) / d 运算结果为：", e)