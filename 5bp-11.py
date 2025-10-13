
#program to find keys with specific values
a={1:10,'a':20,"c":30,"d":40}
b=[x for x,y in a.items() if y==10]
print(b)

#word frequency counting
a="think champ private limited"
b=a.lower().split()
print(b)
wc={}
for w in b:
  if w in wc:
    wc[w]+=1
  else:
    wc[w]=1
print(wc)

#find union of prime numbrs from two sets
s1={1,2,3,4,4,56,7,89,9}
s2={1,3,47,34,7,89,97,7}
s3=set()
for  x in s1.union(s2):
  if x>1:
    for i in range (2,x):
      if x%i==0:
        break
    else:
      s3.add(x)
print(s3)

#find the missing numbers  in the range  using set  difference
s1={1,3,6,8}
s2=set(range(1,11))
s3=s2.difference(s1)
print(s3)

#union of even numbers  from two sets
s1={1,2,3,4,4,56,7,89,9}
s2={1,3,47,34,7,89,97,7}
s3={x for x in s1.union(s2) if  x%2==0}
print(s3)