import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#1.准备数据
#特征 （x):房屋面积（平米）
#标签(y):房屋价格（万元）
data= {
    'area':[50,60,80,100,120,150,200],
    'price':[150,180,240,300,360,450,600]
}
df=pd.DataFrame(data)

X=df[['area']]
y=df['price']

#2.划分训练集和测试集
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#3.创建模型
model=LinearRegression()

#4.训练模型
model.fit(X_train,y_train)

#5.让模型做预测
#比如我们要预测一个110平米的房子能卖多少钱
new_house=pd.DataFrame({'area':[110]})
predicted_price=model.predict(new_house)

print(f"预测结果：一套110平米的房子，预计售价为{predicted_price[0]:.2f}万")

score=model.score(X_test,y_test)
print(f"模型在测试集上的R^2得分为: {score:.2f}")











