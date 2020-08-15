"""
SettingWithCopyWarning：
该警告出现的主要在修改时，pandas不知道你要修改的是一个copy还是一个view
"""
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
movies = pd.read_csv("imdb_1000.csv")
print(movies.head())
Series = movies.content_rating[movies.content_rating == 'NOT RATED']
print(movies.content_rating.isnull().sum())
# 可能出现警告的情景1：出现警告而且没有工作
# movies.content_rating[movies.content_rating=='NOT RATED'] = np.nan
# 这句会产生一个警告：SettingWithCopyWarning:
# A value is trying to be set on a copy of a slice from a DataFrame:
# 正确的做法：
movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan
print(movies.content_rating.isnull().sum())
# 可能出现警告的情景2：虽然产生了警告，但是确实工作了
# top_movies = movies[movies.star_rating >=9]
# top_movies.loc[0, 'duration'] = 150
# 解决方法：
top_movies = movies[movies.star_rating >= 9].copy()
top_movies.loc[0, 'duration'] = 150
print(top_movies)



