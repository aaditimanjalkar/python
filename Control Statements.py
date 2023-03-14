# a menu driven program in python to print Factorial, multiplication table and Fibonacci serie
while True:
 
  o=int(input("Menu\n1.Arithmetic operator\n2.Relational operator\n3.Bitwise operator\n4.Exit\nEnter a choice: "))


  if(o==1):
    a=int(input("Enter a no.:"))
    b=int(input("Enter a no.:"))
    while True:
      c=int(input("Menu\n1.Add\n2.Sub\n3.Multiply\n4.Divide\n5.Integer division\n6.Modulus\n7.Power\n8.Exit\nEnter a choice: "))
      if(c==1):
        print("a+b=",a+b)
      elif(c==2):
        print("a-b=",a-b)
      elif(c==3):
        print("a*b=",a*b)
      elif(c==4):
        print("a/b=",a/b)
      elif(c==5):
        print("Integer division",a//b)
      elif(c==6):
        print("Modulus is ",a%b)
      elif(c==7):
        print("Power is",a**b)
      elif(c==8):
        break
      else:
        print("Invalid Choice ")
  if(o==2):
    while True:
      p=int(input("Menu\n1.Check\n2.Exit"))
      if(p==1):
        a=int(input("Enter a no.:"))
        b=int(input("Enter a no.:"))
        if(a>b):
          print("a is greater")
        elif(a<b):
          print("b is greater ")
        elif(a==b):
          print("a and b are equal")
        elif(a!=b):
          print("a and b are not equal")
      if(p==2):  
        break


  if(o==3):
    a=int(input("Enter a no.:"))
    b=int(input("Enter a no.:"))
    while True:
      c=int(input("Menu\n1.And\n2.Or\n3.Xor\n4.Left shift\n5.Right shift\n6.Exit\nEnter a choice:"))
      if(c==1):
        print("And operation:",a&b)
      elif(c==2):
        print("Or operation",a|b)
      elif(c==3):
        print("Xor operation",a^b)
      elif(c==4):
        print("Left shift",a<<b)
      elif(c==5):
        print("Right shift",a>>b)
      elif(c==6):
        break
      else:
        print("Invalid Choice ")        
  if(o==4):
    break
  else:
    print("Invalid choice")
