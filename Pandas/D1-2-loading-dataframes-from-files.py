import pandas as pd

#comma separated value file
coffee = pd.read_csv('Pandas/complete-pandas-tutorial/warmup-data/coffee.csv')

print(coffee.head())

results = pd.read_parquet('Pandas/complete-pandas-tutorial/warmup-data/results.parquet') #just a different file type