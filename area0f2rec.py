class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area(self):
        return self.__length*self.__width
    def __lt__(self,other):
        return self.area() < other.area()
length1=float(input("Enter the length of rectangle1:"))
width1=float(input("Enter the width of Rectangle1:"))
length2=float(input("Enter the length of rectangle2:"))
width2=float(input("Enter the width of Rectangle2:"))
rect1=Rectangle(length1,width1)
rect2=Rectangle(length2,width2)
if rect1 < rect2:
    print("Rectangle 1 has a smaller area than Rectangle2.")
else:
    print("Rectangle 1 has an area greater than or equal to Rectangle2.")