import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv', sep=';')
st.text('Santiago Plana')
st.title('Portfolio Python')
col1, col2 = st.columns([3, 3])

dfCols = df.columns
with col2:
    with st.container():
        for n in range(len(df)):
            st.subheader(f'{df.loc[n, "title"]}')
            image = 'imgs/'+df.loc[n, "image"]
            st.image(f'{image}')
            st.write(f'{df.loc[n, "description"]}')
            url = df.loc[n, "url"]
            st.write('[Código](url)')

with col1:
    with st.container():
        st.subheader('Acerca de mí')
        st.write('bla bla bla bla bla bla bla bla bla bla bla asjhdahsdashdashdashdasdasdasdasdasd')

