# to accept the continuous assessment of the student according to different rubrics defined for Term Work calculation, calculate the final TW marks and display the grade of the student

term={}
while 1:
  ch=int(input("\nTermwork Calculation\n1.Add Assessment\n2.Calculate termwork\n3.Exit\nEnter Choice: "))
  if ch==1:
    while 1:
      a=int(input("1.Add attendance\n2.Others\n3.Exit\nEnter Choice: "))
      if a==1:
        i=int(input("Enter no. of lecture: "))
        j=int(input("Enter no. of lec attended: "))
        k=int(input("Enter marks out of: "))
        c=(j/i)*100
        total=c/100*k
        print("Marks for attendance: ",int(total))
        term["attendance"]=[total]
      if a==2:
        add=input("Name of Assessment: ")
        if add in term:
          j=int(input("Maximum marks: "))
          o=int(input("Scale Down marks: "))
          lst=[]
          term[add]=lst
          c=1
          while(c<=i):
            print("Enter marks of submission ",c)
            k=int(input())
            if k<=j and k>=0:
              term[add].append(k)
              c+=1
            else:
             print("Invalid marks...!\n Kindly Re-enter: ")
        else:
          i=int(input("Total Enter no. of submission: "))
          j=int(input("Maximum marks: "))
          o=int(input("Scale Down marks: "))
          lst=[]
          term[add]=lst
          c=1
          while(c<=i):
            print("Enter marks of submission ",c)
            k=int(input())
            if k<=j and k>=0:
              term[add].append(k)
              c+=1
            else:
             print("Invalid marks...!\n Kindly Re-enter: ")
        l=sum(lst)
        avg=l/len(lst)
        outof=(avg/j)*o
        z=int(outof)
        term[add]=[z]
      if a==3:
        break
  if ch==2:
      final=0
      for m in term:
        final=term[m][0]+final
      print ("Termwork calculation: ",int(final))
      percent=((final)/outof)*100
      if(percent>=90):
        grade = "A"
      elif(percent>=80):
        grade = "B"
      elif(percent>=70):
        grade = "C"
      elif(percent>=60):
        grade = "D"
      elif(percent<60):
        grade = "FAIL"
      print("Grade:",grade)
  if ch==3:
    break
