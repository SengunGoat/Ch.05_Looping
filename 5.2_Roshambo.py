'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record
(---= or ------=)
'''
ties=0
wins=0
loses=0
plays=0
print("Welcoe to Roshambo! The rules are simple, enter 1 for rock, 2 for paper and 3 for scissors.  When you would like to quit and see your final score enter 4")
print()
import random
playing = True
while playing == True:
    comp = random.randint(1,3)
    useans=int(input("Pick either Rock(1),Paper(2) or Scissors(3) or Quit(4)"))
    if useans==4:
        playing == False
        print()
        print("You got", wins, "wins!")
        print()
        print("You got", ties, "ties")
        print()
        print("You got", loses, "loses")
        print()
        print("You played",plays,"times")

    elif useans == 1 and comp == 1:
        print("It's a tie! You both selected rock")
        ties += 1
        plays += 1
    elif useans == 1 and comp == 2:
        print("You lost, The opponent selected paper")
        loses += 1
        plays += 1
    elif useans == 1 and comp == 3:
        print("You won! The opponent selected scissors")
        wins += 1
        plays += 1
    elif useans == 2 and comp == 1:
        print("You won! The opponent selected rock")
        wins += 1
        plays += 1
    elif useans == 2 and comp == 2:
        print("It's a tie! You both selected paper")
        ties += 1
        plays += 1
    elif useans == 2 and comp == 3:
        print("You lost, The opponent selected scissors")
        loses += 1
        plays += 1
    elif useans == 3 and comp == 1:
        print("You lost, The opponent selected rock")
        loses += 1
        plays += 1
    elif useans == 3 and comp == 2:
        print("You won! The opponent selected paper")
        wins += 1
        plays += 1
    else:
        print("It's a tie! You both selected scissors")
        ties += 1
        plays += 1










