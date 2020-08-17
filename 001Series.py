import pandas as pd
import numpy as np
"""
Series:类似于一维数组
Series = 一组数据（多种类型） + 数据的索引
"""
"""
Series的创建：
pd.Series(对象, index, dtype):用法类似于np.array()
"""
a1 = pd.Series([1, 2, 3, 4])
a2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
a3 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], dtype=np.int32)

# pay attention to the difference of pd and np
b1 = pd.Series({'a': 1, 'b': 2, 'c': 3})  # b1.shape equals to (3, )
b2 = np.array({'a': 1, 'b': 2, 'c': 3})  # b2.shape equals to ()

# 可以重新改变索引的顺序
b3 = pd.Series({'a': 1, 'b': 2, 'c': 3}, index=['b', 'c', 'a'])
"""
Series的属性：
*. values,index,name属性可以通过赋值进行修改
"""
a1 = pd.Series([1, 2, 3, 4])
a1.values  # 获取Series中数据部分，返回narray类型
a1.index  # 获取Series中的索引
a1.shape  # 获得Series的形状(similar to np)
a1.name  # 获得Series的name

"""
Series index
*. Series index is similar to numpy index
"""
'''
basic index
'''
a1 = pd.Series({'a': 1, 'b': 2, 'c': 3})
a1['a']  # index one value
a2[['a', 'b']]  # if index more than 2 values, it should add one more []

'''
bool index
'''
a1 = pd.Series({'a': 1, 'b': 2, 'c': 3})
a1[a1 > 1.5]
# equals to :
bool1 = a1 > 1.5
a1[bool1]

"""
Series运算：
"""
a = pd.Series({'a': 1, 'b': 2, 'c': 3})
b = pd.Series({'b': 1, 'c': 2, 'd': 3})
c = a + b
# result:
# a    NaN
# b    3.0
# c    5.0
# d    NaN
# dtype: float64
