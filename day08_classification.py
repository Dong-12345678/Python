from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

model=DecisionTreeClassifier()

model.fit(X_train,y_train)

predictions=model.predict(X_test)

accuracy=accuracy_score(y_test,predictions)
print(f"决策树模型在测试集上的准确率：{accuracy*100:.2f}%")