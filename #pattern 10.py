#pattern 10
n=5
for rows in range (1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range (1,2*rows):
        print("*",end=" ")  
    print()
for rows in range(1,n):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range (1,2*rows):
        print("*",end=" ")
    print()
for rows in range(1,n-1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range (1,2*rows):
        print("*",end=" ")
    print()
for rows in range(1,n-2):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range (1,2*rows):
        print("*",end=" ")
    print()
for rows in range(1,n-3):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for cols in range (1,2*rows):
        print("*",end=" ")
    print()