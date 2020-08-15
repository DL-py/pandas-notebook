"""
如何使用axis参数：

"""
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

drinks = pd.read_csv('drinks.csv')
# 1.用法1：
print(drinks.head())
print(drinks.drop('continent', axis=1).head())  # 删除列
print(drinks.drop(1, axis=0).head())  # 删除行

# 2.用法2：用于数学运算：
print(drinks.mean())  # 默认是按列进行压缩的即axis=0
print(drinks.mean(axis=1))  # axis=1表示按行压缩
print(drinks.mean(axis='index'))  # 与axis=0等价
print(drinks.mean(axis='columns'))  # 与axis=1等价





