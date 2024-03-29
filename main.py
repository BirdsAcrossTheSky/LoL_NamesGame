import requests
import pandas as pd
import itertools
import time
import json
from operator import itemgetter
import os


def print_col(c_list):
    """
    print list in 6 columns

    :param c_list:
    :return:
    """

    for a, b, c, d, e, f in itertools.zip_longest(c_list[::6], c_list[1::6], c_list[2::6], c_list[3::6], c_list[4::6],
                                                  c_list[5::6], fillvalue=''):
        print('{:<20}{:<20}{:<20}{:<20}{:<20}{:<}'.format(a, b, c, d, e, f))


def print_hs_list(hs_list):
    for n, d in enumerate(hs_list):
        row = '{: >3} {: >12} {: >10}'.format(n + 1, d['username'], d['time'])
        print(row)


def guessed_stat(cng, cn):
    print(f'Champion guessed: {cn - len(cng)}/{cn} ({round((cn - len(cng)) / cn * 100.0, 2)}%)')


def hs_update(lvl):
    filename = f'hs_{lvl.lower()}.json'
    with open(filename, 'r') as f:
        try:
            if os.path.getsize(filename) == 0:
                raise ValueError('The file is empty')
            hs = json.load(f)
        except ValueError:
            hs = []

    hs.append({'username': username, 'time': final_time})
    hs = sorted(hs, key=lambda d: d['time'], reverse=False)
    print_hs_list(hs)

    with open(filename, 'w') as f:
        json.dump(hs, f)


# getting the newest version
api_ver_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
response_ver = requests.get(api_ver_url)
versions_json = response_ver.json()
versions_df = pd.DataFrame(versions_json)
newest_version = versions_df[0][0]

# importing champion data to a DataFrame from league of legends api
api_url = f'http://ddragon.leagueoflegends.com/cdn/{newest_version}/data/en_US/champion.json'
response = requests.get(api_url)
champions_json = response.json()
champions_df = pd.DataFrame(champions_json)
# champion_names = [champion['name'] for champion in champions_df['data']]
champion_names = ['Ahri', 'Aatrox']

# saving champion names as a list
champion_number = len(champion_names)
champion_names.sort()
champions_not_guessed = list(champion_names)

# setting flag of loop
not_won = True

username = input('Enter your username: ')

# user chooses level of difficulty:
# EASY: User sees number of letters
# MEDIUM: User sees first letters
# HARD: User sees no information
level = input("Choose difficulty level you wanna play: EASY, MEDIUM or HARD.\n")
start_time = time.time()

if level.upper() == 'EASY':
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
            guessed_stat(champions_not_guessed, champion_number)
            print(f'Current time: {round(time.time() - start_time, 2)} s')  # poprawić na minuty + sekundy
            print()
        elif ans in champion_names:
            print("You have already guessed it!")

        else:
            print('Wrong input!')

        if len(champions_not_guessed) == 0:
            not_won = False
            guessed_stat(champions_not_guessed, champion_number)
            print("CONGRATULATIONS! YOU HAVE WON!!!")
            final_time = round(time.time() - start_time, 2)
            print(f'Your time is {final_time} s!')

            hs_update(level)


elif level.upper() == 'MEDIUM':

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
            guessed_stat(champions_not_guessed, champion_number)
            print(f'Current time: {round(time.time() - start_time, 2)} s')  # poprawić na minuty + sekundy
            print()
        elif ans in champion_names:
            print("You have already guessed it!")

        else:
            print('Wrong input!')

        if len(champions_not_guessed) == 0:
            not_won = False
            guessed_stat(champions_not_guessed, champion_number)
            print("CONGRATULATIONS! YOU HAVE WON!!!")
            final_time = round(time.time() - start_time, 2)
            print(f'Your time is {final_time} s!')

            hs_update(level)

elif level.upper() == 'HARD':
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
            guessed_stat(champions_not_guessed, champion_number)
            print(f'Current time: {round(time.time() - start_time, 2)} s')  # poprawić na minuty + sekundy
            print()
        elif ans in champion_names:
            print("You have already guessed it!")

        else:
            print('Wrong input!')

        if len(champions_not_guessed) == 0:
            not_won = False
            guessed_stat(champions_not_guessed, champion_number)
            print("CONGRATULATIONS! YOU HAVE WON!!!")
            final_time = round(time.time() - start_time, 2)
            print(f'Your time is {final_time} s!')

            hs_update(level)

else:
    print('No such level!')
