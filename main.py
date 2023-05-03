import requests
import pandas as pd


def print_col(c_list):
    """
    print list in 6 columns

    :param c_list:
    :return:
    """

    for a, b, c, d, e, f in zip(c_list[::6], c_list[1::6], c_list[2::6], c_list[3::6], c_list[4::6], c_list[5::6]):
        print('{:<20}{:<20}{:<20}{:<20}{:<20}{:<}'.format(a, b, c, d, e, f))


# importing champion data to a DataFrame from league of legends api
api_url = 'http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/champion.json' # There is version in URL so it does
# not update automatically
response = requests.get(api_url)
champions_json = response.json()
champions_df = pd.DataFrame(champions_json)
champion_names = [champion['name'] for champion in champions_df['data']]

# saving champion names as a list
champion_names.sort()
champions_not_guessed = list(champion_names)

# setting flag of loop
not_won = True

# user chooses level of difficulty:
# EASY: User sees number of letters
# MEDIUM: User sees first letters
# HARD: User sees no information
level = input("Choose difficulty level you wanna play: EASY, MEDIUM or HARD.\n")

if level == 'EASY':
    # list of answer strings with current answers and place for every champion
    ans_str = []
    for i, champion in enumerate(champion_names):
        name = f'{i + 1}. ' + len(champion) * '_'
        ans_str.append(name)
    while not_won:

        ans = input('Type champion name:\n')

        if ans in champions_not_guessed:
            ind = champion_names.index(ans)
            ans_str[ind] = ans_str[ind].replace('_', '')
            ans_str[ind] += champion_names[ind]
            champions_not_guessed.remove(ans)
            # Printing answer strings in columns
            print_col(ans_str)
            print()
        elif ans in champion_names:
            print("You have already guessed it!")

        else:
            print('Wrong input!')

        if len(champions_not_guessed) == 0:
            not_won = False
            print("CONGRATULATIONS! YOU HAVE WON!!!")

elif level == 'MEDIUM':

    # list of answer strings with current answers and place for every champion
    ans_str = []
    for i, champion in enumerate(champion_names):
        name = f'{i + 1}. {champion[0]}'
        ans_str.append(name)

    while not_won:
        ans = input('Type champion name:\n')

        if ans in champions_not_guessed:
            ind = champion_names.index(ans)
            ans_str[ind] += champion_names[ind][1:]
            champions_not_guessed.remove(ans)
            # Printing answer strings in columns
            print_col(ans_str)
            print()
        elif ans in champion_names:
            print("You have already guessed it!")

        else:
            print('Wrong input!')

        if len(champions_not_guessed) == 0:
            not_won = False
            print("CONGRATULATIONS! YOU HAVE WON!!!")

elif level == 'HARD':
    # list of answer strings with current answers and place for every champion
    ans_str = []
    for i, champion in enumerate(champion_names):
        name = f'{i + 1}. '
        ans_str.append(name)
    while not_won:
        ans = input('Type champion name:\n')

        if ans in champions_not_guessed:
            ind = champion_names.index(ans)
            ans_str[ind] += champion_names[ind]
            champions_not_guessed.remove(ans)
            # Printing answer strings in columns
            print_col(ans_str)
            print()
        elif ans in champion_names:
            print("You have already guessed it!")

        else:
            print('Wrong input!')

        if len(champions_not_guessed) == 0:
            not_won = False
            print("CONGRATULATIONS! YOU HAVE WON!!!")

else:
    print('No such level!')

