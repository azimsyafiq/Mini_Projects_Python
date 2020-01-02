import random

def playGame():

    playerScore = 0
    botScore = 0
    maxScore = 5

    while True:
        choices = ['Rock', 'Paper', 'Scissor']
        botChoice = random.choice(choices)

        playerChoice = input('Choose between Rock, Paper, Scissor: ').capitalize()
        print()

        theChoices = print(f'Player chose {playerChoice}, Computer chose {botChoice}')

        if playerChoice == 'Rock' and botChoice == 'Scissor' or playerChoice == 'Paper' and botChoice == 'Rock' or playerChoice == 'Scissor' and botChoice == 'Paper':
            theChoices
            print('You Win!')
            playerScore += 1

        elif playerChoice == 'Scissor' and botChoice == 'Rock' or playerChoice == 'Rock' and botChoice == 'Paper' or playerChoice == 'Paper' and botChoice == 'Scissor':
            theChoices
            print('You Lose!')
            botScore += 1

        elif playerChoice == botChoice:
            theChoices
            print('Its a draw!')

        elif playerChoice == 'Quit':
            break

        else:
            print('Invalid input')
            print()
            playerChoice = input('Choose between rock, paper, scissor: ').capitalize()

        print(f'Player: {playerScore} - Computer: {botScore}')
        print()

        if playerScore == maxScore or botScore == maxScore:
            if playerScore > botScore:
                print('Player wins!')
                break
            else:
                print('Computer wins!')
                break

playGame()