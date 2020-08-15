"""
如何改变显示方法：

"""
import pandas as pd
drinks = pd.read_csv('drinks.csv')
# 获得显示的最大行/列数：
pd.get_option('display.max_rows')
pd.get_option('display.max_columns')
# 设置显示的最大行/列数：
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# None表示显示全部的行/列

# 重置为默认设置：
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


train = pd.read_csv('titanic_train.csv')
pd.set_option('display.max_columns', None)
width = pd.get_option('display.max_colwidth')
# 改变每一列的宽度：
pd.set_option('display.max_colwidth', 500)
# 改变显示的数字中小数的位数：
precision = pd.get_option('display.precision')
pd.set_option('display.precision', 2)
print(precision)
print(train.head())
# 当数字较大时，如何在显示的时候加入逗号：
drinks['x'] = drinks.wine_servings * 1000
drinks['y'] = drinks.total_litres_of_pure_alcohol * 1000
print(drinks.head())
pd.set_option('display.float_format', '{:,}'.format)  # 只有浮点型的格式没有整型
print(drinks.head())
print(pd.describe_option('rows'))  # 显示所有可能的格式
# 重置所有的格式：
pd.reset_option("all")  # 忽略警告
