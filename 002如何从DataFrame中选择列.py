"""
如何从Dataframe获取列?

"""
import pandas as pd
import numpy as np
ufo = pd.read_csv('ufo.csv', sep=',')
'''
*.利用索引获取：
当columns名与已有的属性名冲突时，也只能使用这种方式
'''
ufo['City']
ufo['Colors Reported']  # 对于这种有空格的只能使用这种方式
'''  
*. 利用属性名获取：
'''
ufo.City
# 如何选择出数字类型的列：
drink = pd.read_csv('drinks.csv')
drink.select_dtypes(include=[np.number])

ufo.City + ',' + ufo.State
# Series可以进行相加
# 在DataFrame中创建一个新的Series的方法：
# 错误做法：
# ufo.location = ufo.City + ',' + ufo.State
# 正确做法：使用[]
ufo['location'] = ufo.City + ',' + ufo.State