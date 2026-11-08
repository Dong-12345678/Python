import pandas as pd
from sqlalchemy import create_engine

db_url = "postgresql://postgres:你的密码@localhost:5432/learning_sql"

engine = create_engine(db_url)
print("数据库引擎创建成功")

data = {
    'product_id' : [101,102,103],
    'product_name' : ['Laptop','Mouse','Keyboard'],
    'price' : [5999.0,199.5,399.0]
}
df = pd.DataFrame(data)
print("\n---准备写入的Pandas 数据---")
print(df)

#写入数据
df.to_sql(name='products',con=engine,if_exists='replace',index=False)

print("\n---从数据库读取数据---")
query="SELECT *FROM products WHERE price >200"
df_from_db=pd.read_sql(query,con=engine)
print(df_from_db)

engine.dispose()




















