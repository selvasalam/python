def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=int(input("enter the 1st num:"))
b=int(input("enter the 2nd num:"))
result=gcd(a,b)
print(f"the gcd of{a} and {b} is {result}")