"""
查看series数据的信息：

"""
import pandas as pd
import matplotlib.pyplot as plt
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
ufo = pd.read_csv('ufo.csv')
ufo.tail()  # 查看文件的最后的5行

# 方法1：
dataframe = ufo.isnull().tail()
dataframe = ufo.notnull().tail()
series = ufo.isnull().sum()  # 显示每一列未缺省的值的个数

# 方法2：
dataframe = ufo.dropna(how='any')  # 丢弃所有的含有NAN的行
dataframe = ufo.dropna(how='all')  # 丢弃全为NAN的行
dataframe = ufo.dropna(subset=['City', 'Shape Reported'], how='any')  # 可以指定某些列

# 方法3：
series = ufo['Shape Reported'].value_counts(dropna=False)

# 方法4：
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
series = ufo['Shape Reported'].value_counts(dropna=False)  # 用特定的值替换NAN


