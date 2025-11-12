#fibonacci series
n=9
a,b=0,1
while a<=n:
    print(a)
    a,b=b,a+b



start=int(input("enter start value:"))
end=int(input("enter end value:"))
a,b=0,1
while a<=end:
    if a>start:
        print(a,end=" ")
    a,b=b,a+b
    