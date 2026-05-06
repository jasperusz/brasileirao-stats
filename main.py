import pandas as pd

match_summary = pd.read_csv('data/campeonato-brasileiro-full.csv')
match_stats = pd.read_csv('data/campeonato-brasileiro-estatisticas-full.csv')
match_goals = pd.read_csv('data/campeonato-brasileiro-gols.csv')
match_cards = pd.read_csv('data/campeonato-brasileiro-cartoes.csv')

team_wins_count = match_summary[match_summary['vencedor'] != '-'].value_counts('vencedor')
team_wins_index = team_wins_count.index.str.lower()

input_teams = input('Input the team who you want to know how many matches they won in Brasileirao: ' ).lower()
get_index = team_wins_index.get_loc(input_teams) if input_teams in team_wins_index else None
team_name = team_wins_count.index[get_index]

"""
input_teams sends the team name in lower so it can be compared with the names in the dataset, which are also converted to lower.
If the team name is found, the code retrieves the index of that team in the team_wins_index and then uses that index to get 
the corresponding team name from team_wins_count.index, which is stored in team_name. 
If the team name is not found, team_name will be None.
"""

if team_name:
     print(f'{input_teams.title()} won {team_wins_count[team_name]} matches in Brasileirão in this period (2003-2025).')
else:
     print(f'{input_teams.title()} is not found in the dataset or has not won any matches in Brasileirão.')