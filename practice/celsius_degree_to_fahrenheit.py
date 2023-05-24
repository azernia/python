# 摄氏度转华氏度
# 接收用户输入
celsius = float(input('输入摄氏温度: '))
 
# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('{}摄氏温度转为华氏温度为{}'.format(celsius, fahrenheit))