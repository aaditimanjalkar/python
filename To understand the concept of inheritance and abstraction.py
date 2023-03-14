# Python program to print area and perimeter of various geometry by inheriting polygon class.
from abc import *
class Polygon:
  @abstractmethod
  def perimeter(self):
    pass
  @abstractmethod
  def area(self):
    pass
class Square(Polygon):
  def perimeter(self,side):
    print("The perimeter of square is: ",4*side)
  def area(self,side):
    print("The area of the square is: ",side*side)
class Rectangle(Polygon):
  def perimeter(self,length,breadth):
    print("The perimeter of rectangle is: ",2*length+2*breadth)
  def area(self,length,breadth):
    print("The area of the rectangle is: ",length*breadth)
class Circle(Polygon):
  def perimeter(self,radius):
    print("The perimeter of circle is: ",2*3.142*radius)
  def area(self,radius):
    print("The area of the square is: ",3.142*radius*radius)
while 1:
  ch=int(input("MENU\n1.Square\n2.Rectangle\n3.Circle\n4.Exit\n"))
  if ch==1:
    side=int(input("Enter the side of the square:"))
    s=Square()
    s.perimeter(side)
    s.area(side)
  elif ch==2:
    length=int(input("Enter the length of the rectangle:"))
    breadth=int(input("Enter the breadth of the rectangle:"))
    r=Rectangle()
    r.perimeter(length,breadth)
    r.area(length,breadth)
  elif ch==3:
    radius=int(input("Enter the radius of the circle:"))
    c=Circle()
    c.perimeter(radius)
    c.area(radius)
  elif ch==4:
    break
  else:
    print("Invalid input!!!")
    
    
#     OR
   
  class Polygon:
    def Area(self):
        print("Area of")
    def Primeter(self):
        print("Primeter of")

class Square(Polygon):
    def Area(self):
        side=float(input("Enter side: "))
        area=side*side
        super().Area()
        print("Square: ",float(area))

    def Primeter(self):
        side=float(input("Enter side: "))
        primeter=4*side
        super().Primeter()
        print("Square: ",float(primeter))

class Rectangle(Polygon):
    def Area(self):
        l=float(input("Enter lenght: "))
        b=float(input("Enter breadth: "))
        area=l*b
        super().Area()
        print("Rectangle: ",float(area))

    def Primeter(self):
        l=float(input("Enter lenght: "))
        b=float(input("Enter breadth: "))
        primeter=2*(l+b)
        super().Area()
        print("Rectangle: ",float(primeter))

class Circle(Polygon):
    def Area(self):
        r=float(input("Enter radius: "))
        area=3.14*r*r
        super().Area()
        print("Circle: ",float(area))

    def Primeter(self):
        l=float(input("Enter radius: "))
        primeter=2*3.24*r
        super().Area()
        print("Circle: ",float(primeter))

while 1:  
  ch=int(input("MENU\n1.Square\n2.Rectangle\n3.Circle\n4.Exit\nEnter a choice: "))
  if ch==1:
   while 1:
    s=Square()
    c=int(input("MENU\n1.Area\n2.Perimeter\n3.Exit\nEnter a choice: "))
    if c==1:
      s.Area()
    elif c==2:
      s.Primeter()
    elif c==3:
      break
  elif ch==2:
   while 1:
    r=Rectangle()
    c=int(input("MENU\n1.Area\n2.Perimeter\n3.Exit\nEnter a choice: "))
    if c==1:
      r.Area()
    elif c==2:
      r.Primeter()
    elif c==3:
      break
  elif ch==3:
   while 1:
    c=Circle()
    c=int(input("MENU\n1.Area\n2.Perimeter\n3.Exit\nEnter a choice: "))
    if c==1:
      c.Area()
    elif c==2:
      c.Primeter()
    elif c==3:
      break
  elif ch==4:
    break
  else:
    print("Invalid choice!!")
