"""
    计算二元一次方程
    ax**2 + bx + c = 0
"""
import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
delta = b**2 - 4*a*c
if delta < 0:
    print('方程无解')
elif delta == 0:
    print('方程有唯一解x = ', -b/(2*a))
else:
    print('方程有两个解x1 = ', (-b + math.sqrt(delta))/(2*a), 'x2 = ', (-b - math.sqrt(delta))/(2*a))