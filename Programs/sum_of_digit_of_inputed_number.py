num = int(input("Enter any number "))
i=1
sod=0

while (num != 0):
   rem=num % 10
   sod=sod+rem
   #num=num/10
   num=num//10
print(sod)

#- - - - -  -- - - - - - - - - - - - - 
     
#OUTPUT :-
'''
Enter any number 12456
18
'''
