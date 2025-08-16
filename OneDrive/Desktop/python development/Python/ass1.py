'''import time
str1="Core python"
print(str1)
print()
print(type[str1])
print()
print("=======slice operator with neative direction======")
print()
print(str1[-1:-9:-1])
print(str1[-2:-7:-2])
print(str1[-1:-7:-1])
print(str1[-5:-11:-2])
print(str1[:-2])
print(str1[:-1])
print(str1[:-9])
print(str1[-1:-7])
print(str1[-3:-9])
print(str1[-10:-11:-1])
print(str1[::-1])
print(str1[::-2])
print(str1[-1:-9:0])
print(str1[-7:-11])



merge of dictionarys:
=====================    
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
A1=0
for X1 in [121,122,123,124,124,125,121,123,124]:
    A1=A1+x1
print("Sum of A1 is:",A1) 


max of 3 numbers:
================
import time 
num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
num3=int(input("Enter the value of num3:"))
max_num=num1
if num2>max_num:
    max_num=num2
if num3>max_num:
    max_num=num3
    print("Max number is:",max_num) 
else:
    print(" please enter the valid number:") 
    
Student subject marks::
======================    
import time 
telugu=int(input("enter the marks for telugu:"))     
hindi=int(input("Enter the marks for hindi:"))
english=int(input("Enter the marks for english:"))
chemistry=int(input("Enter the marks for science:")) 
maths=int(input("Enter the marks for maths:"))
physcis=int(input("enter the marks for social:"))
total=telugu+hindi+english+chemistry+maths+physcis
result=total/6
print("The marks for average is:",result)
if result<=34:
    print("The grade is: fail")
elif result<=45:
    print("The grade is: D")
elif result<=55:
    print("The grade is: C")   
elif result<=70:
    print("The grade is: B")     
elif result<=85:
    print("The grade is: A")
elif result<=95:
    print("The grade is: A+")    
else :
    print("The student failed") 
 
 
 
 
product deatls:
===============   
import time 
p1=eval(input("enter the P1:"))
p2=eval(input("enter the p2:"))
p3=eval(input("enter the p3:"))
p4=eval(input("enter the p4:"))
A=p1+p2+p3+p4
print(A)
if(A>=25000):
    print("Added 18% gst is :",A+(18/100)*A)
elif(A<=20000):
    print("Added 12%  gst is:",A+(12/100)*A) 
elif(A<=5000):
    print("Added 3%  gst is:",A+(3/100)*A)
else:
    print("The amount is:",A)       
       
    
     
 
import time 
str2=""
for str1 in "Django":
    str2=str1+str2 
print("Reverse of a string:",str2)
print()
time.sleep(3)
print("End of an application")

 
import time 
L1=[['A','B','C'],['D','E','F'],['G','H','I']]
print(L1)
print()
for x1 in L1:
    for x2 in x1:
        print(x2,end=" ")
    print()
print()
print()
time.sleep(3)
print("End of an application")

import time 
for x1 in range(3):
    print(x1)
    for y1 in range(3):
        print(y1)
print()
time.sleep(3)
print("End of an application")


import time 
L1=[0,1,2]
L2=[0,1,2]
for a1 in L1:
    
    for a2 in L2:
        print(a1,a2)
print()
time.sleep(3)
print("End of an application")


import time 
L1=[['A','B','C'],['D','E','F'],['G','H','I']]
print(L1)
print()
for x1 in L1:
    for x2 in x1:
        print(x2,end=" ")



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
L1=[['a','b','c'],['d','e','f'], ['g','h','i]'] 
a=0
while(a<len(L1)):
    print(L1[a])
    b=0
    while(b<lenL1[a]):
        print(L1[a])
        b+=1
    a+=1    
   
 =====10 mobile numebers using random function=======
 
 import time
from random import*
print("====10 mobile numbers====")
for a in range(1,11):
    print("+91",randint(6000000000,9999999999))

prttern program [MD]
====================
import time 
for i in range(1,5):
    for r in range(5-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for k in range(5,0,-1):
    for l in range(5-k):
        print(end=" ")
    for m in range(k):
        print("*",end=" ") 
    print()  
[MD] PETTERN ABCDEFGHI
====
import time 
L1=[['A','B','C'],['D','E','F'],['G','H','I']]
print(L1)
for i in L1:
    for j in i:
       print(j,end=" ")
    print()
print() 


MAGIC NUMBERS
=============
a=int(input("Enter the number:"))
while a>9:
    b=0
    for x in str(a):
        b+=int(x)
    a=b
if(b==1):
    print("Magic_number")
else:
    print("not magic number")


Length of the digits
====================
import time
num=int(input("Enter the number:"))
count=0
while num>0:
    digit=num%10
    count+=1
    num=num//10
print("Length of the integer is:",count) 


Factorial of a number:
======================
import time 
n=int(input("Enter the number:"))
product=1
for i in range(1,n+1):
    product=product*i
print("factorial of number is ",product)   
'''


# coping one file.
# ==================
# import shutil

# src_path = r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"
# dst_path = r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"

# shutil.copy(src_path, dst_path)
# print("You File is Copied")


# copying all files
# ==================

# import os
# import shutil
# source_folder= r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"
# destination_folder = r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"


# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name

#     # copy only files
#     if os.path.isfile(source):
#         shutil.copy(source, destination)
#         print("You file is copied:", file_name)


# copying files
# =============
# import shutil
# src_folder = r"C:\Users\a\OneDrive\Desktop\python development\python"
# dst_folder = r"C:\Users\a\OneDrive\Desktop\python development\python Notes"


# # File Names
# src_file = src_folder + "\sai.txt"
# dst_file = dst_folder + "\sai.txt"

# shutil.copyfile(src_file, dst_file)
# print('You File is Copied')





# Move Files or Directories in python
# =====================================
# import shutil


# # Absolute path
# src_path = r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"
# dst_path = r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"


# shutil.move(src_path, dst_path)
# print("Your File is Moved successfully")





# # Move files based on filenames:
# =================================

# import glob
# import os
# import shutil
# src_folder = r"C:\Users\a\OneDrive\Desktop\python development\python"
# dst_folder = r"C:\Users\a\OneDrive\Desktop\python development\python Notes"


# # Move file whose name starts with string 'Arun'
# pattern = src_folder + "\arun*"
# for file in glob.iglob(pattern, recursive=True):
#     # Extract file name from file path
#     file_name = os.path.basename(file)
#     shutil.move(file, dst_folder + file_name)
#     print("Files are moved:", file)




# Move all files from directory:
# ===============================
# import os
# import shutil
# source_folder = r"C:\Users\a\OneDrive\Desktop\python development\python"
# destination_folder = r"C:\Users\a\OneDrive\Desktop\python development\python Notes"



# # Fetch all files
# for file_name in os.listdir(source_folder):
#     # Construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name

#     # Move only files
#     if os.path.isfile(source):
#         shutil.move(source, destination)
#         print("Moved:", file_name)



# Move file and Rename:
# =====================
# import os
# import shutil
# src_path = r"C:\Users\a\OneDrive\Desktop\python development\python"
# dst_path = r"C:\Users\a\OneDrive\Desktop\python development\python Notes"


# file_name = 'sales.csv'

# # check if file exist in destination
# if os.path.exists(dst_path + file_name):
#     # split name and extension
#     data = os.path.splitext(file_name)  # file_name = sales.csv
#     only_name = data[0] # sales
#     extension = data[1] # csv

#     # Adding the new name
#     new_base = only_name + "_new" + extension

#     # Construct full file path
#     new_name = os.path.join(dst_path, new_base)

#     # move file
#     shutil.move(src_path + file_name, new_name)
#     print("File Moved Successfully")
# else:
#     shutil.move(src_path + file_name, dst_path + file_name)



# Remove file with relative path:

# import os

# # removing a file with relative path
# os.remove('sai.txt')






# Check if File Exist Before Deleting it:
# =========================================
# import os
# file_path = r"C:\Users\a\OneDrive\Desktop\python development\sai.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("The system cannot find the file specified")



# Delete all Files from a Directory:
# =================================
# import os

# path = r"C:\Users\a\OneDrive\Desktop\python development\python"

# for file_name in os.listdir(path):
#     # construct full file path
#     file = path + file_name
#     if os.path.isfile(file):
#         print("Deleting File:", file)
#         os.remove(file)


# import csv
# import random
# from datetime import datetime


# class HospitalDataSystem:
#     def __init__(self, data_source):  # ✅ Fixed constructor
#         self.data_file = data_source
#         self.records = self._load_records()
#         self.existing_ids = self._collect_existing_ids()
        
#     def _load_records(self):
#         patient_data = {}
#         with open(self.PA2_data_Sp2025.csv, 'r') as file:
#             reader = csv.DictReader(file)
#             reader.fieldnames = reader.fieldnames[1:]  # Skip empty first column if needed
#             for entry in reader:
#                 patient_id = entry['Patient_ID']
#                 if patient_id not in patient_data:
#                     patient_data[patient_id] = []
#                 patient_data[patient_id].append(entry)
#         return patient_data
    
#     def _collect_existing_ids(self):
#         return {
#             'visits': {e['Visit_ID'] for p in self.records.values() for e in p},
#             'notes': {e['Note_ID'] for p in self.records.values() for e in p}
#         }
    
#     def _create_unique_id(self, id_type):
#         while True:
#             new_id = f"{random.randint(100000, 999999):06}"
#             if new_id not in self.existing_ids[id_type]:
#                 self.existing_ids[id_type].add(new_id)
#                 return new_id
    
#     def export_patient_history(self, patient_id, output_path):
#         if patient_id not in self.records:
#             print(f"No records found for patient {patient_id}")
#             return
        
#         with open(output_path, 'w', newline='') as file:
#             writer = csv.DictWriter(file, fieldnames=self.records[patient_id][0].keys())
#             writer.writeheader()
#             writer.writerows(self.records[patient_id])
#         print(f"Records exported to {output_path}")
    
#     def register_new_encounter(self, patient_id):
#         if patient_id not in self.records:
#             print(f"Patient {patient_id} not found in registry")
#             return
        
#         print("\nNew Medical Encounter Registration:")
#         encounter_data = {
#             'Patient_ID': patient_id,
#             'Visit_ID': self._create_unique_id('visits'),
#             'Note_ID': self._create_unique_id('notes'),
#             'Visit_time': self._get_valid_date(),
#             'Visit_department': input("Medical Department: ").strip(),
#             'Race': input("Patient Race: ").strip(),
#             'Gender': input("Patient Gender: ").strip(),
#             'Ethnicity': input("Patient Ethnicity: ").strip(),
#             'Age': self._get_valid_age(),
#             'Zip_code': input("Zip Code: ").strip(),
#             'Insurance': input("Insurance Provider: ").strip(),
#             'Chief_complaint': input("Primary Complaint: ").strip(),
#             'Note_type': input("Clinical Note Type: ").strip()
#         }
        
#         self.records[patient_id].append(encounter_data)
#         self._update_storage()
#         print("New encounter successfully registered")
    
#     def _get_valid_date(self):
#         while True:
#             date_input = input("Encounter Date (YYYY-MM-DD): ").strip()
#             try:
#                 datetime.strptime(date_input, "%Y-%m-%d")
#                 return date_input
#             except ValueError:
#                 print("Invalid date format. Please use YYYY-MM-DD")
    
#     def _get_valid_age(self):
#         while True:
#             try:
#                 return int(input("Patient Age: ").strip())
#             except ValueError:
#                 print("Invalid age. Please enter a whole number")
    
#     def calculate_daily_activity(self, target_date):
#         total = 0
#         for entries in self.records.values():
#             total += sum(1 for e in entries if e['Visit_time'].startswith(target_date))
#         print(f"Total encounters on {target_date}: {total}")
    
#     def _update_storage(self):
#         all_records = [entry for entries in self.records.values() for entry in entries]
#         with open(self.PA2_data_Sp2025.csv, 'w', newline='') as file:
#             writer = csv.DictWriter(file, fieldnames=all_records[0].keys())
#             writer.writeheader()
#             writer.writerows(all_records)

# # -------------------------------
# # Simulated Execution in Script
# # -------------------------------

# # Simulate parameters (you can edit these)
# data_file = 'PA2_data_Sp2025.csv'  # Make sure this CSV file exists
# mode = 'retrieve'                  # Change to 'add' or 'review' to test other features
# patient_id_or_date = '16755'      # Patient ID or date (for review mode)
# output_file = 'output.csv'        # File to write patient history to

# # Create system instance
# system = HospitalDataSystem(data_file)

# # Execute based on simulated mode
# try:
#     if mode == 'retrieve':
#         if not output_file or not patient_id_or_date:
#             raise ValueError("Retrieve mode requires patient ID and output file")
#         system.export_patient_history(patient_id_or_date, output_file)
#     elif mode == 'add':
#         if not patient_id_or_date:
#             raise ValueError("Add mode requires patient ID")
#         system.register_new_encounter(patient_id_or_date)
#     elif mode == 'review':
#         if not patient_id_or_date:
#             raise ValueError("Review mode requires target date")
#         system.calculate_daily_activity(patient_id_or_date)
# except Exception as error:
#     print(f"Operation failed: {error}")



# a1='bike'
# a2='pickup'
# a3='drop'
# a4='tickets'
# if(a1!='bike'):
#     print("it will not Work")
# elif(a2!='pickup'):
#     print("it will not Work")
# elif(a3!='drop'):
#     print("i will  not work")
# elif(a4!='tickets'):
#     print("it will not work")
# else:
#     print("it will work")



# a1='bike'
# a2='pickup'
# a3='drop'
# a4='tickets'
# try:
#     if(a1,a2,a3==True):
#         print("It will work")
# except():
#     print("it will not work")
    





# 1. Creating window
from tkinter import *

root = Tk()


# 7. Creating functions
def employee_Details():
    e_name = name.get()
    Name.set(e_name)
    e_phn = phn_number.get()
    Phn_number.set(e_phn)
    e_dept = dept.get()
    Dept.set(e_dept)
    e_exp = exp.get()
    Exp.set(e_exp)
    e_id = id.get()
    ID.set(e_id)
    e_email = email.get()
    Email.set(e_email)
    e_address_ = address.get()
    Address.set(e_address_)
    e_education = education.get()
    Education.set(e_education)
    # total_yearly_amount=total_amount.get()
    # Total_yearly_amount.set(total_yearly_amount)
    # leaves=total_leaves.get()
    # Total_leaves.set(leaves)
    # paid=total_paid_salary.get()
    # Total_paid_salary.set(paid)
    # pt=total_pt_amount.get()
    # Total_pt_amount.set(pt)

    # Total yearly salary

    jan_salary = float(jan_sal.get())
    J_sal.set(jan_salary)
    feb_salary = float(feb_sal.get())
    F_sal.set(feb_salary)
    mar_salary = float(mar_sal.get())
    M_sal.set(mar_salary)
    april_salary = float(april_sal.get())
    A_sal.set(april_salary)
    may_salary = float(may_sal.get())
    Ma_sal.set(may_salary)
    june_salary = float(june_sal.get())
    June_sal.set(june_salary)
    july_salary = float(july_sal.get())
    Ju_sal.set(july_salary)
    august_salary = float(august_sal.get())
    aug_sal.set(august_salary)
    sept_salary = float(september_sal.get())
    S_sal.set(sept_salary)
    oct_salary = float(october_sal.get())
    O_sal.set(oct_salary)
    nov_salary = float(november_sal.get())
    N_sal.set(nov_salary)
    december_salary = float(december_sal.get())
    D_sal.set(december_sal)

    sum_salary = float(jan_salary + feb_salary + mar_salary + april_salary + may_salary +
                       june_salary + july_salary + august_salary + sept_salary + oct_salary + nov_salary + december_salary)

    Total_yearly_amount.set(sum_salary)


# leaves
# leaves=(int(jan_leaves.get())+int(feb_leaves.get())+int(mar_leaves.get())+int(april_leaves)+
#       int(may_leaves.get())int(june_leaves.get())+int(july_leaves.get())+int(august_leaves.get())+
#       int(september_leaves.get())+int(october_leaves.get())+int(november_leaves.get())+int(december_leaves))
# total_leaves.set(leaves)
# pt


# 2. Creating window size and Tittle
root.title("Employee Record Management")
root.geometry("1500x1500")
Name = StringVar()
Phn_number = StringVar()
Dept = StringVar()
Exp = StringVar()
ID = StringVar()
Email = StringVar()
Address = StringVar()
Education = StringVar()
# employee
Total_yearly_amount = StringVar()
Total_leaves = StringVar()
Total_paid_salary = StringVar()
Total_pt_amount = StringVar()
J_sal = StringVar()
F_sal = StringVar()
M_sal = StringVar()
A_sal = StringVar()
Ma_sal = StringVar()
June_sal = StringVar()
Ju_sal = StringVar()
aug_sal = StringVar()
S_sal = StringVar()
O_sal = StringVar()
N_sal = StringVar()
D_sal = StringVar()

# 3. Creating Window Labels
Label(root, text="Enter Your Employee  Full Name:").place(x=0, y=10)
Label(root, text="Enter Your Employee Phone Number:").place(x=0, y=40)
Label(root, text="Enter Your Employee Department:").place(x=0, y=70)
Label(root, text="Enter Your Employee Experience:").place(x=0, y=100)

Label(root, text="Enter Your Employee ID:").place(x=500, y=10)
Label(root, text="Enter Your Employee Email:").place(x=500, y=40)
Label(root, text="Enter Your Employee Adress:").place(x=500, y=70)
Label(root, text="Enter Your Employee Education:").place(x=500, y=100)
# Employee monthly salary
Label(root, text="Enter Jan  Salary Amount:").place(x=0, y=150)
Label(root, text="Enter Feb Salary Amount:").place(x=0, y=180)
Label(root, text="Enter March Salary Amount:").place(x=0, y=210)
Label(root, text="Enter April Salary Amount :").place(x=0, y=240)
Label(root, text="Enter May Salary Amount:").place(x=0, y=270)
Label(root, text="Enter June  Salary Amount:").place(x=0, y=300)
Label(root, text="Enter July Salary Amount:").place(x=0, y=330)
Label(root, text="Enter August Salary Amount:").place(x=0, y=360)
Label(root, text="Enter September Salary Amount:").place(x=0, y=390)
Label(root, text="Enter October Salary Amount:").place(x=0, y=420)
Label(root, text="Enter November Salary Amount:").place(x=0, y=450)
Label(root, text="Enter December Salary Amount:").place(x=0, y=480)
# Employee leaves
Label(root, text="Enter Jan leaves Amount :").place(x=380, y=150)
Label(root, text="Enter Feb leaves Amount:").place(x=380, y=180)
Label(root, text="Enter March leaves Amount:").place(x=380, y=210)
Label(root, text="Enter April leaves  Amount :").place(x=380, y=240)
Label(root, text="Enter May leaves Amount:").place(x=380, y=270)
Label(root, text="Enter June leaves Amount:").place(x=380, y=300)
Label(root, text="Enter July leaves Amount:").place(x=380, y=330)
Label(root, text="Enter August leaves Amount:").place(x=380, y=360)
Label(root, text="Enter September leaves Amount:").place(x=380, y=390)
Label(root, text="Enter October leaves Amount:").place(x=380, y=420)
Label(root, text="Enter November leaves Amount:").place(x=380, y=450)
Label(root, text="Enter December leaves Amount:").place(x=380, y=480)
# Employee PT amount
Label(root, text="Enter Jan PT Amount :").place(x=760, y=150)
Label(root, text="Enter Feb PT Amount:").place(x=760, y=180)
Label(root, text="Enter March PT Amount:").place(x=760, y=210)
Label(root, text="Enter April PT Amount :").place(x=760, y=240)
Label(root, text="Enter May  PT Amount:").place(x=760, y=270)
Label(root, text="Enter June PT Amount:").place(x=760, y=300)
Label(root, text="Enter July PT Amount:").place(x=760, y=330)
Label(root, text="Enter August PT Amount:").place(x=760, y=360)
Label(root, text="Enter September PT Amount:").place(x=760, y=390)
Label(root, text="Enter October PT Amount:").place(x=760, y=420)
Label(root, text="Enter NovembeR  PT Amount:").place(x=760, y=450)
Label(root, text="Enter December  PT Amount:").place(x=760, y=480)
# paid salary
Label(root, text="Paid Jan Salary:").place(x=1100, y=150)
Label(root, text="Paid Feb Salary:").place(x=1100, y=180)
Label(root, text="Paid Mar Salary:").place(x=1100, y=210)
Label(root, text="Paid Apr Salary:").place(x=1100, y=240)
Label(root, text="Paid May Salary:").place(x=1100, y=270)
Label(root, text="Paid June Salary:").place(x=1100, y=300)
Label(root, text="Paid July Salary:").place(x=1100, y=330)
Label(root, text="Paid August Salary:").place(x=1100, y=360)
Label(root, text="Paid September Salary:").place(x=1100, y=390)
Label(root, text="Paid October Salary:").place(x=1100, y=420)
Label(root, text="Paid November Salary:").place(x=1100, y=450)
Label(root, text="Paid December Salary:").place(x=1100, y=480)

# 4. Creating Text Boxes
name = Entry(root)
name.place(x=200, y=10)
phn_number = Entry(root)
phn_number.place(x=200, y=40)
dept = Entry(root)
dept.place(x=200, y=70)
exp = Entry(root)
exp.place(x=200, y=100)
id = Entry(root)
id.place(x=670, y=10)
email = Entry(root)
email.place(x=670, y=40)
address = Entry(root)
address.place(x=670, y=70)
education = Entry(root)
education.place(x=670, y=100)

# Employee Salary Records
jan_sal = Entry(root)
jan_sal.place(x=180, y=150)
feb_sal = Entry(root)
feb_sal.place(x=180, y=180)
mar_sal = Entry(root)
mar_sal.place(x=180, y=210)
april_sal = Entry(root)
april_sal.place(x=180, y=240)
may_sal = Entry(root)
may_sal.place(x=180, y=270)
june_sal = Entry(root)
june_sal.place(x=180, y=300)
july_sal = Entry(root)
july_sal.place(x=180, y=330)
august_sal = Entry(root)
august_sal.place(x=180, y=360)
september_sal = Entry(root)
september_sal.place(x=180, y=390)
october_sal = Entry(root)
october_sal.place(x=180, y=420)
november_sal = Entry(root)
november_sal.place(x=180, y=450)
december_sal = Entry(root)
december_sal.place(x=180, y=480)
# Monthly leaves
jan_leaves = Entry(root)
jan_leaves.place(x=560, y=150)
feb_leaves = Entry(root)
feb_leaves.place(x=560, y=180)
mar_leaves = Entry(root)
mar_leaves.place(x=560, y=210)
april_leaves = Entry(root)
april_leaves.place(x=560, y=240)
may_leaves = Entry(root)
may_leaves.place(x=560, y=270)
june_leaves = Entry(root)
june_leaves.place(x=560, y=300)
july_leaves = Entry(root)
july_leaves.place(x=560, y=330)
august_leaves = Entry(root)
august_leaves.place(x=560, y=360)
september_leaves = Entry(root)
september_leaves.place(x=560, y=390)
october_leaves = Entry(root)
october_leaves.place(x=560, y=420)
november_leaves = Entry(root)
november_leaves.place(x=560, y=450)
december_leaves = Entry(root)
december_leaves.place(x=560, y=480)
# monthly PT Amount
jan_pt = Entry(root)
jan_pt.place(x=940, y=150)
feb_pt = Entry(root)
feb_pt.place(x=940, y=180)
mar_pt = Entry(root)
mar_pt.place(x=940, y=210)
april_pt = Entry(root)
april_pt.place(x=940, y=240)
may_pt = Entry(root)
may_pt.place(x=940, y=270)
june_pt = Entry(root)
june_pt.place(x=940, y=300)
july_pt = Entry(root)
july_pt.place(x=940, y=330)
august_pt = Entry(root)
august_pt.place(x=940, y=360)
september_pt = Entry(root)
september_pt.place(x=940, y=390)
october_pt = Entry(root)
october_pt.place(x=940, y=420)
november_pt = Entry(root)
november_pt.place(x=940, y=450)
december_pt = Entry(root)
december_pt.place(x=940, y=480)

# 5. Creating a Button for submitting
Button(root, text="Submit", command=employee_Details).place(x=700, y=530)

# 6. Result
Label(root, text="--------------Employee Health Record Management----------- :").place(x=10, y=580)
Label(root, text="Employee Full Name :").place(x=10, y=600)
Label(root, text="", textvariable=Name).place(x=170, y=600)

Label(root, text="Employee ID:").place(x=380, y=600)
Label(root, text="", textvariable=ID).place(x=545, y=600)

Label(root, text="Employee Phone Number:").place(x=760, y=600)
Label(root, text="", textvariable=Phn_number).place(x=930, y=600)

Label(root, text="Employee Email:").place(x=1100, y=600)
Label(root, text="", textvariable=Email).place(x=1250, y=600)

Label(root, text="Employee Department:").place(x=10, y=650)
Label(root, text="", textvariable=Dept).place(x=170, y=650)

Label(root, text="Employee Experience:").place(x=380, y=650)
Label(root, text="", textvariable=Exp).place(x=545, y=650)

Label(root, text="Employee Education:").place(x=760, y=650)
Label(root, text="", textvariable=Education).place(x=930, y=650)

Label(root, text="Employee Address:").place(x=1100, y=650)
Label(root, text="", textvariable=Address).place(x=1250, y=650)

Label(root, text="Total Financial year Amount:").place(x=10, y=750)
Label(root, text="", textvariable=Total_yearly_amount).place(x=200, y=750)

Label(root, text="Total Number of Leaves:").place(x=380, y=750)
# Label(root, text="", textvariable=total_leaves).place(x=580, y=750)

Label(root, text="Total Amount Debited:").place(x=760, y=750)
# Label(root, text="", textvariable=total_pt_amount).place(x=950, y=750)


Label(root, text="Total Paid Salary:").place(x=1100, y=750)
# Label(root, text="", textvariable=total_paid_salary).place(x=1250, y=750)


mainloop()