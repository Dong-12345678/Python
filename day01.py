#1.温度转换
c=float(input("请输入摄氏度："))
f=c*9/5+32
print(f"对应的华氏度：{f}")

#2.字符串反转
a=input("请输入一段话")
print(f"反转后的结果是：{a[::-1]}")

#3.求平均数
num1=float(input("请输入第一个数："))
num2=float(input("请输入第二个数："))
num3=float(input("请输入第三个数："))
p=(num1+num2+num3)/3
print(f"输入的平均数是：{p}")

#4.判断奇偶
d=int(input("请输入需要判断奇偶的数："))
if d % 2==0:
    print("该数为偶数")
else:
    print("该数为奇数")

#5.简单计算器 输入两个数加一个运算符
numa=float(input("请输入第一个数："))
numb=float(input("请输入第二个数："))
e=input("请输入运算符号：")
if e== "+" :
    g=numa+numb
elif e == "-" :
    g=numa-numb
elif e =="*" :
    g=numa *numb
elif e =="/":
    g=numa / numb
else:
    print("不支持的运算符，请重新输入！")
    g=None
print(f"运算结果是：{g}")

