#pattern 18
n=5
for rows in range (1,n+1):
    for cols in range(1,n+1):
        if (rows+cols)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()