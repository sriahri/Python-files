import pandas as pd

# read file
# 1)
df = pd.read_csv("titanic_passenger_list.csv")

# 2)
print(df.tail(6))

# 3)
result = df.select_dtypes(include='number')
print(result.describe())


# 5)
df['survived'] = df.survived.astype(str)
df['pclass'] = df.pclass.astype(str)
df['embarked'] = df.embarked.astype(str)
