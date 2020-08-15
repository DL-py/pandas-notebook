"""
多条件筛选：


"""
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

movies = pd.read_csv('imdb_1000.csv')
print(movies.head(20))
# 方法1：
print(movies[(movies.duration >= 200) & (movies.genre == 'Crime')])
# 这里要用&表示为运算，而不是使用and

# 方法2：这两种形式的功能相似：
print(movies[(movies.genre == 'Crime') | (movies.genre == 'Action')])
print(movies[movies.genre.isin(['Crime', 'Action'])])

