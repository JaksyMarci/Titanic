import pandas as pd


train = pd.read_csv('train.csv')
print(train.describe())
test = pd.read_csv('test.csv')
print(train.describe())

