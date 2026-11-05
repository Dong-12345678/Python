# 1.定义类（图纸）
class DataFetcher:
    def __init__(self,name,url):
        self.name=name
        self.url=url

    def fetch(self):
        print(f"{self.name}正在向{self.url}发送请求...")
        return f"{self.name}的数据已经抓取完毕"

weather_fetcher=DataFetcher(name="北京天气",url="http://api.weather.com")
stock_fetcher=DataFetcher(name="茅台股票",url="http://api.stock.com")

result1=weather_fetcher.fetch()
print(result1)

result2=stock_fetcher.fetch()
print(result2)