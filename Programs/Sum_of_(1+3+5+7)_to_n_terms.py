#Find sum of following series
#1+3+5+7 upto n terms


#CODE:-

n = int(input("Enter range "))
i = 1
sum = 0

while (i <= 2*n-1):
   sum = sum+i
   i = i+2

print("The sum is", sum)



#OUTPUT :-

Enter range 12
The sum is 144
