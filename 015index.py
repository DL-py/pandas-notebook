"""
index:

"""
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
drinks = pd.read_csv('drinks.csv')
#print(drinks.head())
# 查看index
series = drinks.index


# 选择功能：
drinks.loc[23, 'beer_servings']
# 设置新的index
drinks.set_index('country', inplace=True)
# 删除index_name
drinks.index.name = None
# 添加index_name
drinks.index.name = 'country'
# 按照index进行排序
series = drinks.continent.value_counts()
series = series.sort_index()
# 将Series加入dataframe

# 创建series的方法：
people = pd.Series([11000, 5000], index=['Afghanistan', 'Angola'], name='people')
# print(people)
dataframe = pd.concat([drinks, people], axis=1)
# print(dataframe)
