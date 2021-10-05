  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
#print("This program takes three numbers and returns the sum.")
#total = 0
#total instead of x
#for i in range(3):
   # x = int(input("Enter a number: "))
    #total+=x
#print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.'''
#for i in range(2,101,2):
    #print(i)





'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
#x=False
#while x==False:
   # for x in range(10,-1,-1):
        #print(x)
     #   x=True
#print("Blast off!")






'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
#import random
#numb=random.randint(1,10)
#print(numb)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
count=0
pos=0
neg=0
zero=0
for i in range(7):
    i=float(input("Pick a number"))
    count+=i
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1
print("Your total is",count,)
print("You had",pos,"positive numbers")
print()
print("You had",neg,"negative numbers")
print()
print("You input",zero,"zeros")
