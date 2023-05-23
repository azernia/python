# Python 面向对象编程

# 创建一个简单的类
from typing import Any


class Person:
    __name = "" # __表示声明为私有变量，外部无法访问
    # 构造方法，初始化类的实例，self 代表类的实例
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def say_hi(self):
        print('Hello, my name is', self.__name)
        
# 类的继承
class Student(Person):
    __stu_number = ""
    __gender = 0
    def __init__(self, name, stu_number, gender):
        self.name = name
        self.stu_number = stu_number
        self.gender = gender
        
    def get_stu_number(self):
        return self.stu_number
    
    def set_stu_number(self, stu_number):
        self.stu_number = stu_number
        
    def show_student_info(self):
        print("学号：{}, 姓名: {}, 性别: {}".format(self.stu_number, self.name, "女" if self.gender == 0 else "男"))
        
        
p = Person('Swaroop')   # 实例化对象
p.say_hi()              # 调用类的方法; Hello, my name is Swaroop
p.set_name("张三")
p.say_hi()              # Hello, my name is 张三

stu = Student("张三", "20190101", 1)
stu.show_student_info()