"""
创建DataFrame:

"""
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# 通过字典来创建：
# 生成的DataFrame数据的列表可能不是按字典顺序的，可以通过columns关键字加以指定,同样可以指定
# index的值
DataFrame = pd.DataFrame({'id': [100, 101, 102], 'color': ['red', 'blue', 'green']},
                         index=['a', 'b', 'c'], columns=['id', 'color'])

# 通过列表来创建：
# pandas会默认将相同类型的数据放到一列
DataFrame1 = pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'green']], columns=['id', 'color'])


# 利用numpy中的数组数据来创建：
arr = np.random.rand(4, 2)
DataFrame = pd.DataFrame(arr, columns=['one', 'two'])
print(DataFrame)

# 创建一个Series:
Series = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')
print(Series)

# 将DataFrame与Series连接：
DataFrame = pd.concat([DataFrame1, Series], axis=1)
print(DataFrame)
# Series的name将会变成列名
