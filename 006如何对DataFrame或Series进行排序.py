"""
如何对DataFrame和Series进行排序：

"""
import pandas as pd
movies = pd.read_csv('imdb_1000.csv')

# Series排序方式：
movies_title = movies.title.sort_values(ascending=False)
# 会返回一个新的Series,默认是升序，ascending=False表示降序，不会对原数据进行改变

# 对整个DataFram进行排序,同样不会对原数据进行改变；
movies_n = movies.sort_values('title')  # 按照单一的列值排序
movies_n1 = movies.sort_values(['title', 'duration'])  # 按照多个列值排序
print(movies_n1)
