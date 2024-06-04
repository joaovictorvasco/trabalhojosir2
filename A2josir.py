import streamlit as st
import pandas as pd

# Página 1: Perguntas sobre hábitos de assistir podcasts
st.title("Amantes de Podcast")
st.header("Vamos conhecer seus hábitos de assistir podcasts!")
assiste_podcast = st.radio("Você costuma assistir podcast?", ("Sim, amo!", "Não"))
frequencia = st.selectbox("Com qual frequência você assiste?", ["Diariamente", "Semanalmente", "Mensalmente", "Raramente", "Nunca"])
canais_diferentes = st.radio("Você costuma assistir canais diferentes?", ("Sim", "Não, gosto de assistir o mesmo sempre "))

if assiste_podcast == "Sim, amo!":
    st.header("Se sim, que bom! Vou te mostrar outros para você experimentar. Se você só assiste os mesmo, essa é uma ótima oportunidade para conhecer novos canais. Vamos la? ")
    ansioso = st.selectbox(("sim, vamos la"), ("claro, estou ansioso (a)",))
    st.experimental_set_query_params(page=2)  # Altera para a página 2 após responder as perguntas
else:
    st.write("Parece que você não assiste podcasts. Talvez você possa começar a assistir alguns dos nossos recomendados!")

# Página 2: Perguntar sobre o nicho de interesse
if "page" in st.experimental_get_query_params():
    if st.experimental_get_query_params()["page"] == ["2"]:
        st.header("Qual nicho de podcast você gosta de assistir?")
        nicho = st.selectbox("Escolha um nicho", ["Conversas", "React", "Politica", "Empreendedorismo", "Paranormal", "Esporte", "Jogos", "Especialistas", "Tecnologia"])
        nome_arquivo = "podcast_" +  nicho.lower() + ".csv"
        # Mostrar os 10 melhores canais de podcast no nicho escolhido
        df = pd.read_csv(nome_arquivo)
        st.header(f"Top 10 canais de podcast no YouTube brasileiro sobre {nicho}")
        st.write(df)
