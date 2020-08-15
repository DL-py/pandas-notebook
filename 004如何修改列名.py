"""
如何修改列名：
"""
import pandas as pd
ufo = pd.read_table('ufo.csv', sep=',')
# 更改colums的名字：
print(ufo.columns)  # 用于显示所有的列的名称
# 方法1：更改部分列名
ufo.rename(columns={'Colors Reported': 'Color_Reported'}, inplace=True)
# 方法2：更改全部列名
cols = ['city', 'color reported', 'shape reported', 'state', 'time']
ufo.columns = cols
# 方法3：在读取文件时更改，columns名
ufo = pd.read_table('ufo.csv', sep=',', names=cols, header=0)
# header=0表示去掉原来的header

# 该改变列名的部分元素：将所有的columns名中' '替换为'_'
ufo.columns = ufo.columns.str.replace(' ', '_')
print(ufo.columns)