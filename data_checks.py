import pandas as pd

df = pd.read_csv('data/earthquakes.csv')
#print(df['Date'].head())

df['Formatted_Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False,errors='coerce', utc=True, infer_datetime_format=True)   
df['Year'] = df['Formatted_Date'].dt.year
print(df.dtypes)
