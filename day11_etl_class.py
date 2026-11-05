import requests
import pandas as pd

class Wea:
    def __init__(self,city_name,latitude,longitude):
        self.city_name=city_name
        self.latitude=latitude
        self.longitude=longitude
        self.url=f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Shanghai"

    def extract(self):
        try:
            response=requests.get(self.url,timeout=10)
        except Exception as e:
            print(f"error:{e}")
            return None

        if response.status_code==200:
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
            print(f"error:{response.status_code}")
    def transform(self,df):
        if df is None:
            return None
        
        df['time']=pd.to_datetime(df['time'])
        df['temp_diff']=df['max_temp']-df['min_temp']
        df=df[df['temp_diff']>10]
        return df

    def load(self,df):
        if df is None:
            print("error")
            return None
        df.to_csv(f"{self.city_name}_cleaned.csv",index=False,encoding='utf-8-sig')
        print(f"Data loaded to {self.city_name}_cleaned.csv")

    def run(self):
        df=self.extract()
        df=self.transform(df)
        self.load(df)
        print(f"==={self.city_name} ETL completed===")

if __name__=="__main__":
    beijing=Wea("北京",39.90,116.40)
    beijing.run()

    changchun=Wea("长春",43.88,125.32)
    changchun.run()
    
