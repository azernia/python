# 判断字符串是否为数字

# 方法一：使用正则表达式
import re
def is_number(s):
    if re.match(r'^[0-9]+$', s):
        return True
    else:
        return False
    
# 方法二：使用内置函数
def is_number2(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# 方法三：使用isdigit()
def is_number3(s):
    if s.isdigit():
        return True
    else:
        return False
    
# 方法四：使用unicode
def is_number4(s):
    try:
        if isinstance(float(s), float):
            return True
    except ValueError:
        return False
    
# 方法五：使用ast
import ast
def is_number5(s):
    return isinstance(ast.literal_eval(s), (int, float, complex))

# 方法六：使用numpy
import numpy as np
def is_number6(s):
    try:
        np.float(s)
        return True
    except ValueError:
        return False

# 方法七：使用pandas
import pandas as pd
def is_number7(s):
    try:
        pd.to_numeric(s)
        return True
    except ValueError:
        return False