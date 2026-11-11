import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

dates=['11-01','11-02','11-03','11-04','11-05','11-06']
max_temps=[15,17,14,10,8,12]
min_temps=[2,4,1,-3,-5,0]

plt.figure(figsize=(8,4))

plt.plot(dates,max_temps,marker='o',label='最高温',color='red')
plt.plot(dates,min_temps,marker='s',label='最低温',color='blue')

plt.title("长春市近6天温度趋势",fontsize=16)
plt.xlabel("日期")
plt.ylabel("温度(摄氏度)")

plt.grid(True,linestyle='--',alpha=0.6)
plt.legend()
plt.show()


df=pd.read_csv('weather_changchun.csv')
df['time']=pd.to_datetime(df['time'])
df['date_str']=df['time'].dt.strftime('%m-%d')

plt.figure(figsize=(10,5))

plt.bar(df['date_str'],df['max_temp'],color='orange',alpha=0.8,label='最高温')
for i in range(len(df)) :
    plt.text(i,df['max_temp'][i]+0.5,str(df['max_temp'][i]),ha='center')

plt.title("长春市未来一周最高温预报",fontsize=16)
plt.xlabel("日期")
plt.ylabel("最高温度")
plt.legend()
plt.show()
