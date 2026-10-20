student={
    "name" : "Tom",
    "age" :20,
    "city" : "Beijing",
    "score":88

}

for key in student.keys() :
  print(key)

for value in student.values() :
  print(value)

for key,value in student.items() :
 print(f"{key}:{value}")

student["score"]=95
student["grade"]="A"
for key,value in student.items():
  print(f"{key}:{value}")

classroom={
  "student1":{"name":"alice","score":90},
  "student2":{"name":"Bob","score":85}
}

print(classroom["student1"]["name"])
print(classroom["student2"]["score"])