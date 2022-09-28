from random import randint

game = True
while game:
    opening_string = 'THE PYTHON GAME: ROCK PAPER SCISSORS'
    print(opening_string.center(130, '=') + '\n\n')
    print('Hi folks, if want to play, choose your weapon please \n\n   Just type the first letter or the whole word: ')

    options = ['rock', 'paper', 'scissors']
    rock_list = ['rock', 'r']
    paper_list = ['paper', 'p']
    scissors_list = ['scissors', 's']
    player_choice = str(input())
    player_choice = player_choice.lower()
    if player_choice in rock_list:
        player_choice = options[0]
        print('You choose ' + player_choice.upper())
    if player_choice in paper_list:
        print('PAPER is your weapon')
        player_choice = options[1]
    if player_choice in scissors_list:
        print('You picked SCISSORS')
        player_choice = options[2]
    if player_choice not in ['rock', 'r', 'paper', 'p', 'scissors', 's']:
        print('>>>>>>>>>>>>>>>>   To play this game, you have to choose between these three: ROCK PAPER Scissors   <<<<<<<<<<<<<' + '\n')
        continue

    
    sentences = ['and some crazy computer picked: ', 'and the computer choice is: ', 'and the machine believes in: ', 'and CPU random choice is: ']
    computer_choice = options[randint(0,2)]
    sentence_choice = sentences[randint(0,3)]
    print(sentence_choice + computer_choice.upper() + ', so\n')
    computer_choice = computer_choice.lower()


    if computer_choice == player_choice:
        print('DRAW')

    elif player_choice in rock_list and computer_choice in scissors_list:
        print('ROCK beats the scissors')
    elif player_choice in scissors_list and computer_choice in paper_list:
        print('SCISSORS cut the paper and YOU WIN')
    elif player_choice in paper_list and computer_choice in rock_list:
        print('PAPER covers the rock and YOU just BEAT the computer')
    else:
        print('Sorry, MATE, but you lost to the computer')
    
    print('\n\n' + 'Are YOU ready for another game?')
    player_game_choice_1 = input()
    player_game_choice_1 = player_game_choice_1.lower()
    game_choice = ['yes', 'y']
    if player_game_choice_1 not in game_choice:
        print('\n\n' + 'THE END'.center(130, '=') + '\n\n')
        break
    else:
        print('\n\n' + 'WELCOME AGAIN IN '.center(130, '=') + '\n')


