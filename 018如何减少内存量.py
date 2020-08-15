"""
如何减少内存量：

"""
import pandas as pd
drinks = pd.read_csv('drinks.csv')
# 查看占用的内存大小、类型等信息：
drinks.info()
# 查看真正的内存大小：
drinks.info(memory_usage='deep')
# 查看每一列真正占用内存的大小：
# print(drinks.memory_usage(deep=True))

# 减少内存的方法：将占用内存较大的object类型转换为整数类型的数据进行存储：
# 适用情况：当object对象的值只有几个不同的值时
# 转换后不仅会减少内存量同样会加快运算速度。
drinks['continent'] = drinks.continent.astype('category')
print(drinks.continent.head())
print(drinks.continent.cat.codes.head())  # 查看具体是如何转换的
print(drinks.memory_usage(deep=True))  # 此时continent列占用的内存大大减少

