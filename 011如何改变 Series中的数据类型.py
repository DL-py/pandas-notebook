"""
如何使用字符串方法：
详细的用法请看：pandas参考手册中 P1232 String handing
"""
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

drinks = pd.read_csv('drinks.csv')
print(drinks.head())

# 1.方法：
drinks['beer_servings'] = drinks.beer_servings.astype(float)
# 2.方法：在读取文件时，定义Series类型
drinks = pd.read_csv('drinks.csv', dtype={'beer_servings': float})

# 3.方法:
orders = pd.read_table('chipotle.tsv')
orders['item_price'] = orders.item_price.str.replace('$', '').astype(float)
print(orders.head())
# 4.方法：用于将bool型的数据转为float
series2 = orders.item_name.str.contains('Chicken').astype(float).head()




