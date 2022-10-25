#This is the generation paycheck that will gather information, calculate regular and overtime pay, amd calcualte taxes.

import re
import random


print("Welcome to the Generation Paycheck Calculator")

# Requesting the employees name


employname = input("Can you please enter the employee name or press 0:" )

if employname == "0":
    quit()
    

Hours = float(input("Enter the amount of hours you work: " ))
Rate = float(input("Enter Rate of Pay: $"))
OverTime= Hours-40
OverTimeRate = Rate*1.6
OverTimePay = round(OverTimeRate*OverTime, 2)

#Calculatetaxes

def calcfederaltax():
    fedtax = float(GrossPay() *0.15)
    return round (fedtax, 2)

def calcstatetax():
    statetax = float(GrossPay * .10)
    return round(statetax, 2)

def calcfica():
    fica = float(GrossPay() * .02)

while employname:
        Hours = float(input("Enter Hours worked: "))
        Rate = float(input("Enter Rate of Pay: $"))
        if Hours <40:
            GrossPay = round(Rate *Hours, 2)
            print("Employee Name: ", employname)
            print("Gross Pay: $", GrossPay)
            print("Employee Name: ", employname) 
            print("Gross Pay: $", GrossPay)
            print("(OvertimePay: $", OverTimePay,")")
            print("Fedtax:", GrossPay * .15)
            print("Statetax:", GrossPay * .10 )
            print("Fica:", GrossPay * .02 )
            print("Thank you for your time.")
            break
        else:
            RegularPay = Rate*40
            OverTime= Hours-40
            OverTimeRate = Rate*1.6
            OverTimePay = round(OverTimeRate*OverTime, 2)
            GrossPay = round(RegularPay+OverTimePay, 2)
            Fedtax = GrossPay * 0.15
            statetax= GrossPay * 0.10
            fica = GrossPay * .02

            
    



           
