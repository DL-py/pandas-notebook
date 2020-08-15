"""
如何通过列值来筛选行：


"""
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

movies = pd.read_csv('imdb_1000.csv')

# 例：找到电影长度大于200min的电影：
# 方法1：
is_long = movies.duration > 200  # 产生一个布尔型的Series数据
print(movies[is_long].genre)
# 方法2：
print(movies.loc[movies.duration > 200, 'genre'])
# loc可以选择行和列通过labels

