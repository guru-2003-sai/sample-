'''import time 
class I_HUB_APP_STORE:
    def __init__(self):
        print("constructor method")
    def m1(self):
        print("INSTANCE METHOD") 
    @classmethod
    def m2(cls):
        print("CLASS METHOD")
    @staticmethod
    def m3():
        print("STATIC METHOD")           
i1=I_HUB_APP_STORE()
i1.m1()
i1.m2()
i1.m3()
print()   

import time 
class sai:
    def __init__(self):
        print("1st method")
    def m1(self):
        print("2nd method")
    @classmethod
    def m2(cls):
        print("3rd MEthod")
    @staticmethod
    def m3():
        print("4th method")  
i1=sai()
i1.m1()
i1.m2()
i1.m3()
print() 

import time 
class sai:
    def __init__(self,pid,pname,price,company):
        self.pid=int(input("Enter the pid:"))
        self.pname=input("enter the pname:")
        self.price=float(input("enter the price:"))
        self.company=input("enter the company:")
    def m1(self):
        print("=======product details=====")
        print(self.pid," ",self.pname," ",self.price," ",self.company,)
        print()
        
i1=sai()
i1.m1()
print()

defing and declaring and delting and assigng:
================================================
import time 
class sai:
    def __init__(self):
        self.A1=1001
        self.A2=1002
        self.A3=1003
        print(self.A1,self.A2,self.A3)
    def m1(self):
        self.B1=2001
        self.B2=2002
        self.B3=2003
        print(self.B1,self.B2,self.B3)
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=sai()
print(i1.__dict__) 
i1.m1()
print(i1.__dict__)
i1.c1=3001
i1.c2=3002
i1.c3=3003
print(i1.c1,i1.c2,i1.c3)
print(i1.__dict__)


import time 
class sai:
    def __init__(self):
        self.A1=1001
        self.A2=1002
        self.A3=1003
        print(self.A1,self.A2,self.A3)
        del self.A1,self.A2
        self.name="sai"
    def m1(self):
        self.B1=2001
        self.B2=2002
        self.B3=2003
        print(self.B1,self.B2,self.B3)
        del self.B1,self.B3
        self.name="harsha"
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
i1=sai()
print(i1.__dict__) 
i1.m1()
i1.name="sai"
print(i1.__dict__)
i1.c1=3001
i1.c2=3002
i1.c3=3003
print(i1.c1,i1.c2,i1.c3)
del i1.c2,i1.c3
print(i1.__dict__)


sattic mathod:
=============
import time 
class sai:
    pid=1001
    def __init__(self):
        pass
    def m1(self):
        pass
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def __m3():
        pass
i1=sai()
print("pid is:",i1.pid)
print("pid is:",sai.pid)
print()    

assiginment
=============
import math 
class circle:
    def area(r):
        print("enter the radius:",circle.area(r))
        return math.pi*r**2
    print()
print()

import time 
def fibonacci_series(start,end):
    def fib():
        a,b = 0,1
        while a<=end:
            if a>=start:
                yield a
            a,b = b,a+b
    return list(fib())


import time 
import os
try:
    print("Python Developer")
    print()
    
    print() 
    os._exit(True)

   
except:
    print("Angular Developer")
    print()
    
finally:
    print("Full Stack Python Developer")
    print()
    
print()
time.sleep(2)
print("End of an application")

import time 
try:
    print("outer try block")
   
    
    try:
        print("inner try block")
    
    except:
        print("inner Except block")
        print(100//0)
    else:
        print("inner else block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
    
else:
    print("outer else block")
    
finally:
    print("outer finally block")
   
print()
time.sleep(2)
print("End of an aplication")'''

'''for j in range(5,0,-1):
    for i in range(0,j):
        print(j,end="")
    print()'''

# import time 
# f1=open("sai.txt","r")
# print("====File_Details=====")
# print("File_Name is:",f1.name)
# print("File_Mode is:",f1.mode)
# print("File is closed:",f1.closed)
# print("File is readable or not:",f1.readable())
# print("File is writable or not:",f1.writable())
# print()
# f1.close()
# print()
# time.sleep(3)
# print("End of an application")


# file=open('sai1.txt','r')
# f=("sai\ndad\nmom\n")
# file.readlines(f)
# print("file name is",file.name)

# patterns programs:
# ==================
# n=5
# m=1
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print("{:2d}".format(m),end="")
#         m+=1
#     print()

# n=5
# m=2
# for i  in range(1,n+1):
#     for j in range(1,n+1):
#         print("{:2d}".format(m),end="")
#         m+=1
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n,(i*j))
#     print()


# for i in range(1,6):
#     for j in range(1,i,+1):
#         print("*",end="")
#     print()
# for k in range(1,6):
#     for m in range(6,k,-1):
#         print("*",end="")
#     print()

# n=5
# m=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i+j)
#     print()

# for x in range(5,0,-1):
#     for y in range(5,0,-1):
#         print(x,end="")
#     print()


# for x in range(1,6):
#     for y in range(1,6):
#         print(y,end="")
#     print()

# n=5 
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print(str(x+y-1)+"",end="")
#     print()



# n=5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print(str((x+y)%2)+"",end="")
#     print()


# n=5
# for x in range(1,n+1):
#     for y in range(0,n):
#         print(str((x+y)%2)+"",end="")
#     print()


# n=int(input("Enter the number:"))
# if n%2==0:
#     print("even ")
# else:
#     print('odd')

# fact=1
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     fact=fact*i
# print("the factorial of n is",fact)

# factorial using functions:
# ==========================
# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         n=n * fact(n-1)
#         return n
    
# n=int(input("Enter the number:"))
# print("the factorial of the number is ",fact(n))


count=0
n=int(input("Enter the number:"))
for i  in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n," it is a prime number")
else:
    print(n," it is a not prime number")

