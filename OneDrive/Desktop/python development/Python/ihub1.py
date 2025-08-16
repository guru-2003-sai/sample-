'''import time 
S1=set()
print(S1)
print()
print("====Adding the Product_Details=====")
S1.add(1001)
S1.add("Mobile_1")
S1.add(24000)
S1.add("S1")
print(S1)
print()
print(type(S1))
print()
print("====Removing Product_Details=====")
S1.remove(1001)
S1.remove("Mobile_1")
S1.remove(24000)
S1.remove("S1")
print(S1)
print()
print(type(S1))
print()
time.sleep(3)
print('End of an application')

import time 
D1={5:12,1:121,3:1200}.items()
print("Before_Operations:",D1)
print()
D2=sorted(D1)
print("After_Operations:",D2)
print()
D2=sorted(D1,reverse=True)
print("Reverse values are:",D2)
print()
time.sleep(3)
print('End of an application')'''

'''import time
D1={'eid':1001,'ename':"sai",'esal':200000}
print(D1)
print(type(D1))
print("Before the operation:",D1)
D2=D1.get('eid')
print("eid is:",D2)
print("eid is:",D1['eid'])
time.sleep(2)
print("end of an application")

import time 
D1={}
print(D1)
print(type(D1))
print("=====updating values======")
D1.update({'eid':1001,'ename':"sai",'esal':25000})                                                                                                                                         
print(D1)
time.sleep(2)
print('End of an application')

import time 
D1={1:234,70:34,9:1}.values()
print("before the operation:",D1)
D2=sorted(D1)
print("after the operation:",D2)
D2=sorted(D1,reverse=True)
print("reverse keys are:",D2)
print()
time.sleep(2)
print("End of application")

import time 
for x1 in range("core python"):
    print(x1)
print()
time.sleep(2)
print("End of an application")

import time
L1=[11,12,13,14,15,111] 
res1=bytearray(L1)
for X1 in res1:
    print(X1)
print(type(res1))

import time 
S1={'A','B','C','D','E','F'}
S2=frozenset(S1)
print(S2)
print(type(S2))
for X1 in S2:
    print(X1)
print()
time.sleep(2)
print("end of an appication")
    
    
import time 
T1=[100,101,102,103,104,105,102,102]
print(T1)
print(type(T1))
print()
S1={101,102,103,104,105,101,103,102}
print(S1)
print(type(S1))
time.sleep(2)
print('end of an application')


import time 
for X1 in range(0,30,2):
    print("even num",X1)
print()    
for X1 in range(1,30,2):
    print("odd num",X1)
print()        

import time 
for X1 in range(True+False+True+1,True+15+False+1-1,True+2+False):
    print(X1)
print()


import time 
D1=[1,2,3,4,5]
D2=[6,7,8,9,10] 
print("====before merge====") 
print(D1,D2) 
print()
print("=====after merge=====")
print(D1+D2) 
print()
time.sleep(2)
print("End of an application")  


import time 
str1="sai"
str2="hello"
print("===before converting into integer====")
print(str1,str2)
print(type(str1))
print(type(str2))
print("====after converting into integer===")
integer=int(str1)
integer=int(str2)
print(int1,int2)
print(type(int1))
print(type(int2))
time.sleep(2)
print("end of an application")

import time 
Emp_salary=2100
print("Emp_salary is:",Emp_salary)
print("Data type is:",type(Emp_salary))
Emp_salary=None
print("Emp_salary is:",Emp_salary)
print("Data type is:",type(Emp_salary))
Emp_salary=21000,9000
print("Emp_salary is:",Emp_salary)
print("Data type is:",type(Emp_salary))
print()
time.sleep(2)
print("End of an application")

import time 
L1=eval(input("enter the list data:",))
L2=eval(input("Enter the list data:",))
print("===using equqlity operator===")
res1=L1=L2
res2=L1!=L2
print("the result set is:",res1)
print("The data type is:",type(res1))
print("the result set is:",res2)
print("the data type is:",type(res2))
print()
time.sleep(2)
print("End of an application")

import time 
X1=True 
print("The value of X1 is:",X1)
print("The data type is:",type(X1))
X2=not X1
print("the value of X2 is:",X2)
print("The data type is:",type(X2))
print()
time.sleep(2)
print("End of an application") 

print((4&5)|(4^5))  


import time 
L1=[1,2,3,4,5]
L2=[1,2,3,4,5] 
print("====list objects====")
print(L1,L2) 
print("===adressess===")
print(id(L1),id(L2))
print("===using an identity operator====")
print("The result set is:",L1 is L2)
print("The data type is:",type(L1 is L2))
print("The result set is:",L1 is not L2)
print("The data type is:",type(L1 is not L2))
print()
time.sleep(2)
print("End of an application")


print(4&5)
print(4^5)
print(4|5)

X1=[1,2,3,]
print(X1)
print(" data type is:",type(X1))

num=int(2.3)
print("num is:",num)

a=[1,2,3,4]
b=a
c=[1,2,3,4]

print(a is b)
print(a is c)


a=dict(1,2,3,4,5,2,3)
print("before set data type :",a)
print("a is:",type(a))
print(a)

import time 
X1=-22
X2=~X1
print("the value of X1 is:",X1)
print("The value of X2 is:",X2)

import time 
X1=20
X2=X1<<5
print("Before left shift:",X1)
print("After left shift:",X2)

import time 
a=eval(input("Enter the value of a:"))
b=eval(input("Enter the value of b:"))
c=eval(input("Enter the value of c:"))
d=eval(input("Enter the value of d:"))
e=eval(input("Enter the value of e:"))
print("===using chaning operator===")
print(a,b,c,d,e,)
res1=a>b>c>d>e
res2=a>b>c<d<e
res3=a==b==c==d==e
print("The result set is:",res1)
print("The result set is:",res2)
print("The result set is:",res3)
print("The data type is:",type(res1,res2,res3))

import time 
X1=30
X2=bin(30)
print("the value is:",X2)

import time 
X1=0o1234
X2=0O65443
print("The value of X1 is:",X1)
print("The value of X2 is:",X2)

import time 
Y1=20
Y2=Y1>>1
Y3=Y1<<1
print("The right shift opeator is:",Y2)
print("The left shift opeartor is:",Y3)


import time 
S1={X1*X1 for X1 in range (5,11)if X1%2==0}
print(S1)
print(type(S1))  
for X1 in S1:
    print(X1)
print()
time.sleep9m (2)
print("end of an application")


import time 
D1={number:number*number for number in range(5,8)}
print(D1)
print(type(D1))
for X1,X2 in D1.items():
    print(X1,"==",X2)
print()
time.sleep(2)
print("end of an applcation")

import time 
from sys import*
print(argv)
print(type(argv))


import time 
from sys import*
argv=[1,2,3,4,5]
print(argv)
print(type(argv))
print("====using index====")
print(argv[0])
print(argv[1])
print(argv[2])
print(argv[4])
print()
time.sleep(2)
print("end of an application")

import time 
from sys import*
argv=[1,2,3,4,5]
print(argv)
print(type(argv))
print("===using slicing===")
print(argv[1:])
print(argv[2:])
print()
time.sleep(2)
print("end of an application")

import time 
from sys import*
argv=(67,68,69,70,43)
print(argv)
print(type(argv))
print("====+====")
print(argv[1]+argv[2]+argv[3]+argv[4])
print()
time.sleep(2)
print("end of an application")

import time 
from sys import*
argv=[12,13,14,15,16]
print(argv)
print(type(argv))
print("====+====")
print(int(argv[1]+int(argv[2]+int(argv[3]))))
print()
time.sleep(3)
print("end of an application)

import time 
name=input("Enter the language:")
day=int(input("enter the day:"))
month=int(input("enter the month:"))
year=int(input("enter the data:"))
print()
print("===using replacement operator===")
print("Name of the languageis:",name)
print("date of release is{}/{}/{}".format (day,month,year))

import time 
language=input("enter the language:")
if(language=="python"):
    print(language,":meant for general purpose")
print()
time.sleep(2)

import time 
N1=int(input("enter the N1:")) 
N2=int(input("enter the N2:"))
if(N1>=N2):
    print("the largest number is:",N1)
    
import time 
first_name=input("Enter the first_name:")
second_name=input("Enter the second_name:")
third_name=input("Enter the third_name:")
if(first_name=="sai"):
    print("first_name is:",first_name)
    print() 
    if(second_name=="gurudatta"):
        print("second_name is:",second_name) 
        print()
        if(third_name=="guru"):
            print("third_name is:",third_name)
print()
time.sleep(2)
print("end of an application")

import time 
p1=input("enter the password:")
p2=input("enter the conform password:")
if(p1=="ihub123"and p2=="ihub123"):
    print(p1,p2,":valid password")
    print()
else:
    print(p1,p2,":in valid password")    
    print()
time.sleep(2)
print("end of an application")

import time 
n1=int(input("enter the value1:"))
n2=int(input("enter the value2:"))
if(n1>n2):
    ptint("true")
else:
    print("flase")

import time 
str1="Iam sai" 
if(str1[1]=='a'):
    print("correct")
    
import time 
Y1=int(input("enter the year:"))
if(Y1%4==0):
    print("itis a leap year")
    print()
else:
    print("it is not a leap year")
    
import time 
N1=int(input("Enter the number:"))
if(N1%5==0 or N1%11==0):
    print("it is divisible by 5 or 11")
    
else:
    print("it is not divisible by 11")
    
FORMS FOR for LOOPS:
====================    
import time  
for X1 in [101,102,103,104,105]:
    if(X1 %2 ==1):
        print("Odd_numbers:",X1)
        
    
import time
L1=[101,102,103,104,105] 
for X1 in L1:
    if(X1%2==1):
        print("Odd numbers is:",X1)

import time 
L1=[101,102,103,104,105]
for X1 in range(len(L1)):
     if(L1[X1]%2==1):
         print("Odd numbers is:",L1[X1])


SUM OF LIST USING FOR LOOP:
=============================         
import time 
A1=0
for X1 in [121,122,123,124,125,121,123,124]:
    A1=A1+X1
print("Sum of list is:",A1)


import time 
L1=[121,122,123,124,125,121,123,124]
A2=0
for X1 in L1:
    A2=A2+X1
print("Sum of list is:",A2)   
             
 
import time 
L1=[121,122,123,124,125,121,123,124]
A3=0
for X1 in  range(len(L1)):
    A3=A3+L1[X1]
print("Sum of list is:",A3)


REMOVING DUPLICATE VALUES FROM THE LIST: 
=======================================    
import time 
L1=[]
for X1 in [121,122,123,124,125,121,123,124] :
    if(X1 not in L1):
        L1.append(X1)
print("After removing the duplicate elements:",L1)  

import time 
L1=[121,122,123,124,125,121,123,124]
L3=[]
for X1 in L1:
    if(X1 not in L3):
        L3.append(X1)
print("Before deleting:",L1)
print()
print("Ater deleting:",L3)  


import time 
L1=[121,122,123,124,125,121,123,124] 
L3=[]
for X1 in range(len(L1)):
    if(L1[X1] not in L3):
        L3.append(L1[X1])  
print("Before deleting:",L1) 
print("After deleting:",L3)

import time 
L2=[]
for X1 in [10,11,12,13,15,16,91,92,93,94,98,5003,5004,5006]:
    if(X1<20):
        A1=X1+100
        L2.append(A1)
    elif(X1>5000):
        A2=X1+10000
        L2.append(A2)
    elif(X1>20 and X1<5000):
        A3=X1+0 
        L2.append(A3)
print("After operation:",L2) 


import time 
for str1 in "sai":
    print(str1,end=" ")
print()

import time 
str1=" "
for str2 in "sai":
    str1=str2+str1
print("reverse of a string is :",str1)

import time 
L1=['A','B','C','D','E','F']
L2=['a','b','c','d','e','f']
for X1 in L1:
    for X2 in L2:
        print(X1,"-----",X2)
        
import time 
S1=eval(input("Enter the number:"))
for X1 in range (1,11):
    print(S1,"x",X1,"=",S1*X1)
    
    
import time
L1=[34,12,45,21,2]
L2=[]
for X1 in range(len(L1)):
    L2.append(L1[X1])
    L2.sort(reverse=True)
print(L2[0]) 

import time
c1=0 
for str1 in "Data engineer":
    if(str1 in ("AEIOUaeiou")):
        c1+=1
        print("vowels are:",str1) 
print()
print("No.of vowels are:",c1)

import time 
str1=input("Enter the string :")
c2=0
for X1 in str1:
    if(X1 in ("AEIOUaeiou")):
        c2+=1
        print("vowels are:",X1)
print("No.of vowels are:",c2)

import time                
str1=input("Enter the string:")
str2=" "
for X1 in str1:
    str2=X1+str2
print("Reverse of a string:",str2) 
if(str1==str2):
    print(str1,str2,":its a palidrom")   
else:
    print(str1,str2,":its not a palidrom") 
    
    
import time 
n=(eval(input("Enter the no.of rows:")))
for X1 in range(n):
    print("* "*n)          
    
import time 
for X1 in range(4):
    print(X1)
    for X2 in range(4):
        print(X2)   
   

import time 
L1=[1,2,3]
L2=[1,2,3]
for X1 in L1:
    print(X1)
    for X2 in L2:
        print(X2)
        
import time 
L1=[1,2,3]
L2=[1,2,3]
for a1 in L1:
    print(a1)
    for a2 in L2:
        print(a2)
        print(a1,'==',a2)                       
         
import time 
L1=[['a','b','c'],['d','e','f'],['g','h','i']]
print(L1)
for X1 in L1:
    print(X1)
for X2 in X1:
    print(X2)
    
import time 
L1=[['a','b','c'],['d','e','f'],['g','h','i']]
print(L1)
for X1 in L1:
    for X2 in X1:
        print(X2)
           
import time 
L1=[['a','b','c'],['d','e','f'],['g','h','i']]
print(L1)
for X1 in L1:
    for X2 in X1:
        print(X2,end=" ")

import time 
L1=[['a','b','c'],['d','e','f'],['g','h','i']]
print(L1)
for X1 in L1:
    for X2 in X1:
        print(X2,end=" ")        
    print()
print() 

import time 
L1=[1001,1002,1003,1004,1005]
L2=[2001,2002,2003,2004,2005]
print(L1,L2)
print(type(L1),type(L2))
T1=tuple(zip(L1,L2))
print(T1)
print(type(T1))

import time 
L1=[1,2,3,4,5]
print(L1)
print(type(L1))
T1=tuple(zip(L1))
print(T1) 
print(type(T1))

import time 
a=1
while(a<=1):
    print(a)
    
import time 
a=100
while(True):
    print(a)

import time 
L1=[311,312,313,314,315,316]
a=0
while(a<len(L1)):
    print(a)
    a+=1   
        
import time 
L1=[311,312,313,314,315,316]
a=0
while(a<len(L1)):
    print(L1[a])
    a+=1

import time 
L1=[311,312,313,314,315,316]
a=0
while(a<len(L1)):
    if(L1[a]%2==0):
        print(L1[a])      
    a+=1      
    
import time 
L1=[311,312,313,314,315,316]
a=0
s=0
while(a<len(L1)):
    s=s+L1[a]
    a+=1    
print("sum is:",s) 


import time   
number=eval(input("enter the number:"))
a=1
while(a<=10):
    print(number,"X",a,"=",number*a)
    a+=1
print()    

import time 
L1=[311,312,313,314,315,316]
L2=[]
a=0
while(a<len(L1)):
    if(L1[a] not in L2):
        L2.append(L1[a])
    a+=1
print("Before operating:",L1)
print("After operating:",L2) 
       
import time 
str1=input("enter the string:")
str2=""
a=0
while(a<len(str1)):
    str2=str1[a]+str2
    a+=1
if(str2==str1):
    print(str1,str2,":palindrom")
else:
    print(str1,str2,":not palindrom")               
    
    
import time 
for i in range(1,11):
    for j in range(1,11,):
        print(i,"X",j,"=",j*i)
    print()
    
import time 
number=eval(input("enter the number:"))
if(number%2==0):
    print("Even number:")
    break
else:
    print("odd number:")
    
import time 
for x1 in range(15):
    if(x1==11):
        print("welcome to IHUB_STORE")
break
print("the processing values are:",x1)

import time
number=int(input("Enter the number:")) 
for x1 in range (26):
    if(number%2==0):
        print("Even numbers:",x1)
        continue
    print("odd numbers:",x1)
    
import time 
for x1 in range (15):
    if(x1%2==0):
        continue
    else:
        print("odd numbers",x1)    
     
import time 
L1=[1,2,3,4,5,6,150,2500,11,12,13]
for L2 in L1:
    if(L2>150):
        print("Welcometo i hub:")
        continue
    print("the processing values are:")
else:
    print("For with else block:")
    
import time 
for x1 in range(0,7,1):
    print(x1)
    for y1 in range (0,7,1):
        pass
    print()    
        
        
import time 
for x1 in range(0,7,1):
    pass
    for y1 in range (0,7,1):
        print(y1,end=" ")
    print()    

import time 
l1=[1,2,3,4,5]
def double_numbers(l1):
    for num in l1:
        if(num*2):
            print(l1)
    

import time 
def double_numbers(numbers):
    return=[num*2 for num in numbers]
if(__name__=="__main__"):
    print(double_numbers(numbers))
         
       
import time 
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for_in range(2,n+1):
            a,b=b,a+b       

import time 
num=int(input("Enter the number:"))
def Test_case1(num):
    return(num*num)
if(__name__=="__main__"):
    print(Test_case1(num))
    
import time 
for X1 in range (10):
    if(X1==7):
        print("Welcome to ihub:")
        continue
    print("The processing values:")
print()
print("End of an applicatin")

import time
for X1 in range (15):
    if(X1%2==0):
        continue
    print("odd numbers:",X1)
    
import time 
for X1 in range(15):
    if(X1%2==0):
        continue
    else:
        print("Odd numbers:",X1)
        
import time 
str1="data engineer"
c1=0
for X1 in str1:
    if(X1 in ("AEIOUaeiou")):
        print("vowels are:",X1)
        c1+=1
print("numbers of vowels are:",c1) 

import time
for X1 in range( 1,150):
    if(X1%3==0,X1%5==0):
        print("divisibe by 3 and 5:",X1)
        
             
import time 
def Test_case1():
    pass
def Test_case2():
    pass
def Test_case3():
    pass   
def Test_case4():
    pass
if(__name__=="__main__"):
    Test_case1()
    Test_case2()8
    Test_case3()
    Test_case4()
print()
time.sleep(2)'''

# import time 
# def Test_case1(pid= 1001 ,pname="dell",price=29000):
#     print("===product deatails=====")
#     print("pid is:",pid)
#     print("pname is:",pname)
#     print("Price:",price)
# if(__name__=="__main__"):
#     Test_case1(pid=1002,pname="cell",price=30009)
# print()
# time.sleep(2)
# print("End of an application")   
         
            
# def common_letters():
#     str1=input("Enter the string one:")
#     str2=input("Enter the string  two:")
#     s1=set(str1)
#     s2=set(str2)
#     list=s1&s2
#     print(list)
# common_letters()


    # Initial log data
log_data = [
    ("2023-10-26 10:00:00", "INFO", "User logged in"),
    ("2023-10-26 10:01:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:01:30", "INFO", "Data processed successfully"),
    ("2023-10-26 10:02:00", "WARN", "Low disk space"),
    ("2023-10-26 10:03:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:04:00", "INFO", "User logged out"),
    ("2023-10-26 10:05:00", "ERROR", "Null pointer exception"),
    ("2023-10-26 10:05:30", "DEBUG", "Debugging user session"),
]

# Task 1: Filter Error Logs
# error_logs = [entry for entry in log_data if entry[1] == "ERROR"]
# print("1. Error Logs:")
# for log in error_logs:
#     print(log)

# # Task 2: Count Specific Errors
# db_error_count = sum(1 for entry in error_logs if entry[2] == "Database connection failed")
# print("\n2. 'Database connection failed' Count:", db_error_count)

# # Task 3: Find First Warning
# warn_logs = [entry for entry in log_data if entry[1] == "WARN"]
# if warn_logs:
#     timestamp, _, message = warn_logs[0]
#     print("\n3. First WARN log:")
#     print("Timestamp:", timestamp)
#     print("Message:", message)
# else:
#     print("\n3. No WARN log found.")

# # Task 4: Sort Logs by Timestamp
# sorted_logs = sorted(log_data, key=lambda entry: entry[0])
# print("\n4. Logs Sorted by Timestamp:")
# for log in sorted_logs:
#     print(log)

# # Task 5: Check for Critical Issues
# all_short = all(len(entry[2]) < 100 for entry in log_data)
# has_critical = any(entry[1] == "CRITICAL" for entry in log_data)
# print("\n5. Log Message Conditions:")
# print("All messages < 100 characters:", all_short)
# print("Any CRITICAL level logs:", has_critical)

# # Task 6: Append New Log
# new_log = ("2023-10-26 10:06:00", "INFO", "System check complete")
# log_data.append(new_log)
# print("\n6. Appended New Log Entry:")
# print(new_log)

x= 10
y=20
x,y=y,x
print("The value of x",x)
print("The value of y",y)