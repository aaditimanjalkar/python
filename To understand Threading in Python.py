# To achieve thread synchronization using locks when multiple passengers are booking the ticket simultaneously.

from threading import *
from time import *
class Railway:   
    def __init__(self,available):
        self.available=available
        self.l=Lock()
    def reserve(self,wanted):
        self.l.acquire()
        print("Available number of seats are:", self.available)
        if(self.available>=wanted):
            name=current_thread().getName()
            print(wanted,"Seat alloted to",name)
            #sleep(1.5)
            self.available-=wanted
            sleep(1.5)           
        else:
            print("seats are not avaialble")
        self.l.release()
     
available=int(input("Enter available seat: "))   
a=input("Enter your name: ") 
a1=int(input("Enter no. of seats required: "))
b=input("Enter your name: ")   
b1=int(input("Enter no. of seats required: "))
c=input("Enter your name: ")   
c1=int(input("Enter no. of seats required: "))
d=input("Enter your name: ")   
d1=int(input("Enter no. of seats required: "))
e=input("Enter your name: ")   
e1=int(input("Enter no. of seats required: "))
obj=Railway(available)
t1=Thread(target=obj.reserve,args=(a1,))
t2=Thread(target=obj.reserve,args=(b1,))
t3=Thread(target=obj.reserve,args=(c1,))
t4=Thread(target=obj.reserve,args=(d1,))
t5=Thread(target=obj.reserve,args=(e1,))
t1.setName(a)
t2.setName(b)
t2.setName(c)
t2.setName(d)
t2.setName(e)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
