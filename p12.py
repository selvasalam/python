name=input("Enter the file name:")
if '.' in name:
    extension=name.split('.')
    print(extension[-1])
else:
    print("The file has no extension")