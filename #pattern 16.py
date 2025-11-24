#pattern 16
n=5
for rows in range(1,n+1):
    for cols in range (1,rows+1):
        print(chr(rows+cols+63),end=" ")
    print()