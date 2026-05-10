import pandas as pd
import numpy as np
import streamlit as st

# Data loading and preprocessing functions to be used in Streamlit app
@st.cache_data
def load_data():
     match_summary = pd.read_csv('data/campeonato-brasileiro-full.csv')
     other_stats = pd.read_csv('data/campeonato-brasileiro-estatisticas-full.csv')
     return match_summary, other_stats
match_summary, other_stats = load_data()


# Matches Played Variables
matches_played = match_summary[match_summary['mandante'].str.replace('-', ' ') != '-'].value_counts('mandante') + \
match_summary[match_summary['visitante'].str.replace('-', ' ') != '-'].value_counts('visitante')

# Team Stats Variables
team_options = sorted(other_stats['clube'].unique())
team_wins_count = match_summary[match_summary['vencedor'] != '-'].value_counts('vencedor')
team_draws_count = match_summary[match_summary['vencedor'] == '-']['mandante'].value_counts() + \
                   match_summary[match_summary['vencedor'] == '-']['visitante'].value_counts()
points_earned = team_wins_count * 3 + team_draws_count # 3 points for each win plus 1 point for each draw
points_average = points_earned / matches_played # Points per game average
wins_average = (points_earned / (matches_played * 3)) * 100 # Performance record as a percentage of points won per match played
team_wins_index = team_wins_count.index.str.lower().str.replace('-', ' ')
top_10_teams = team_wins_count.head(10).reset_index()


def search_team(input_teams, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_draws_count):
     input_teams = input_teams.lower().replace('-', ' ')
     
     if input_teams not in team_wins_index:
          return None
     
     get_index = team_wins_index.get_loc(input_teams)
     team_name = team_wins_count.index.to_numpy()[get_index]

     return {
          'team_name': team_name,
          'wins': team_wins_count[team_name],
          'matches': matches_played[team_name],
          'points': points_earned[team_name],
          'wins_avg': wins_average[team_name],
          'points_avg': points_average[team_name],
          'draws': team_draws_count[team_name]
     }

"""
This code defines the data loading and preprocessing functions for a Streamlit app that displays statistics for Brazilian 
football teams from 2003 to 2025. 
It loads match summary and other statistics from CSV files, 
calculates matches played, wins, draws, points earned, 
points average, and performance record for each team. 
The `search_team` function allows users to input a team name and retrieve their statistics.
"""