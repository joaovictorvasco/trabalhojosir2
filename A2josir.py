import streamlit as st
# Dados simulados - Você pode substituir esses dados com a resposta da API do YouTube
podcasts = {
   "Conversas": ["Canal 1", "Canal 2", "Canal 3", "Canal 4", "Canal 5", "Canal 6", "Canal 7", "Canal 8", "Canal 9", "Canal 10"],
   "React": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
   "Politica": ["Canal 21", "Canal 22", "Canal 23", "Canal 24", "Canal 25", "Canal 26", "Canal 27", "Canal 28", "Canal 29", "Canal 30"],
    "Empreendedorismo": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
    "Paranormal": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
    "Esporte": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
    "Games": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
    "Especialistas": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
    "Tecnologia": ["Canal 11", "Canal 12", "Canal 13", "Canal 14", "Canal 15", "Canal 16", "Canal 17", "Canal 18", "Canal 19", "Canal 20"],
}

# Página 1: Perguntas sobre hábitos de assistir podcasts
st.title("Amantes de Podcast")
st.header("Vamos conhecer seus hábitos de assistir podcasts!")
assiste_podcast = st.radio("Você costuma assistir podcast?", ("Sim, amo!", "Não"))
frequencia = st.selectbox("Com qual frequência você assiste?", ["Diariamente", "Semanalmente", "Mensalmente", "Raramente", "Nunca"])
canais_diferentes = st.radio("Você costuma assistir canais diferentes?", ("Sim", "Não, gosto de assistir o mesmo sempre "))
st.header("Se sim, que bom! Vou te mostrar outros para você experimentar. Se você só assiste os mesmo, essa é uma ótima oportunidade para conhecer novos canais. Vamos la? ")
ansioso = st.selectbox("sim, vamos la", ("claro, estou ansioso (a)"))

# Página 2: Perguntar sobre o nicho de interesse
if assiste_podcast == "Sim":
   st.header("Qual nicho de podcast você gosta de assistir?")
   nicho = st.selectbox("Escolha um nicho", ["Conversa", "React", "Politica", "Empreendedorismo", "Paranormal", "Esporte", "Games", "Especialistas", "Tecnologia"])
   # Mostrar os 10 melhores canais de podcast no nicho escolhido
  
   st.header(f"Top 10 canais de podcast no YouTube brasileiro sobre {nicho}")
   for i, canal in enumerate(podcasts[nicho], 1):
       st.write(f"{i}. {canal}")
else:
   st.write("Parece que você não assiste podcasts. Talvez você possa começar a assistir alguns dos nossos recomendados!")
```

