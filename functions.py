
#functions
def greet():
  print("hello world")
greet()

def add(a,b):
  return a*b
print(add(2,3))

#built in functions
#len()
f="hello world"
print(len(f))

#max()
s=[9,8,7,6,5,43,2,3]
print(max(s))

#min()
a=(1,3,5,6,7,9,8)
print(min(a))

b=[2,3,4,5,6,7,8]
print(sum(b))

#user defined functions
#positional arguments
def greet(name,age):
  print(f"hello my name is{name},and my age is{age}")
greet("ammu",22)

#keyword arguments
def greet(name, age):
  print(f"hello my name is{name},my age is {age}")
greet(name="ammu",age="20")

#default arguments
def greet(name,age=23):
  print(f"hello my name is {name} and my age is{age}")
greet("ammu")

#default arguments
def greet(name="ammu",age=23):
  print(f"hello my name is{name}my age is{age}")
greet("lucky",25)

#arbitary arguments
def my_sum(*args):
  return sum(args)
print(my_sum(1,2,3,4,5))

#arbitary arguments
def maxi(*args):
  return max(args)
print(maxi(3,4,5,6,7,67))

#arbitary keyword arguments
def student (**kwargs):
  for key,value in kwargs.items():
    print(key,":",value)
student (name="ammu",age=22,course='mca')

def student1(**kwargs):
  for i in kwargs.items():
    print(i)
student1(name="salma",age=23,course="mca")

#return system
def square(x):
  return x**2
print(square(5))