import pandas as pd
import numpy as np
import csv

'''
Data structures: use dataframes
Goal: be able to access important information about players, like their gameweek performance history in last gameweeks played in

'''
def process_player_data():
    '''
    DICT:  seasons_data[2016] = player_info[player_id]  = dataframe for them that season.
    '''

    seasons_data = {}
    SEASONS = ["2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23","2023-24"]
    for season in SEASONS:
        # print("processing season: ", season)
        file_path = f"../data/{season}/player_idlist.csv"
        player_list = []
        player_info = {}
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
        
            # Iterate over the csv reader object to add each row to the list
            for row in csv_reader:
                player_list.append(row)
        #[first,last,id]
        player_list.pop(0)
                
        for player in player_list:
            name = ""
            name += str(player[0]) + "_" + str(player[1])
            if season != "2016-17" and season != "2017-18": #later seasons also have ID number because of duplicate issue
                name += "_" + player[2]

            file_path = f"../data/{season}/players/{name}/gw.csv"
            player_info[player[2]] = pd.read_csv(file_path)
        
        seasons_data[season] = player_info

    return seasons_data

def get_season_summary():
    '''
    seasons_data[season] = DF with the table of players and their season totals 
    '''

    seasons_data = {}
    SEASONS = ["2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23","2023-24"]
    for season in SEASONS:
        # print("processing season: ", season)
        file_path = f"../data/{season}/cleaned_players.csv"
        summary = pd.read_csv(file_path, encoding="utf-8")
        seasons_data[season] = summary.sort_values(by="total_points", ascending=False)

    return seasons_data

# summaries = get_season_summary()
# print(summaries["2020-21"])