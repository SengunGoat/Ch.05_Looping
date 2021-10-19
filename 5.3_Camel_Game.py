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

miletrav=0
drinks=6
enedist=-20
thirst=0
narwhalstam=0
done=False
while done==False:
    enemspeed=random.randint(10,20)
    userspeed=random.randint(13,25)
    randthirst=random.randint(1,3)
    narwhalenergy=random.randint(1,3)
    moderandom=random.randint(3,10)
    oasisodds=random.randint(1,15)
    print("1. Drink from your penguins beak")
    print("2.Move ahead at moderate speed")
    print("3.Move ahead at full speed")
    print("4.Take shelter in a igloo for the night")
    print("5.Check status")
    print("q.Quit your journey")
    print()
    answer=str(input("Select one of the actions to continue the game"))
    if answer.lower()=="q":
        done==True
        print()
        print("The game has ended and has now restarted")
        print()
    elif answer.lower()==5:
        print()
        print("You have traveled",miletrav,"miles!")
        print()
        print("The seals are",enedist,"miles away from you!")
        print()
        print("You have",drinks,"drinks left in the beak!")
        print()
        print("You thirst level is",thirst,)
    elif answer==4:
        narwhalstam==0
        print()
        print("Your Narwhal seems ready to continue the journey!")
        enedist+=enemspeed
        print()
    elif answer==3:
        print()
        print("You charge ahead at full speed and gain",userspeed,"miles today!")

        enemspeed+=enedist
        userspeed+=miletrav
        randthirst+=thirst
        narwhalstam+=narwhalenergy
        print()
        print("The seals moved",enemspeed,"today!")
    elif answer==2:
        print()
        moderandom+=miletrav
        print("You moved forward",moderandom,"today!")
        print()
        enemspeed+=enedist
        thirst+=1
        narwhalstam+=1
        print("The seals moved",enemspeed,"today!")
        print()
    else:
        thirst==0
        print()
        print("You replenished your thirst!")
        print()
        enemspeed+=enedist
        print("The seals traveled",enemspeed,"today!")
    if thirst>=4:
        print("You're very thirsty!")
    elif thirst>6:
        done==True
        print("You died of dehydration so you lost!")
    if narwhalstam>=5:
        print("Your narwhal is losing it's will to continue")
    elif narwhalstam>8:
        done==True
        print("Your narwhal lost all respect for you and left you to die in the middle of no where")
    if miletrav-enedist<20:
        print("The seals are getting close!")
    if miletrav>=250:
        print()
        print("You won! congrats on making it to the end and surviving the antartic!")
        done==True
    if oasisodds==1:
        print("You found a nearby town and decdied to rest there for the day!")
        thirst==0
        narwhalstam==0
        drinks==6









