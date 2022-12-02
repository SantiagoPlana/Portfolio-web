import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv', sep=';')
st.text('Santiago Plana')
st.title('Portfolio Python')
col1, col2, col3 = st.columns([2, 2, 2])

with col2:
    with st.container():
        st.subheader('Nombre del proyecto')
        st.image('imgs/1.png')
        st.text('Explicación breve del proyecto')
        st.subheader('Nombre del proyecto')
        st.image('imgs/1.png')
        st.text('Explicación breve del proyecto')

with col3:
    with st.container():
        st.subheader('Nombre del proyecto')
        st.image('imgs/1.png')
        st.text('Explicación breve del proyecto')
with col1:
    with st.container():
        st.subheader('Acerca de mí')
        st.text('''bla bla bla bla bla bla 
bla bla bla 
bla bla bla''')

