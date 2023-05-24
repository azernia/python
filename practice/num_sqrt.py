import cmath

# 正数求平方根
positive_num = float(input("Enter a positive number: "))
num_sqrt = positive_num ** 0.5
print("The square root of %0.3f is %0.3f" % (positive_num, num_sqrt))

# 负数求平方根
negative_num = float(input("Enter a negative number: "))
num_sqrt = cmath.sqrt(negative_num)
print("The square root of %0.3f is %0.3f + %0.3fj" % (negative_num, num_sqrt.real, num_sqrt.imag))