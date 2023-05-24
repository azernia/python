# 计算图形的面积

def cal_triangle_area(a, b, c):
    # 计算三角形的面积
    # 三角形的面积公式：S = sqrt(p * (p - a) * (p - b) * (p - c))
    if a + b > c and a + c > b and b + c > a:
        p = (a+b+c)/2 # 半周长及周长的一半
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('三角形的面积是：', area)
    else:
        print('不能构成三角形')

def cal_rectangle_area(a, b):
    # 计算长方形的面积
    # 长方形的面积公式：S = a * b
    area = a * b
    print('长方形的面积是：', area)

def cal_circle_area(r):
    # 计算圆形的面积
    # 圆形的面积公式：S = pi * r * r
    pi = 3.1415926
    area = pi * r * r
    print('圆形的面积是：', area)