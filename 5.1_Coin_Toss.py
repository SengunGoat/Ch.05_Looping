'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
heads=0
tails=0
false=0
true=0
for i in range(50000):
    for i in range(50):
        onetwo = random.randint(0, 1)
        if onetwo==1:
            heads+=1
        else:
            tails+=1
    print()
    print("You got heads",heads,"times!")
    print("You got tails",tails,"times!")
    heads=0
    tails=0







