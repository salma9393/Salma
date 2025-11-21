#square pattern-12
n=5
for rows in range(1,n+1):
    for cols in range (1,n+1):
        if rows==1 or rows==n+1 or cols==1 or cols==n+1:
            print("*",end=" ")
    print() 