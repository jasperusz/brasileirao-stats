import streamlit as st
import pandas as pd
import plotly.express as px
from main import search_team, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_options, team_draws_count, top_10_teams

translations = {
     'English': {
            'title': 'Brasileirão Team Stats',
            'select_team': 'Select Team to view stats: ',
            'matches_played': 'Matches Played',
            'points_earned': 'Points Earned',
            'wins': 'Wins',
            'points_per_game': 'PPG (Points per Game)',
            'draws': 'Draws',
            'performance_record': 'Performance Record (%)',
            'not_found': 'Team not found. Try again.',
            'top_10_title': 'Top 10 Teams by Wins in Brasileirão (2003-2025)',
            'chart_x': 'Team',
            'chart_y': 'Number of Wins'
     },

     'Português': {
            'title': 'Estatísticas de Times no Brasileirão',
            'select_team': 'Selecione o Time: ',
            'matches_played': 'Partidas Jogadas',
            'points_earned': 'Pontos Conquistados',
            'wins': 'Vitórias',
            'points_per_game': 'PPJ (Pontos por jogo)',
            'draws': 'Empates',
            'performance_record': 'Aproveitamento (%)',
            'not_found': 'Time não encontrado. Tente novamente.',
            'top_10_title': 'Top 10 Times por vitórias (2003-2025)',
            'chart_x': 'Time',
            'chart_y': 'Número de Vitórias'
     },
     'Español': {
            'title': 'Estadísticas de Equipos en el Brasileirão',
            'select_team': 'Seleccione el Equipo: ',
            'matches_played': 'Partidos Jugados',
            'points_earned': 'Puntos Conquistados',
            'wins': 'Victorias',
            'points_per_game': 'PPP (Puntos por partido)',
            'draws': 'Empates',
            'performance_record': 'Rendimiento (%)',
            'not_found': 'Equipo no encontrado. Inténtelo nuevamente.',
            'top_10_title': 'Top 10 Equipos por victorias (2003-2025)',
            'chart_x': 'Equipo',
            'chart_y': 'Número de Victorias'
     }
}


# The variable 'translations' is a dictionary that contains translations for the elements displayed in the app in both English
# and Portuguese-BR languages. You can add more languages by including additional dictionaries inside the variable.


with st.container(border=True):
    language = st.selectbox('Language/Idioma', options=['English', 'Português', 'Español'])
    tr = translations[language]
    st.markdown(f"<h1 style='text-align: center;'>{tr['title']}</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>(2003-2025)</h2>", unsafe_allow_html=True)
    input_teams = st.selectbox(tr['select_team'], team_options, index=None )
    if input_teams is not None: # If the user selected a team.
        with st.container(border=True):
            if input_teams:
                results = search_team(input_teams, team_wins_count, matches_played, points_earned, points_average, wins_average, team_wins_index, team_draws_count)
                if results:
                    col1, col2, col3 = st.columns(3) # Create three columns to structure the display of the metrics.
                    with col1:
                            st.metric(tr['matches_played'], results['matches'])
                            st.metric(tr['points_earned'], int(results["points"]))
                    with col2:
                            st.metric(tr['wins'], results['wins'])
                            st.metric(tr['points_per_game'], f'{results["points_avg"]:.2f}')
                    with col3:   
                            st.metric(tr['draws'], results['draws'])
                            st.metric(tr['performance_record'], f'{results["wins_avg"]:.2f}%')
                else:
                    st.write(tr['not_found'])
    
    top_10_teams = top_10_teams.rename(columns={'vencedor': tr['chart_x'], 'count': tr['chart_y']})
    top10_chart = px.bar(top_10_teams, x=tr['chart_x'], y=tr['chart_y'], title=tr['top_10_title'],\
                color_discrete_sequence=['#c7ff00']) 
    with st.container(border=True):
        st.plotly_chart(top10_chart) # Display the top 10 teams by wins in a chart.