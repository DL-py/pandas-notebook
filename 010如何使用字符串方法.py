"""
如何使用字符串方法：
详细的用法请看：pandas参考手册中 P1232 String handing
"""
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
orders = pd.read_table('chipotle.tsv')
print(orders.head())


# 1.列名大写：
item_name = orders.item_name.str.upper()  # 返回一个Series类型的数据

# 2.contain()函数：
bool1 = orders.item_name.str.contains('Chicken')  # 生成bool Series数据

series1 = orders.choice_description.str.replace('[', ' ').str.replace(']', ' ')
# 方法可以进行连接使用
series2 = orders.choice_description.str.replace('[\[\]]', ' ')
print(series2)