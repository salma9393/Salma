#pattern17
n=5
for rows in range(1,n+1):
    for spaces in range (1,n-rows+1):
        print(" ",end=" ")
    for cols in range (1,2+rows):
        if cols<=rows:
            print(cols,end=" ")
        else:
            print(2*rows-cols,end=" ")
    print()
    