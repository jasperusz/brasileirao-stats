import streamlit as st
import pandas as pd
import plotly.express as px
from main import search_team, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_options, team_draws_count, top_10_teams


with st.container(border=True):
    st.markdown("<h1 style='text-align: center;'>Brasileirão Team Stats (2003-2025)</h1>", unsafe_allow_html=True)
    input_teams = st.selectbox('Select Team to view stats: ', team_options, index=None )
    if input_teams is not None:
        with st.container(border=True):
            if input_teams:
                results = search_team(input_teams, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_draws_count)
                if results:
                    col1, col2, col3 = st.columns(3)
                    with col1:
                            st.metric('Matches Played', results['matches'])
                            st.metric('Points Earned', int(results["points"]))
                    with col2:
                            st.metric('Wins', results['wins'])
                            st.metric('Points per Game', f'{results["points_avg"]:.2f}')
                    with col3:   
                            st.metric('Draws', results['draws'])
                            st.metric('Performance Record', f'{results["wins_avg"]:.2f}%')
                else:
                    st.write('Team not found. Try again.')

    top_10_teams = top_10_teams.rename(columns={'vencedor': 'Team', 'count': 'Number of Wins'})
    top10_chart = px.bar(top_10_teams, x='Team', y='Number of Wins', title='Top 10 Teams by Wins in Brasileirão (2003-2025)',\
                color_discrete_sequence=['#c7ff00'])
    with st.container(border=True):
        st.plotly_chart(top10_chart)