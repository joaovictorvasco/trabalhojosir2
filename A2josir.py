import streamlit as st
import pandas as pd
from PIL import Image

st.sidebar.title ("Já conhece o nosso site?")
st.sidebar.info ("Nosso site é para os amantes de podcast que estão em busca de novos canais. Aqui você pode escolher a categoria que você gosta e descobrir novas experiências. Aproveite!")

# Página 1: Perguntas sobre hábitos de assistir podcasts
st.title("Amantes de Podcast")
foto = Image.open('Foto site .JPG') 
st.image(foto, width= 500)
st.header("Vamos conhecer seus hábitos de assistir podcasts!")
assiste_podcast = st.radio("Você costuma assistir podcast?", ("Sim, amo!", "Não"))
frequencia = st.selectbox("Com qual frequência você assiste?", ["Diariamente", "Semanalmente", "Mensalmente", "Raramente", "Nunca"])
canais_diferentes = st.radio("Você costuma assistir canais diferentes?", ("Sim", "Não, gosto de assistir o mesmo sempre "))

with st.form('form'):
    if assiste_podcast == "Sim, amo!":
        st.header("Se sim, que bom! Vou te mostrar outros para você experimentar. Se você só assiste os mesmo, essa é uma ótima oportunidade para conhecer novos canais. Vamos la? ")
        
        st.experimental_set_query_params(page=2)   # Altera para a página 2 após responder as perguntas
    else:
        st.write("Parece que você não assiste podcasts. Talvez você possa começar a assistir alguns dos nossos recomendados!")
    botao = st.from_submit_button('next') 
        

# Página 2: Perguntar sobre o nicho de interesse
#if "page" in st.experimental_get_query_params():
if botao:
    if st.experimental_get_query_params()["page"] == ["2"]:
        st.header("Qual nicho de podcast você gosta de assistir?")
        nicho = st.selectbox("Escolha um nicho", ["Conversas", "React", "Politica", "Empreendedorismo", "Paranormal", "Esporte", "Jogos", "Especialistas", "Tecnologia"])
        nome_arquivo = "podcast_" +  nicho.lower() + ".csv"
        # Mostrar os 10 melhores canais de podcast no nicho escolhido
        df = pd.read_csv(nome_arquivo)
        st.header(f"Top 10 canais de podcast no YouTube brasileiro sobre {nicho}")
        st.write(df)
        # Adiciona a imagem no topo da primeira página
st.image("https://tecnoblog.net/noticias/youtube-teste-problema-desmonetizacao/", use_column_width=True)

