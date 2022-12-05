import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')
st.set_page_config(layout='wide')
st.text('Santiago Plana')
st.title('Portfolio Python')
col1, col2 = st.columns(2)

dfCols = df.columns
with col1:
    st.image('imgs/foto.jpeg', use_column_width='always', )

with col2:
    # with st.container():
    st.subheader('Acerca de mí')
    st.info('A lo largo de mi vida he cursado estudios y pasado por trabajos diversos. Ninguno terminó emocionándome'
             'y captándome tanto como lo hizo la programación, y más específicamente la ciencia de datos. '
             'Desde que tímidamente empecé aprender Python, allá por el 2021, desarrollé un conjunto de habilidades'
             'que me permitió y me permite explorar temas de gran interés para mí, '
             'pudiendo explayar mis capacidades lógicas y analíticas para la resolución de problemas de una manera '
             'que no había conocido hasta entonces. '
             'Poder explorar tales temas con la potencia que ofrecen las herramientas que he podido aprender a '
             'utilizar es realmente emocionante, '
             'y no he dejado de estar entusiasmado por poder trabajar y mejorar constantemente. Mi conjunto de '
             'habilidades técnicas comprende un fluido manejo de Python '
             '(en especial de las librerías comúnmente utilizadas en manejo de datos, visualización, NLP, '
             'machine learning),así como también sólido conocimiento en otros lenguajes o herramientas '
             'complementarias como SQL, Spark, Airflow, Hadoop y Excel, entre otros. '
             'Además, cuento con un excelente manejo del inglés,'
             'habiéndome desempeñado intermitentemente como traductor y profesor particular. Por otro lado, '
             'destaco mi habilidad de aprendizaje, mi capacidad para el razonamiento y la lógica, '
             'y mi entusiasmo por la resolución de problemas.')


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    with st.container():
        for index, row in df[:4].iterrows():
            st.header(row['title'])
            image = 'imgs/'+row['image']
            st.image(f'{image}')
            st.write(row['description'])
            url = row['url']
            st.write(f'[Código]({url})')


with col4:
    with st.container():
        for index, row in df[4:].iterrows():
            st.header(row['title'])
            image = 'imgs/' + row['image']
            st.image(f'{image}')
            st.write(row['description'])
            url = row['url']
            st.write(f'[Código]({url})')
