import random

computerlist = ['Rock', 'Paper', 'Scissors']

player = False
computer_score = 0
player_score = 0

while (player == False):
    for i in range(3):
        choice = random.choice(computerlist)

        player = input('Rock, Paper, Scissors? ')
        if player == choice:
            player_score = 0
            computer_score = 0
            print('Tie!')
        elif player == "Rock":
            if choice == "Paper":
                computer_score = computer_score + 1
                print("You lose!", choice, "covers", player)
            else:
                player_score = player_score + 1
                print("You win!", player, "smashes", choice)
        elif player == "Paper":
            if choice == "Scissors":
                computer_score = computer_score + 1
                print("You lose!", choice, "cuts", player)
            else:
                player_score = player_score + 1
                print("You win!", player, "covers", choice)
        elif player == "Scissors":
            if choice == "Rock":
                computer_score = computer_score + 1
                print("You lose!", choice, "smashes", player)
            else:
                player_score = player_score + 1
                print("You win!", player, "cuts", choice)
        else:
            print('Please type a valid input.')

if (player_score > computer_score):
    print('You win! Score:', player_score, 'to', computer_score)
if (computer_score > player_score):
    print('You lose! Score:', player_score, 'to', computer_score)
else:
    print('Tie!')
