#Calculate the Gross Salary of an employee for following allowance & deduction.

''' Get Basic Salary of Employee,
DA = 25% of Basic,
HRA = 15% of Basic,
PF = 12% of Basic,
TA = 7.50% of Basic.
Net Pay = Basic + DA + HRA + TA
Gross Pay = Net Pay - PF.
'''


CODE :-

print("SALARY PROGRAM")
name= str(input("Enter name of employee:"))
basic=float(input("Enter Basic Salary :"))
da=float(basic*0.25)
hra=float(basic*0.15)
pf=float((basic+da)*0.12)
ta=float(basic*0.075)
netpay=float(basic+da+hra+ta)
grosspay=float(netpay-pf)

print()
print()
print("S A L A R Y D E T A I L E D B R E A K U P ")
print("==============================================")
print(" NAME OF EMPLOYEE : ",name)
print(" BASIC SALARY : ",basic)
print(" DEARNESS ALLOW. : ",da)
print(" HOUSE RENT ALLOW.: ",hra)
print(" TRAVEL ALLOW. : ",ta)
print("==============================================")
print(" NET SALARY PAY : ",netpay)
print(" PROVIDENT FUND : ",pf)
print("==============================================")
print(" GROSS PAYMENT : ",grosspay)
print("==============================================")




OUTPUT :-

SALARY PROGRAM
Enter name of employee:Pankaj Lohani
Enter Basic Salary :25000



S A L A R Y D E T A I L E D B R E A K U P 
==============================================
 NAME OF EMPLOYEE :  Pankaj Lohani
 BASIC SALARY :  25000.0
 DEARNESS ALLOW. :  6250.0
 HOUSE RENT ALLOW.:  3750.0
 TRAVEL ALLOW. :  1875.0
==============================================
 NET SALARY PAY :  36875.0
 PROVIDENT FUND :  3750.0
==============================================
 GROSS PAYMENT :  33125.0
==============================================
