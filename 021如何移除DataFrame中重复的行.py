"""
如何移除DataFrame中重复的行：


"""
import pandas as pd
pd.set_option("display.max_columns", None)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
user = pd.read_table('user.txt', sep='|', header=None, names=user_cols, index_col='user_id')
print(user.head())
# 查看某一列是否有重复的数据：
Series = user.zip_code.duplicated()
# 查看整个DataFrame数据是否有重复的数据：表示整个行都是重复
Series = user.duplicated()
print(user.loc[user.duplicated(keep='last'), :])
# keep='last'，表示保留DataFrame重复数据中的最后的一个
print(user.loc[user.duplicated(keep=False), :])
# keep=False表示重复的数据一个都不保留；


# 移除重复数据的方法：
DataFrame = user.drop_duplicates(keep='first')

# 考虑某即列的值是否重复：
DataFrame = user.duplicated(subset=['age', 'zip_code']).sum()
print(DataFrame)

