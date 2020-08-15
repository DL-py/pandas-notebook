"""
如何处理日期和时间：

"""
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
ufo = pd.read_csv('ufo.csv')
print(ufo.head())
# 方法1：
ufo.Time.str.slice(-5, -3).astype(int).head()

# 方法2：转换成pandas的时间的标准格式：datetime64[ns]类型
ufo['Time'] = pd.to_datetime(ufo.Time)
# 这么做的好处：
ufo.Time.dt.hour  # 显示出小时
ufo.Time.dt.minute
ufo.Time.dt.second
ufo.Time.dt.weekday_name  # 自动根据日期显示星期几
ufo.Time.dt.dayofyear  # 自动根据日期显示该天是当年的第几天

# 利用时间进行索引和切片：
time = pd.to_datetime('1991/4/18')

ufo.loc[ufo.Time >= time, :]

ufo.Time.max()  # 找出其中的最大值

# 利用时间进行绘图：
ufo['year'] = ufo.Time.dt.year
ufo.year.value_counts().sort_index().plot()
plt.show()