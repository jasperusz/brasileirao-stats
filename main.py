import pandas as pd

match_summary = pd.read_csv('data/campeonato-brasileiro-full.csv')
match_stats = pd.read_csv('data/campeonato-brasileiro-estatisticas-full.csv')
match_goals = pd.read_csv('data/campeonato-brasileiro-gols.csv')
match_cards = pd.read_csv('data/campeonato-brasileiro-cartoes.csv')

team_wins_count = match_summary[match_summary['vencedor'] != '-'].value_counts('vencedor')

input_teams = input('Input the team who you want to know how many matches they won in Brasileirao: ' ).title()
if input_teams in team_wins_count:
    print(f'{input_teams} won {team_wins_count[input_teams]} matches in Brasileirão in this period (2003-2025).')
else:
    print(f'{input_teams} is not found in the dataset or has not won any matches in Brasileirão.')
