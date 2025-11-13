#else after loops
for i in range(10):
    print(i)
else:
    print("executed successfully")



fruits=["mango","apple","grapes","banana"]
search="guava"
for i in fruits:
    if i==search:
        print("search found",search)
        break
else:
    print("search not found")



num=[1,3,5,7,8,7,8,9,4,6]
for i in num:
    if i%2==0:
        print("all are even numbers")
        break
else:
    print("all are odd numbers")



n=[1,3,5,7,8,7,8,9,4,6]
for i in n:
    if i%2==1:
        print("all odd numbers")
        break
else:
    print("all are even numbers")







