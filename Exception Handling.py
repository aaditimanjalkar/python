#to perform exception handling using try, except, finally, else, assert and raise
a=[]
while 1:
  ch=int(input("Menu\n1.Add element\n2.search Element\n3.Display list\n4.Exit\nEnter your choice: "))
  if ch==1:
    try:
      x=(input("Enter no. in the array:"))
      y=int(x)
      if y>0:
        a.append(y)
      assert y>0,"your input is not correct"
      print("The number entered : ",y)
    except ValueError as t:
      print(t)
    except AssertionError as obj:
      print(obj)
  elif ch==2:
    try:
      b=int(input("Enter element to be display at postion: "))
      print(a[b-1])
    except IndexError as e:
      print(e)
      c=int(input("Please Enter element to be display at postion which is present in the entred array: "))
      print(a[c-1])
    else:
        print("No exception found..!")    
    finally:
      print("List of Element:",a)
    if b<0:
      raise Exception("Enter a positive integer")
  elif ch==3:
    print("List of Element:",a)
  elif ch==4:
    break  
  else:
     print("Invalid..!")

  
