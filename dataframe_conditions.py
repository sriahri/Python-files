import pandas as pd

df = pd.DataFrame("xxxxxx")
con1 = df['working-employer'] == 'government'
con2 = df['per-weeks-hours'] > 40
condition = con1 & con2
var = df.loc[condition]
df_local = df
rows = df_local.shape
