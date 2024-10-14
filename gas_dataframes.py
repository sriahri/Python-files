import pandas as pd
dataframe_1 = pd.read_csv('dataSensor1.txt')
dataframe_2 = pd.read_csv('dataSensor2.txt')
print(dataframe_1)
print(dataframe_2)
dataframe_3 = pd.concat(dataframe_1, dataframe_2)
print(dataframe_3)