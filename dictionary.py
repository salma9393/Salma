
#dictionary
d1={}
print(d1)
print(d1)

d2={"id":101,"name":"ammu"}
print(d2)

d3=dict(id=102,name="bob")
print(d3)
print(type(d3))

#mixed data types
d4={"id":101,"name":"ammu","marks":[10,20,30],"grade":("a","b","c")}
print(d4)
print(type(d4))

#nested dictionaries
d5={
  "student1":{"name":"ammu","age":20}
  }
print(d5)
print(type(d5))

#accessing dictionary items
student = {"name":"salma","age":23,"course":"mca"}
print(student["name"])
print(student["age"])

student = {"name":"salma","age":23,"course":"mca"}
print(student.get("age"))
print(student.get("course"))
print(student.get("course","data not found"))


#changing and adding items
student={"name":"salma","age":23}
student["age"]=24
print(student)
student["course"]:"mba"
print(student)


#removing items
student={"name":"salma","age":23,"course":"mca"}
student.popitem()
print(student)
student.clear()
print(student)


#dictionary operations
marks={"maths":90,"science":65}
print("maths" in marks)
print("english" in marks)
print(len(marks))


#dictionary methods
student = {"name":"salma","age":23,"course":"mca"}
print(student.keys())
print(student.values())
print(student.items())

#update dictionary
student = {"name":"salma","age":23,"course":"mca"}
student.update({"location":"nellore"})
print(student)
student.update({"salary":30000})
print(student)

#copydictionary
copy_student=student.copy()
print(copy_student)


#looping through dictionary
student = {"name":"salma","age":23,"course":"mca"}
for i in student:
  print(i)

student = {"name":"salma","age":23,"course":"mca"}
for v in student.values():
  print(v)

student = {"name":"salma","age":23,"course":"mca"}
for k in student.keys():
  print(k)

student = {"name":"salma","age":23,"course":"mca"}
for k,v in student.items():
  print(k,v)


#dictionary comprehension
squares={x:x*x for x in range(1,6)}
print(squares)
cubes={y:y**3 for y in range(1,10)}
print(cubes)