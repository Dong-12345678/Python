import pandas as pd

# 用字典创建一个 DataFrame（你可以把它想象成 Excel 表格）
data = {
    'name': ['Alice', 'Bob', 'Cindy', 'David', 'Eva'],
    'city': ['Beijing', 'Shanghai', 'Beijing', 'Shenzhen', 'Beijing'],
    'math_score': [90, 75, 88, 92, 85],
    'english_score': [85, 95, 78, 88, 92]
}

df = pd.DataFrame(data)
print("--- 原始数据 ---")
print(df)

print("\n---前两行---")
print(df.head(2))
print("\n---北京的学生---")
beijing_student=df[df['city']=='Beijing']
print(beijing_student)

df['total_score']=df['math_score']+df['english_score']
print("\n---增加总分列后---")
print(df)

print("\n---各城市的平均数学分---")
city_avg=df.groupby('city')['math_score'].mean()
print(city_avg)

print("\n---数学成绩大于85分的学生")
math_score_high=df[df['math_score']>85]
print(math_score_high)

print("\n---算出每个城市的英语平均分---")
english_avg=df.groupby('city')['english_score'].mean()
print(english_avg)