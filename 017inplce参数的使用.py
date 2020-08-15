"""
inplace的使用：
如果函数中有inplace参数，默认是inplace=Flase, 如果inploce=True将真的对原文件作出操作

"""

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
ufo = pd.read_csv('ufo.csv')
# ufo.drop('City', axis=1, inplace=True)  # inplace=True表示文本的列真的会删除
dataframe = ufo.dropna(how='any')
