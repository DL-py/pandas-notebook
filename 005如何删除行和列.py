"""
如何删除行和列：

"""
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
ufo = pd.read_table('ufo.csv', sep=',')

# 列的删除方法：
print(ufo.head())
ufo.drop('Colors Reported', axis=1, inplace=True)  # axis=1：列
ufo.drop(['State', 'City'], axis=1, inplace=True)  # 删除多个要用[]

# 行的删除方法：
ufo.drop([0, 1], axis=0, inplace=True)  # axis=0:行
print(ufo.head())
