# to accept two matrices and find their tanspose, addition and product.

from numpy import *
while True:
  ch=int(input("\nMenu\n1.Form matrix\n2.Add\n3.Transpose\n4.Multiply\n5.Exit\nEnter Choice: "))
  if ch==1:
    a=int(input("Enter no of rows: "))
    b=int(input("Enter no of column: "))
    print("Enter element of 1st matrix of", a,"rows", b,"column" )
    matrix=[]
    for i in range(a):
        r = []  
        for j in range(b):  
           r.append(int(input("Enter a element: ")))  
        matrix.append(r)  
    for i in range(a):  
      for j in range(b):  
        print(matrix[i][j], end=" ")  
      print() 

      
    print("Enter element of 2nd matrix", a,"rows", b,"column")
    matrix1=[]
    for i1 in range(a):
        r1 = []  
        for j1 in range(b):  
           r1.append(int(input("Enter a element: ")))  
        matrix1.append(r1)  
    for i1 in range(a):  
      for j1 in range(b):  
        print(matrix1[i1][j1], end=" ")  
      print()


  if ch==2:
    print("Addition of matrix :")
    m=add(matrix,matrix1)
    for i in range(a):  
      for j in range(b):
        print(m[i][j], end=" ")  
      print()


  if ch==3:
    print("Transpose of 1st matrix:")
    m=[]
    for i in range(a): 
      for j in range(b):  
        print(matrix[j][i], end=" ")  
      print()
    print("Transpose of 2nd matrix:")  
    for i1 in range(a):  
      for j1 in range(b):  
        print(matrix1[j1][i1], end=" ")  
      print()

      
  if ch==4:
    print("Multiplication of matrix :")
    m1=multiply(matrix,matrix1)
    for i in range(a):  
      for j in range(b):
        print(m1[i][j], end=" ")  
      print()

  
  if ch==5:
    break
