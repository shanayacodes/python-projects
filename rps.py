import random

#Valid choices or answers
letters = ['R', 'r', 'P', 'p', 'S', 's']

# Type in your choice
answer = input("Rock, paper or scissors? (R, P or S?) :) ")

# Validate the input
count = len(answer)
if count != 1:
    print ("Invalid answer, give another!")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer not in letters:
    print ("Invalid answer, give another!")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")


# Computer randomly generates its answer
computer = random.choice(['R', 'P', 'S'])
print (computer)

# Compute the winner of each game, or if it's a tie :P
if answer in ('R','r') and computer in ('R'):
    print ("Draw! :P")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('R','r') and computer in ('S'):
    print ("You win! :D")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('R','r') and computer in ('P'):
    print ("You lose :(")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('P','p') and computer in ('R'):
    print ("You win! Yay!")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('P','p') and computer in ('S'):
    print ("I win :P")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('P','p') and computer in ('P'):
    print ("It's a draw!")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('S','s') and computer in ('R'):
    print ("You lost :'(")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('S','s') and computer in ('S'):
    print ("Tie! ;)")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
elif answer in ('S','s') and computer in ('P'):
    print ("Yay, you won!")
    answer = input("Rock, paper or scissors? (R, P or S?) :) ")
