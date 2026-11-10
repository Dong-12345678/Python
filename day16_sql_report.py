import pandas as pd
from sqlalchemy import create_engine

db_url='postgresql://postgres:你的密码@localhost:5432/learning_sql'

engine=create_engine(db_url)

query="SELECT city,time,temp_diff,RANK() OVER (PARTITION BY city ORDER BY temp_diff DESC) FROM weather_data;"

df=pd.read_sql(query,con=engine)

df.to_csv("城市温差排名.csv",index=False,encoding="utf-8-sig")

print("报表已经成功导出！")
engine.dispose()