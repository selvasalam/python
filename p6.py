from itertools import count

names=["Rohan","Sithara","Nayana","Kiara"]
count=0
for i in names:
    for j in i:
        if j=="a":
            count=count++1
            print("occurence of a list:",count)