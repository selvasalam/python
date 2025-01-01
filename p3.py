a=[1,2,-5,3,-4,-10]
b=[x for x in a if x>0]
print(b)

a=[1,2,3,4,5]
b=[x*x for x in a]
print(b)

a=input("enter word:")
b=[x for x in a if x in "a,e,i,o,u"]
print(b)

word=input("enter word:")
b=[ord(x)for x in word]
print(b)