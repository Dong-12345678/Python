import pandas as pd
df_info=pd.read_csv('students_info.csv')
df_score=pd.read_csv('scores_data.csv')
df1=pd.merge(df_info,df_score,on='id',how='inner')
print(df1)
df2=pd.merge(df_info,df_score,on='id',how='left')
print(df2)
df=df2.dropna()
print(df)