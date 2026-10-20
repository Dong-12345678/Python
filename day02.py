#1
nums=[10,20,30,40,50,60,70,80,90,100]
print(nums[:3])
print(nums[-3:])
print(nums[::2])
print(nums[::-1])

#2
my_list=[]
my_list.append("苹果")
my_list.append("香蕉")
my_list.append("水蜜桃")
my_list.insert(0,"西瓜")
my_list.remove("香蕉")
print(len(my_list))
print(my_list)

#3
total=0
scores = [88, 92, 75, 60, 95, 81]
for x in range(0,6) :
 total += scores[x]

averge=total/6
print(averge)

high_scores=[]
for x in range(0,6) :
 if scores[x] >90 :
  high_scores.append(scores[x])

print(high_scores)

#4
evens=[y for y in range(1,21)  if y %2 ==0]
print(evens)
