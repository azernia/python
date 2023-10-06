"""
Python 装饰器
"""
import time


def clock_it_deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} execute time: {format(end_time - start_time, '.2f')}")
        return result

    return wrapper


@clock_it_deco
def foo(a, b):
    count = 1
    while True:
        if count > a ** b:
            break
        count += 1


foo(10, 5)
