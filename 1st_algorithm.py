from random import randint
from textwrap import dedent
import os 


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_dice_value(player_name):
    return randint(1, 6)


def get_yes_or_no(question):
    yes_or_no = input(question + '(press Y or N) ').lower()

    while yes_or_no.lower() not in ['y', 'n']:
        yes_or_no = input('Only Y/y or N/n is accepted ').lower()

    return yes_or_no == 'y'


def main():
    player_name = ''
    current_player_index = 0
    sum_of_dice_values_in_this_round = 0
    safe_score_of_players = [0, 0]
    score_to_reach = 100
    current_player_won = False

    clear_terminal()
    print("Let's start the game :)\n")

    while not current_player_won:
        player_name = f'Player {current_player_index + 1}'
        dice_value = get_dice_value(player_name)

        if dice_value == 1:
            print(f'{player_name} - Booo. You threw 1, you lost your {sum_of_dice_values_in_this_round} and stayed with {safe_score_of_players[current_player_index]}')
            sum_of_dice_values_in_this_round = 0
            current_player_index = 0 if current_player_index == 1 else 1
            continue
        
        sum_of_dice_values_in_this_round += dice_value
        print(f'{player_name} - Hurraaay, you threw {dice_value}')
        
        current_player_won = score_to_reach <= safe_score_of_players[current_player_index] + sum_of_dice_values_in_this_round
        if not current_player_won:
            # dedent cuts down leading spaces from each line of this string
            do_you_rethrow_question = dedent(f'''
                Your safe score is {safe_score_of_players[current_player_index]}
                Your score in this round is {sum_of_dice_values_in_this_round}
                Do you want to throw the dice again? [stressful music in the background])
                ''')
        
            rethrow = get_yes_or_no(do_you_rethrow_question)
            clear_terminal()

            if not rethrow:
                print(f'Wise decision. Your safe score became {safe_score_of_players[current_player_index]}')
                safe_score_of_players[current_player_index] += sum_of_dice_values_in_this_round
                sum_of_dice_values_in_this_round = 0
                current_player_index = 0 if current_player_index == 1 else 1
            
    print(f'{player_name} won :)')


main()