import pandas as pd

df = pd.read_csv('Data/catalog.csv', engine="python")
print(df.head)