"""

"""
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
train = pd.read_csv('titanic_train.csv')
print(train.head())

# apply函数的用法:将函数用于Series或DataFrame的元素中：
# apply用于Series中：
train['Name_Length'] = train.Name.apply(len)

train['Fare_ceil'] = train.Fare.apply(np.ceil)  # ceil表示向上取整

# apply用于DataFrame中：
drinks = pd.read_csv('drinks.csv')
print(drinks.head())
Series = drinks.loc[:, 'beer_servings': 'wine_servings'].apply(max, axis=0)

Series = drinks.loc[:, 'beer_servings': 'wine_servings'].apply(np.argmax, axis=1)
# 找到每一行的最大值所在的列

# applymap:将函数用于DataFrame每一个元素：
DataFrame = drinks.loc[:, 'beer_servings': 'wine_servings'].applymap(float)
