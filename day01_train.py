#1
name="DDn"
print(f"Hello,my name is {name}")

#2
age=20
height=1.75
print(f"我今年{age}岁，身高{height}米。")

#3
na=input("请输入你的名字：")
print(f"欢迎{na}来加入Python.")

#4
fruits=["apple","banana","orange"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))
fruits.append("grape")
print(fruits)

#5
student={
    "name":"Tom",
    "age":20,
    "city":"Beijing"
}
print(student.get("name"))
student["score"]=90
print(student)

#6
score=85
if score >90:
    print("A")
elif score >80:
    print("B")
elif score >60:
    print("C")
else : print("D")


#7
for i in range(1,11):
  print(i)

#8
total=0
for i in range(1,101):
    total +=i
print(total)