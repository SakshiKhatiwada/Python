import pandas as pd

# df = pd.DataFrame([[1,2,3],[4,5,6], [7,8,9]], columns=["A","B","C"])
df = pd.DataFrame([[1,2,3],[4,5,6], [7,8,9]], columns=["A","B","C"], index=['x','y','z'])
#index = rows

print(df.head()) #view the data
print(df.head(2)) #view the data -> first 2 rows

df
df.index
df.index.tolist()

df.info()
df.describe()
df.nunique()
df['A'].unique()

df.shape