#pattern 15
n=5
for rows in range (1,n+1):
    for cols in range(1,rows +1):
        print(chr(rows+64),end=" ")
    print()