'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
1.) First print the instructions to the screen. Do this with multiple print statements. Don't use one print statement and multiple \n characters to jam everything on one line.
2.) Create a boolean variable called done and set to False.
3.) Create a while loop that will keep looping while not done.
4.) Inside the loop, print out the following:
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.

'''
import random

miletrav=20
drinks=5
enedist=0
thirst=0
narwhalstam=0
done=False
instructionsanswer=str(input("Welcome to the camel game, antartic edition,would you like to hear the instructions?(y/n)"))
if instructionsanswer.lower()=="y":
    print()
    print("The game is simple,you are riding your narwhal to escape the seal population.")
    print()
    print("You can use different commands to direct your narwhal to the end goal,PinguVille.")
    print()
    print("Your goal is to get to PinguVille before the seals catch up to you, luckily you heard about their plans earlier so you already have a 20 mile headstart.")
    print()
    print("Make sure you and your narwhal are ready to continue!")
    print()
else:
    print()
while done==False:
    enemspeed=random.randint(10,15)
    userspeed=random.randint(15,20)
    randthirst=random.randint(1,3)
    narwhalenergy=random.randint(1,3)
    moderandom=random.randint(3,10)
    oasisodds=random.randint(1,15)
    print("1. Drink from your penguins beak")
    print("2.Move ahead at moderate speed")
    print("3.Move ahead at full speed")
    print("4.Take shelter in a igloo for the night")
    print("5.Check status")
    print("6.Quit your journey")
    print()
    answer=int(input("Select one of the actions to continue"))
    if answer==6:
        done==True
        print()
        print("The game has ended and has now restarted")
        print()
    elif answer==5:
        print()
        print("You have traveled",miletrav,"miles!")
        print()
        print("The seals are",miletrav-enedist,"miles away from you!")
        print()
        print("You have",drinks,"drinks left in the beak!")
        print()
        print("You thirst level is",thirst,)
        print()
    elif answer==4:
        narwhalstam==0
        print()
        print("Your Narwhal seems ready to continue the journey!")
        enedist+=enemspeed
        print("The seals moved",enemspeed,"today!")
        print()
    elif answer==3:
        print()
        print("You charge ahead at full speed and gain",userspeed,"miles today!")
        enedist+=enemspeed
        miletrav+=userspeed
        thirst+=randthirst
        narwhalstam+=narwhalenergy
        print()
        print("The seals moved",enemspeed,"today!")
        print()
    elif answer==2:
        print()
        moderandom+=miletrav
        print("You moved forward",moderandom,"today!")
        print()
        enedist+=enemspeed
        thirst+=randthirst
        narwhalstam+=narwhalenergy
        print("The seals moved",enemspeed,"today!")
        print()
    elif answer==1:
        thirst==0
        drinks-=1
        print()
        print("You replenished your thirst!")
        print()
        enedist+=enemspeed
        print("The seals traveled",enemspeed,"today!")
        print()
    elif answer==1 and drinks==0:
        print("You can't do that you have no drinks remaining")
    else:
        print("Error,try to enter a valid action")
    if thirst>=4 and thirst<=6 and answer!=5:
        print("You're very thirsty!")
        print()
    elif thirst>6:
        print()
        print("You died of dehydration so you lost!")
        done==True
    if narwhalstam>5:
        print("Your narwhal is losing it's will to continue")
        print()
    elif narwhalstam>9:
        done==True
        print()
        print("Your narwhal lost all respect for you and left you to die in the middle of no where")
    if miletrav-enedist<20:
        print("The seals are getting close!")
        print()
    if miletrav>=250:
        print()
        print("You won! congrats on making it to the end and surviving the antartic!")
        print()
        done==True
    if oasisodds==1:
        print("You found a nearby town and decided to rest there for the day!")
        print()
        thirst==0
        narwhalstam==0
        drinks==6








