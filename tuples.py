#creating tuple
t1=()
print(t1)
print(type(t1))

t2=(1,2,3,4,5)
print(t2)
t3=(1,2,"hello",'ammu',3.14,True)
print(t3)
print(type(t3))

t4=1,"apple",3.14
print(t4)

t5=(1,(2,3),(4,5,6))
print(t5)
print(type(t5))

t6=(10,)
t7=("ammu",)
print(t6)
print(t7)
print(type(t6))
print(type(t7))

#accessing elements
colours=("red","blue","black","green")
print(colours[0])
print(colours[-1])
print(colours[1:3])
print(colours[:])
print(colours[1:])

t=(1,2,3,[2,3,4],7,8)
print(t)
print(type(t))
t[3][1]=9
print(t)

#tuple operations
#concatenation
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
#multiple
print(t1*3)
print(t2*4)

#membership
t4=(1,2,3,4,5,6,7,8)
print(2 in t4)
print(9 not in t4)
print(3 not in t4)

#built in functions
t=(1,2,3,4,5,6,7,8,1,2)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(t.index(2))
print(t.count(2))

def calc(a,b):
  return(a+b,a-b,a*b)
result=calc(2,5)
print(result)