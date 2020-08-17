"""
Dataframe:表格型的数据结构

"""
"""
Dataframe的创建：
*. 一般是通过字典来进行创建
"""
import pandas as pd
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
# 指定列的顺序:
frame = pd.DataFrame(data, columns=['year', 'state', 'pop'])
# *.传入的列在数据中找不到，就会用NAN替代

frame = pd.DataFrame(data, columns=['year', 'state', 'pop'], dtype='object')

"""
Dataframe的方法：

"""
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame.head(3)  # 选取前3行，默认是5行
frame.describe()  # 获取统计信息

"""
Dataframe的属性：
"""
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame.dtypes  # Dataframe中每个Series元素的属性
frame.shape   # 获取Dataframe的形状
