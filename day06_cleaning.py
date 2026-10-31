import pandas as pd
df=pd.read_csv('dirty_data.csv')
print(df.info())
print(df.isnull().sum())
df['english_score']=df['english_score'].fillna(df['english_score'].mean())
print(df)
df['city']=df['city'].str.strip()
print(df)
df=df.drop_duplicates()
print(df)
print(df.info())
df=df[df['name'].notna()]
print(df)