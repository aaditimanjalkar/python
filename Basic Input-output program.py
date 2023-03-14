# a program to display marksheet of student
name=input("Enter name: ")
r=input("Enter Roll no.: ")
print("Enter marks out of 100")
b=int(input("Maths : "))
c=int(input("CN :"))
d=int(input("COA :"))
e=int(input("AT :"))
f=int(input("OS :"))
percent=((b+c+d+e+f)/500)*100
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
print("")
print("Name:",name)
print("Roll No.:",r)
print("Percentage:",percent)
print("Grade:",grade)
