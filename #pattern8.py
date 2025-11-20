#pattern8
n=5
for rows in range (1,n+1):
    if rows <n:
        for cols in range (1,rows+1):
            print("*",end=" ")
        print()
for rows in range(1,n):
    for cols in range (1,n-rows+1):
        print("*",end=" ")
    print()