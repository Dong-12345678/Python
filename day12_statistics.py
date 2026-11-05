import pandas as pd
df=pd.read_csv("weather_changchun.csv")
print("---原始数据---")
print(df)

# 提取日期信息，并计算温差
df['time']=pd.to_datetime(df['time'])
df['weekday']=df['time'].dt.day_name()
df['temp_diff']=df['max_temp']-df['min_temp']

#找出最热和最冷的一天
hot=df.sort_values(by='max_temp',ascending=False)
cold=df.sort_values(by='min_temp')

print(f"最热的一天：{hot.iloc[0]['time']}，最高温为 {hot.iloc[0]['max_temp']}")
print(f"最冷的一天：{cold.iloc[0]['time']},最低温度为{cold.iloc[0]['min_temp']}")

#计算3天滚动平均最高温
df['3_day_avg_max']=df['max_temp'].rolling(window=3).mean()

print(df)
print("统计十天基本情况")
print(df.describe())












