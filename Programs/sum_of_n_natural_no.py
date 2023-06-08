#Sum of first n natural number

n=int(input("Enter range "))

if n < 0:
  print ( "It's a Negative Number")
  print("Enter a positive number")
else:
   sum = 0
   while(n > 0):
       sum += n
       n-= 1
   print("The sum is", sum)
  
  
'''
OUTPUT :-
Enter range 5
The sum is 15

'''
