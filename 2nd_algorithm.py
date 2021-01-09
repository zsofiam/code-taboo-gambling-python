import random
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_one_card(score_to_reach_limit):
    cards = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 10, 'Q': 10,
        'K': 10, 'A': '?'
        }
    
    # gets random key
    card_taken = random.choice(list(cards))
    card_score = cards[card_taken]
    
    if card_taken == 'A':
        card_score = 11 if 11 < score_to_reach_limit else 1

    return card_taken, card_score

def get_yes_or_no(question):
    yes_or_no = input(question + '(press Y or N) ').lower()

    while yes_or_no.lower() not in ['y', 'n']:
        yes_or_no = input('Only Y/y or N/n is accepted ').lower()

    return yes_or_no == 'y'


def get_score_for_player(name):
    user_score = 0
    limit = 21
    
    card_taken, card_score = get_one_card(limit - user_score) 
    user_score += card_score

    while user_score <= limit:
        print(f'{name} - You got {card_taken}, your score is {user_score}')
        take_one_more = get_yes_or_no('Do you want to take another card?')
        if take_one_more:
            card_taken, card_score = get_one_card(limit - user_score) 
            user_score += card_score
        else:
            break

    if user_score <= limit:
        print(f'Your final score in this round {user_score}\n')
        return user_score
    else:
        print(f'You got toooo many point: {user_score}\n')
        return 0


def play_one_round(name1, name2):
    score1 = get_score_for_player(name1)
    score2 = get_score_for_player(name2)

    if score2 < score1:
        return name1
    elif score1 < score2:
        return name2
    
    return None


def return_player_if_won(players, limit):
    for player, score in players.items():
        if limit <= score:
            return player

    return ''


def main():
    players = {}
    winner = ''
    how_many_to_win = 3

    player1 = input('Gimme the name of the first player: ')
    player2 = input('Gimme the name of the second player: ')
    
    players[player1] = 0
    players[player2] = 0

    print("You must win 3 rounds to win the whole game! Let's Get Ready To Rumble!!!")

    while not winner:
        winner_of_round = play_one_round(player1, player2)
        clear_terminal()

        if winner_of_round:
            players[winner_of_round] += 1
            print(f'{winner_of_round} won this round.\n')
            winner = return_player_if_won(players, how_many_to_win)
        else:
            print('It was a tie.\n')

    print(f'{winner} won the whole game too.')

main()