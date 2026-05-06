import pandas as pd
import numpy as np


match_summary = pd.read_csv('data/campeonato-brasileiro-full.csv')
match_stats = pd.read_csv('data/campeonato-brasileiro-estatisticas-full.csv')
match_goals = pd.read_csv('data/campeonato-brasileiro-gols.csv')
match_cards = pd.read_csv('data/campeonato-brasileiro-cartoes.csv')

# Matches Played Variables
matches_played = match_summary[match_summary['mandante'].str.replace('-', ' ') != '-'].value_counts('mandante') + \
match_summary[match_summary['visitante'].str.replace('-', ' ') != '-'].value_counts('visitante')

# Winner Teams Variables
team_wins_count = match_summary[match_summary['vencedor'].str.replace('-', ' ') != '-'].value_counts('vencedor')
wins_average =  team_wins_count / 23 # 23 seasons in the dataset (2003-2025)
points_earned = team_wins_count * 3 # 3 points for each win
points_average = wins_average * 3
team_wins_index = team_wins_count.index.str.lower().str.replace('-', ' ')

input_teams = input('Input the team who you want to know how many matches they won in Brasileirao: ' ).lower().replace('-', ' ')
get_index = team_wins_index.get_loc(input_teams) if input_teams in team_wins_index else None
team_name = team_wins_count.index.to_numpy()[get_index]


"""
input_teams sends the team name in lower so it can be compared with the names in the dataset, which are also converted to lower.
.replace is used to remove any hyphens from team names, exampling 'Atletico-MG'.
If the team name is found, the code retrieves the index of that team in the team_wins_index and then uses that index to get 
the corresponding team name from team_wins_count.index, which is stored in team_name. 
If the team name is not found, team_name will be None.
"""

if len(team_name) > 0:
     try:  
          print(f'{input_teams.title()} won {team_wins_count[team_name]} matches in Brasileirão in {matches_played[team_name]} matches played.\n'
               f'{input_teams.title()} earned {points_earned[team_name]} points in total across this period.\n'
               f'Their average is {wins_average[team_name]:.2f} wins, scoring {points_average[team_name]:.2f} points per season.')
     except ValueError:
          print(f'{input_teams.title()} is not found in the dataset or has not won any matches in Brasileirão.')

