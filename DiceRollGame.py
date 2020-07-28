# Created by Jordan Leich on 7/27/2020

# Imports
import random
import time
import colors
import restart

# Globals
rounds = 1
player1 = 0
player1wins = 0
player2 = 0
player2wins = 0


def intro():
    global username
    print('The goal of winning the game is by beating the second player by rolling a higher dice number in a total of '
          '5 rounds!\n')
    username = str(input('Hi! What is your name? '))
    print()
    time.sleep(1)
    game_choice = str(input('''Normal Game (normal)
Quad Dice Game (quad) '''))
    print()
    time.sleep(1)

    if game_choice.lower() == 'n' or game_choice.lower() == 'normal':
        main()

    elif game_choice.lower() == 'q' or game_choice.lower() == 'quad':
        quads()

    else:
        print(colors.red + 'Input error found...\n', colors.reset)
        time.sleep(3)
        restart.restart()


def main():
    global rounds, player1, player2, player1wins, player2wins

    user_choice = str(input('Do you wish to roll (yes or no) '))
    print()
    time.sleep(1)

    if rounds <= 5:
        if user_choice.lower() == 'y' or user_choice.lower() == 'yes':
            print("Round " + str(rounds))
            player1 = dice_roll()
            player2 = dice_roll()
            print(colors.green + username + " Roll: " + str(player1), colors.reset)
            print(colors.red + "Player 2 Roll: " + str(player2), colors.reset)

            if player1 == player2:
                print(colors.yellow + "Draw!\n", colors.reset)
            elif player1 > player2:
                player1wins = player1wins + 1
                print(colors.green + username + " Wins!\n", colors.reset)
            else:
                player2wins = player2wins + 1
                print(colors.red + "Player 2 Wins!\n", colors.reset)
            rounds = rounds + 1
            main()

        elif user_choice.lower() == 'n' or user_choice.lower() == 'no':
            print(colors.green + 'Thanks for playing!\n', colors.reset)
            time.sleep(2)
            quit()

        else:
            print(colors.red + 'Input error found...\n', colors.reset)
            time.sleep(3)
            restart.restart()

    if rounds >= 5:

        if player1wins > player2wins:
            print(colors.green + username + " Wins - Rounds Won: " + str(player1wins), colors.reset, '\n')
            time.sleep(2)
            restart.restart()

        elif player2wins > player1wins:
            print(colors.red + "Player 2 Wins - Rounds Won: " + str(player2wins), '\n', colors.reset)
            time.sleep(2)
            restart.restart()

        elif player1wins == player2wins:
            print(colors.yellow + "The game ends with a draw!\n", colors.reset)
            time.sleep(2)
            restart.restart()

        else:
            print(colors.red + 'Critical error found...\n', colors.reset)
            time.sleep(3)
            restart.restart()


def dice_roll():
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    dice_total = dice_roll1 + dice_roll2
    return dice_total


def higher_dice_roll():
    high_dice_roll1 = random.randint(6, 24)
    high_dice_roll2 = random.randint(6, 24)
    high_dice_total = high_dice_roll1 + high_dice_roll2
    return high_dice_total


def quads():
    global rounds, player1, player2, player1wins, player2wins, username

    user_choice = str(input('Do you wish to roll (yes or no) '))
    print()
    time.sleep(1)

    if rounds <= 5:
        if user_choice.lower() == 'y' or user_choice.lower() == 'yes':
            print("Round " + str(rounds))
            player1 = higher_dice_roll()
            player2 = higher_dice_roll()
            print(colors.green + username + " Roll: " + str(player1), colors.reset)
            print(colors.red + "Player 2 Roll: " + str(player2), colors.reset)

            if player1 == player2:
                print(colors.yellow + "Draw!\n", colors.reset)
            elif player1 > player2:
                player1wins = player1wins + 1
                print(colors.green + username + " Wins!\n", colors.reset)
            else:
                player2wins = player2wins + 1
                print(colors.red + "Player 2 Wins!\n", colors.reset)
            rounds = rounds + 1
            quads()

        elif user_choice.lower() == 'n' or user_choice.lower() == 'no':
            print(colors.green + 'Thanks for playing!\n', colors.reset)
            time.sleep(2)
            quit()

        else:
            print(colors.red + 'Input error found...\n', colors.reset)
            time.sleep(3)
            restart.restart()

    if rounds >= 5:

        if player1wins > player2wins:
            print(colors.green + username + " Wins - Rounds Won: " + str(player1wins), colors.reset, '\n')
            time.sleep(2)
            restart.restart()

        elif player2wins > player1wins:
            print(colors.red + "Player 2 Wins - Rounds Won: " + str(player2wins), '\n', colors.reset)
            time.sleep(2)
            restart.restart()

        elif player1wins == player2wins:
            print(colors.yellow + "The game ends with a draw!\n", colors.reset)
            time.sleep(2)
            restart.restart()

        else:
            print(colors.red + 'Critical error found...\n', colors.reset)
            time.sleep(3)
            restart.restart()


intro()
