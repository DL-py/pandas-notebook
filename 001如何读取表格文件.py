"""
如何读取表格文件：

"""
import pandas as pd
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 1.文件1：
orders = pd.read_table('chipotle.tsv')
# 2.文件2：
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('user.txt', sep='|', header=None, names=user_cols)
# sep='|'可以跳读|;header=None：文本没有标题;names=user_cols读取的文件加入列名
user_head = users.head(10)  # 获取文件的前面10个数据


# 从指定的文件路径读取文件：
# 方法1：
drinks = pd.read_csv('F:/003学习笔记（编程）/002python/002第三方库/003pandas/drinks.csv')
# 方法2：
drinks = pd.read_csv(r'F:\003学习笔记（编程）\002python\002第三方库\003pandas\drinks.csv')


# 如何值读取指定的列：usecols
orders = pd.read_table('chipotle.tsv', usecols=['item_name', 'item_price'])
# 只读前n行
orders = pd.read_table('chipotle.tsv', nrows=3)