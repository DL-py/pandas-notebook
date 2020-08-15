"""
如何进行分组：

"""
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

drinks = pd.read_csv('drinks.csv')
print(drinks.head())
# 分组进行求平均值：
series1 = drinks.groupby('continent').beer_servings.mean()

# 可以用agg函数来使用多个数学函数：
Dataframe1 = drinks.groupby('continent').beer_servings.agg([max, min])
