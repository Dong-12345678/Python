import requests
import pandas as pd

#E 抽取数据
def fetch_weather_data():
    """这个函数负责从API拿数据。
    如果成功，返回解析后的DataFrame;
    如果失败，返回None。
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=39.90&longitude=116.40&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Shanghai"
    print("正在向服务器请求数据...")
    try:
        response=requests.get(url,timeout=10)
    except Exception as e:
        print(f"错误：{e}")
        return None
    if response.status_code == 200:
        print("数据请求成功，正在解析数据...")
        raw_data=response.json()
        daily_data=raw_data['daily']
        df=pd.DataFrame(daily_data)
        df=df.rename(columns={
            'time':'time',
            'temperature_2m_max':'max_temp',
            'temperature_2m_min':'min_temp'
        })
        return df
    else:
        print(f"请求失败，状态码:{response.status_code}")
        return None

# T数据转换与业务计算
def transform_data(df):
    """
    这个函数负责对表格进行清洗和计算。
    传入原始df,返回处理后的df。
    """
    if df is None:
        return None
    print("正在对数据进行清洗和计算...")

    # 计算温差
    df['temp_diff']=df['max_temp']-df['min_temp']
    df['time']=pd.to_datetime(df['time'])
    df=df[df['temp_diff']>10]
    return df

#L 数据加载/保存
def save_data(df,filename):
    """
    把处理好的df保存到csv文件
    """
    if df is None:
        print("没有数据可以加载")
        return
    print(f"正在保存数据到{filename}...")
    df.to_csv(filename,index=False,encoding='utf-8-sig')

#执行主流程
if __name__=="__main__":
    print("===数据管道开始运行===")
    raw_df = fetch_weather_data()

    clean_df=transform_data(raw_df)

    if clean_df is not None:
        print("\n===最终处理好的数据===")
        print(clean_df)
        save_data(clean_df,"beijing_weather_cleaned.csv")
    else :
        print("管道终端：数据抓取失败。")
    print("===数据管道运行结束===")




