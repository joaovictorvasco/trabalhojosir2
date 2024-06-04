import streamlit as st
import pandas as pd

# Sidebar content
st.sidebar.title("Já conhece o nosso site?")
st.sidebar.info("Nosso site é para os amantes de podcast que estão em busca de novos canais. Aqui você pode escolher a categoria que você gosta e descobrir novas experiências. Aproveite!")

# Função para mostrar a página de perguntas sobre hábitos de assistir podcasts
def show_page1():
    st.title("Amantes de Podcast")
    st.header("Vamos conhecer seus hábitos de assistir podcasts!")
    assiste_podcast = st.radio("Você costuma assistir podcast?", ("Sim, amo!", "Não"))
    frequencia = st.selectbox("Com qual frequência você assiste?", ["Diariamente", "Semanalmente", "Mensalmente", "Raramente", "Nunca"])
    canais_diferentes = st.radio("Você costuma assistir canais diferentes?", ("Sim", "Não, gosto de assistir o mesmo sempre"))

    if assiste_podcast == "Sim, amo!":
        st.header("Se sim, que bom! Vou te mostrar outros para você experimentar. Se você só assiste os mesmos, essa é uma ótima oportunidade para conhecer novos canais. Vamos lá?")
        ansioso = st.selectbox("Você está ansioso(a) para descobrir novos canais?", ["Claro, estou ansioso(a)!"])
        if st.button("Avançar"):
            st.experimental_set_query_params(page="2")
            st.experimental_rerun()  # Rerun the script to update the page
    else:
        st.write("Parece que você não assiste podcasts. Talvez você possa começar a assistir alguns dos nossos recomendados!")

# Função para mostrar a página de nicho de interesse
def show_page2():
    st.header("Qual nicho de podcast você gosta de assistir?")
    nicho = st.selectbox("Escolha um nicho", ["Conversas", "React", "Politica", "Empreendedorismo", "Paranormal", "Esporte", "Jogos", "Especialistas", "Tecnologia"])
    nome_arquivo = "podcast_" + nicho.lower() + ".csv"
    
    try:
        # Mostrar os 10 melhores canais de podcast no nicho escolhido
        df = pd.read_csv(nome_arquivo)
        st.header(f"Top 10 canais de podcast no YouTube brasileiro sobre {nicho}")
        st.write(df)
    except FileNotFoundError:
        st.error(f"Arquivo {nome_arquivo} não encontrado.")

# Checar os parâmetros da URL para determinar qual página mostrar
params = st.experimental_get_query_params()
if "page" in params and params["page"] == ["2"]:
    show_page2()
else:
    show_page1()

