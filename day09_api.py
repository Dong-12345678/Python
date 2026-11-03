import requests
import pandas as pd

url="https://api.open-meteo.com/v1/forecast?latitude=39.90&longitude=116.40&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Shanghai"

print("正在向服务器请求数据")

try:
    response=requests.get(url,timeout=10)
except Exception as e:
    print(f"出错了！网络请求失败:{e}")
    exit()

if response.status_code == 200:
    print("请求成功，正在解析数据")
    raw_data=response.json()
   
   # print(raw_data)

    daily_data = raw_data['daily']

    df=pd.DataFrame({
       'time' : daily_data['time'],
       'max_temp' : daily_data['temperature_2m_max'],
       'min_temp' : daily_data['temperature_2m_min']
   })

    print("\n---抓取到的天气数据---")
    print(df)

    df.to_csv('weather_beijing.csv',index=False,encoding='utf-8-sig')

    print("\n数据已经保存为 weather_beijing.csv")

else:
    print(f"请求失败，状态码：{response.status_code}")
