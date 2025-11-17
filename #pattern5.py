#pattern5
n=5
for rows in range(1,n+1):
    print("*",end=" ")
    for cols in range (1,n-rows+2):
        print("*",end=" ")
    print()
