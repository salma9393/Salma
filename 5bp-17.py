

#print to square of all elements
lis1=[10,20,30]
print(list(map(lambda x:x**2,lis1)))

#program to check if all elements  in the list are greater than 0
lis1=[1,2,3,4,5,-1,0]
print(all(x>0 for x in lis1))

#handling index errors in generators
def gen(d):
  try: yield d[0]; yield d[2];
    except indexerror:print('out of bounds')
    obj-gen([1,2,3])
    print(list(obj))

print(""hello world"")

print(" " " hello world" " ")
