integer=[1,-3,4,-2]
newlist=[x for x in integer if x>0]
print(newlist)

integer=[1,-3,4,-2]
newlist=[x*x for x in integer]
print(newlist)

li=["h","e","l","l","o"]
newlist=[x for x in li if x in "aeiou"]
print(newlist)