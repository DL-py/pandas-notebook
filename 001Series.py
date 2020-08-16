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
"""
Series的属性：
"""
a1 = pd.Series([1, 2, 3, 4])
a1.values  # 获取Series中数据部分，返回narray类型
a1.index  # 获取Series中的索引