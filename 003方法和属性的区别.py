"""
属性与方法的区别：
"""
import pandas as pd
movies = pd.read_csv('imdb_1000.csv')  # 用于导入.csv文件
print(movies.describe())  # 获取movies的统计数据如最大值、最小值、平均值等
print(movies.shape)  # 获取DateFrame的数据行列数目
print(movies.dtypes)  # 获取每一列的数据类型
# 属性不需要加入圆括号，而方法需要加入圆括号





