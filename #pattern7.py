#pattern7
n=5
for rows in range (1,2*n):
    if rows<=n:
        for cols in range (1,rows+1):
            print("*",end=" ")
    else:
         for cols in range(1,2*n-rows+1):
             print("*",end=" ")
    print()