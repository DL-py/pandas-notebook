"""
查看series数据的信息：

"""
import pandas as pd
import matplotlib.pyplot as plt
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

movies = pd.read_csv('imdb_1000.csv')

# 方法1：利用describe()函数
movies.genre.describe()
# 方法2：
movies.genre.value_counts()
movies.genre.value_counts().plot(kind='bar')
series1 = movies.genre.value_counts(normalize=True)  # normalize表示进行归一化
# 方法3：
series2 = movies.genre.unique()  # 找出没有重复的名字
int1 = movies.genre.nunique()  # 找出没有重复的个数
# 方法4：
Dataframe = pd.crosstab(movies.genre, movies.content_rating)

plt.show()