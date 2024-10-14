import pandas as pd

df = pd.read_csv("details.csv")
print(df)

print(df.loc[0:2, ['AnnualIncome', 'CreditScore']])
