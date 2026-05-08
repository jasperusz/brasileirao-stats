import streamlit as st
from main import search_team, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_options, team_draws_count

st.title('Brasileirão Team Stats (2003-2025)')
input_teams = st.selectbox('Input the team to get their stats from Brasileirao (2003-2025): ', team_options ).lower().replace('-', ' ')

if input_teams:
    results = search_team(input_teams, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_draws_count)
    if results:
        st.write(f'- {results["team_name"]}\n'
                 f'- Matches Played: {results["matches"]}\n'
                 f'- Wins: {results["wins"]}\n'
                 f'- Draws: {results["draws"]}\n'
                 f'- Total Points Earned: {int(results["points"])}\n'
                 f'- Performance Record: {results["wins_avg"]:.2f}% (Percentage of points won per match played)\n'
                 f'- Points per game: {results["points_avg"]:.2f}')