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
player3 = 0
player3wins = 0
player4 = 0
player4wins = 0


def intro():
    global username
    print('The goal of winning the game is by beating the second player by rolling a higher dice number in a total of '
          '5 rounds!\n')
    username = str(input('Hi! What is your name? '))
    print()
    time.sleep(1)
    game_choice = str(input('''Normal Dice Game (normal)
Quad Dice Game (quad)
Quit Program (quit) '''))
    print()
    time.sleep(1)

    if game_choice.lower() == 'n' or game_choice.lower() == 'normal':
        normal()

    elif game_choice.lower() == 'quad' or game_choice.lower() == 'q':
        quads()

    elif game_choice.lower() == 'quit':
        print(colors.green + 'Ending program...\n', colors.reset)
        time.sleep(1)
        quit()

    else:
        print(colors.red + 'Input error found...\n', colors.reset)
        time.sleep(3)
        restart.restart()


def normal():
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
            time.sleep(1)
            print(colors.red + "Player 2 Roll: " + str(player2), colors.reset)
            time.sleep(1)

            if player1 == player2:
                print(colors.yellow + "Draw!\n", colors.reset)

            elif player1 > player2:
                player1wins = player1wins + 1
                print(colors.green + username + " Wins!\n", colors.reset)

            else:
                player2wins = player2wins + 1
                print(colors.red + "Player 2 Wins!\n", colors.reset)

            rounds = rounds + 1
            normal()

        elif user_choice.lower() == 'n' or user_choice.lower() == 'no':
            print(colors.green + 'Thanks for playing!\n', colors.reset)
            time.sleep(2)
            quit()

        else:
            print(colors.red + 'Input error found...\n', colors.reset)
            time.sleep(3)
            restart.restart()

    if rounds >= 5:
        rounds = 1
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
    global rounds, player1, player2, player1wins, player2wins, username, player3, player4, player4wins, player3wins

    user_choice = str(input('Do you wish to roll (yes or no) '))
    print()
    time.sleep(1)

    if rounds <= 5:
        if user_choice.lower() == 'y' or user_choice.lower() == 'yes':
            print("Round " + str(rounds))
            player1 = higher_dice_roll()
            player2 = higher_dice_roll()
            player3 = higher_dice_roll()
            player4 = higher_dice_roll()
            print(colors.green + username + " Roll: " + str(player1), colors.reset)
            time.sleep(.500)
            print(colors.red + "Player 2 Roll: " + str(player2), colors.reset)
            time.sleep(.500)
            print(colors.red + "Player 3 Roll: " + str(player3), colors.reset)
            time.sleep(.500)
            print(colors.red + "Player 4 Roll: " + str(player4), colors.reset)
            time.sleep(.500)

            if player1 > player2 and player1 > player3 and player1 > player4:
                player1wins = player1wins + 1
                print(colors.green + username + " Wins!\n", colors.reset)
            elif player2 > player1 and player2 > player3 and player2 > player4:
                player2wins = player2wins + 1
                print(colors.red + "Player 2 Wins!\n", colors.reset)
            elif player3 > player1 and player3 > player2 and player3 > player4:
                player3wins = player3wins + 1
                print(colors.red + "Player 3 Wins!\n", colors.reset)
            elif player4 > player1 and player4 > player3 and player4 > player2:
                player4wins = player4wins + 1
                print(colors.red + "Player 4 Wins!\n", colors.reset)
            elif player4 == player1 or player4 == player3 or player4 == player2:
                print(colors.yellow + "Draw found!\n", colors.reset)
            elif player1 == player2 or player1 == player3 or player1 == player4:
                print(colors.yellow + "Draw found!\n", colors.reset)
            else:
                print(colors.red + 'Critical scoring error found...\n', colors.reset)
                time.sleep(2)
                restart.restart()
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
        rounds = 1
        if player1wins > player2wins and player1wins > player3wins and player1wins > player4wins:
            print(colors.green + username + " Wins - Rounds Won: " + str(player1wins), colors.reset, '\n')
            time.sleep(2)
            restart.restart()

        elif player2wins > player1wins and player2wins > player3wins and player2wins > player4wins:
            print(colors.red + "Player 2 Wins - Rounds Won: " + str(player2wins), '\n', colors.reset)
            time.sleep(2)
            restart.restart()

        elif player3wins > player1wins and player3wins > player2wins and player3wins > player4wins:
            print(colors.red + "Player 3 Wins - Rounds Won: " + str(player2wins), '\n', colors.reset)
            time.sleep(2)
            restart.restart()

        elif player4wins > player1wins and player4wins > player3wins and player4wins > player2wins:
            print(colors.red + "Player 4 Wins - Rounds Won: " + str(player2wins), '\n', colors.reset)
            time.sleep(2)
            restart.restart()

        elif player1wins == player2wins and player1wins == player3wins and player1wins == player4wins:
            print(colors.yellow + "The game ends with a draw!\n", colors.reset)
            time.sleep(2)
            restart.restart()

        else:
            print(colors.red + 'Critical error found...\n', colors.reset)
            time.sleep(3)
            restart.restart()


intro()
