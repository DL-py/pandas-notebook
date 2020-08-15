"""
如何选择行和列：

"""

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
ufo = pd.read_csv('ufo.csv')

# loc: 按label进行选择
# 方法1：选择单行/列
series = ufo.loc[0, :]  # ：表示1全选
series = ufo.loc[:, 'City']
series = ufo.loc[ufo.City =='Oakland', 'State']

# 方法2：选择多行
dataFrame = ufo.loc[[0, 1, 2], :]
dataframe = ufo.loc[0:2, :]  # 起始和终止都会包含
dataframe = ufo.loc[:, ['City', 'State']]
dataframe = ufo.loc[:, 'City':'State']


# iloc:按照整数的位置进行选择
dataframe = ufo.iloc[:, [0, 3]]
dataframe = ufo.iloc[:, 0:4]  # 与loc不同，iloc不包含终止值


