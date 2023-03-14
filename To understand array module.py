# to search an element in 1D Array.

import array as arr 
ar=arr.array('i', [])
while 1:
  ch=int(input("\nMenu\n1.Add element\n2.Display array\n3.search element\n4.Delete element\n5.Exit\nEnter Choice: "))
  if ch==1:
    a=int(input("Enter interger to be added in the array: "))
    ar.append(a)
    

  if ch==2:
    print ("The created array is : ", end =" ") 
    for p in range(0, len(ar)) : 
      print (ar[p], end =" ") 
    print() 


  if ch==3:
    b=int(input("Enter element to be search: "))
    if b in ar:
      print("Element found ")
      print("Postion: ",ar.index(b)+1)
    else:
      print("Element not found")

      
  if ch==4:
    c=int(input("Enter interger to be deleted in the array: "))
    if c in ar:
      ar.remove(c)
      print("Element deleted")
    else:
      print("Element not found")

  if ch==5:
    break
