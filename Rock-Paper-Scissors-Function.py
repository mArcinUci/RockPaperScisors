import random
from enum import IntEnum

class Options(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    
    
def opening():
    opening_string = 'THE PYTHON GAME: ROCK PAPER SCISSORS'
    print('\n' + opening_string.center(130, '=') + '\n\n')

def player_choice():
    player_options = [f'{option.name}[{option.value}]' for option in Options]
    player_options_str = ','.join(player_options)
    choice = int(input(f'Please choose your wapon ({player_options_str}): '))
    made_choice = Options(choice)
    return made_choice
    
def cpu_choice():
    computer_options = random.randint(0, len(Options)-1)
    cpu_made_choice = Options(computer_options)
    return cpu_made_choice
    
def is_draw(made_choice, cpu_made_choice):
    if made_choice == cpu_made_choice:
        return True
        
    
def who_won(made_choice, cpu_made_choice):
    if made_choice.value == 0 and cpu_made_choice.value == 2:
        print('\n' + f'{cpu_made_choice.name} have no chance against the {made_choice.name}. You WON!' + '\n')
    elif made_choice.value == 1 and cpu_made_choice.value == 0:
        print('\n' + f'{made_choice.name} covers {cpu_made_choice.name}. You WON!' + '\n')
    elif made_choice.value == 2 and cpu_made_choice.value == 1:
        print('\n' + f'{made_choice.name} cut {cpu_made_choice.name}, so You are the WINNER!' + '\n')
    else:
        print('\n' + f'ups, sorry mate but {cpu_made_choice.name} beats {made_choice.name}, so You LOST' + '\n')


def play_game():
    while True:
        opening()
        try:
            made_choice = player_choice()
        except ValueError as er:
            valid_number = (len(Options) - 1)
            print(f"Sory mate, wrong choice. Please pick a number from 0 to {valid_number}")
            continue

        cpu_made_choice = cpu_choice()
        if is_draw(made_choice, cpu_made_choice):
            print('\n' + f'You and CPU both picked {made_choice.name}, so there is a DRAW' + '\n')
        else:
            print(f'So You picked {made_choice.name} and CPU picked {cpu_made_choice.name}, that means:')
            who_won(made_choice, cpu_made_choice)

        
        play_again = input('\n' + "Are You ready for another challange? (y/n): " + '\n')
        if play_again.lower() != "y":
            print('\n\n' + 'THE END'.center(130, '=') + '\n\n')
            break
        else:
            print('\n\n' + 'WELCOME AGAIN IN '.center(130, '='))

if __name__ == '__main__':
    play_game()