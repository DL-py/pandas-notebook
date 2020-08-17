import pandas as pd
"""
Dataframe切片操作：
"""
"""
使用loc完成：
*. 基本语法与np的切片操作类似
"""
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

frame.loc[0:2:1, :]  # 第一个参数为行，第二个参数为列
frame.loc[:, 'pop']
frame.loc[[1, 2], 'pop']  # 可以使用[]挑选指定的行或列
# frame.loc[[1, 2], [1]]  # (错)loc中列不能传入columns的序号
"""
使用iloc完成：
*. 基本语法与loc类似，但是只能传入整数，列从0开始编号
"""
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame.iloc[0:1, 0]



















