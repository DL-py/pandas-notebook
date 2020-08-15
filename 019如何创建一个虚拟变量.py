"""
如何创建虚拟变量：
创建虚拟变量：对columns中的值进行编码
"""
import pandas as pd
pd.set_option('display.max_columns', None)
train = pd.read_csv('titanic_train.csv')
# 创建虚拟变量的方法：
# 方法1：
train['Sex_male'] = train.Sex.map({'female': 0, 'male': 1})
print(train.head())
# 方法2:将Series创建虚拟变量：
DataFrame = pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:]
# prefix表示在列名加入前缀
train = pd.concat([train, DataFrame], axis=1)
# 将DataFrame创建虚拟变量：
train = pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True)
# drop_first=True可以丢掉冗余的dummies变量
print(train.head())


