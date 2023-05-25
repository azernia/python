# Python 日期时间
# Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
# 时间间隔是以秒为单位的浮点小数。
# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
# Python 的 time 模块下有很多函数可以转换常见日期格式。
# 如函数time.time()用于获取当前时间戳, 如下实例:
import time  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)

# 什么是时间元组？
# 很多Python函数用一个元组装起来的9组数字处理时间:
# 序号	字段	值
# 0	4位数年	2008
# 1	月	1 到 12
# 2	日	1到31
# 3	小时	0到23
# 4	分钟	0到59
# 5	秒	0到61 (60或61 是闰秒)
# 6	一周的第几日	0到6 (0是周一)
# 7	一年的第几日	1到366 (儒略历)
# 8	夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
# 上述也就是struct_time元组。这种结构具有如下属性：
# 序号	属性	值
# 0	tm_year	2008
# 1	tm_mon	1 到 12
# 2	tm_mday	1 到 31
# 3	tm_hour	0 到 23
# 4	tm_min	0 到 59
# 5	tm_sec	0 到 61 (60或61 是闰秒)
# 6	tm_wday	0到6 (0是周一)
# 7	tm_yday	一年中的第几天，1 到 366
# 8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
# 获取当前时间
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

# 获取格式化的时间
# 可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

# 格式化日期
# 我们可以使用 time 模块的 strftime 方法来格式化日期，：
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
# 可以使用 time 模块的 strptime 方法来将格式字符串转换为时间戳，：
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# Python中时间日期格式化符号：
# 符号	描述	实例
# %y	两位数的年份表示（00-99）	18
# %Y	四位数的年份表示（000-9999）	2018
# %m	月份（01-12）	10
# %d	月内中的一天（0-31）	31
# %H	24小时制小时数（0-23）	14
# %I	12小时制小时数（01-12）	12
# %M	分钟数（00=59）	59
# %S	秒（00-59）	56
# %a	本地简化星期名称	Thu
# %A	本地完整星期名称	Thursday
# %b	本地简化的月份名称	Aug
# %B	本地完整的月份名称	August
# %c	本地相应的日期表示和时间表示	Thu Aug 23 14:55:02 2018
# %j	年内的一天（001-366）	335
# %p	本地A.M.或P.M.的等价符	PM
# %U	一年中的星期数（00-53）星期天为星期的开始	33
# %w	星期（0-6），星期天为星期的开始	4
# %W	一年中的星期数（00-53）星期一为星期的开始	34
# %x	本地相应的日期表示	08/23/18
# %X	本地相应的时间表示	14:55:02
# %Z	当前时区的名称	CDT

# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar

cal = calendar.month(2018, 8)
print ("以下输出2018年8月份的日历:")
print (cal)
