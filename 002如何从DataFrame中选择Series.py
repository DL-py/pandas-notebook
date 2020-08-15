"""
如何从DataFrame中选择Series

"""
import pandas as pd
import numpy as np
ufo = pd.read_table('ufo.csv', sep=',')
# 方式1：
ufo['City']
ufo['Colors Reported']  # 对于这种有空格的只能使用这种方式
# 当columns名与已有的属性名冲突时，也只能使用这种方式
# 方式2：
ufo.City

# Series可以进行相加
ufo.City + ',' + ufo.State

# 在DataFrame中创建一个新的Series的方法：
# 错误做法：
# ufo.location = ufo.City + ',' + ufo.State
# 正确做法：使用[]
ufo['location'] = ufo.City + ',' + ufo.State
print(ufo.head(10))

# 如何选择出数字类型的列：
drink = pd.read_csv('drinks.csv')
print(drink.select_dtypes(include=[np.number]).dtypes)
