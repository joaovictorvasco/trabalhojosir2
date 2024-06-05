import streamlit as st
from streamlit.report_thread import get_report_ctx
 
def pagina_inicial():
    st.title('Página Inicial')
    st.write('Bem-vindo à minha primeira página!')
 
def pagina_secundaria():
    st.title('Página Secundária')
    st.write('Esta é a segunda página.')
 
def main():
    # Obtenha o contexto do relatório para acessar o estado da sessão
    ctx = get_report_ctx()
 
    # Verifique se a sessão está ativa
    if not hasattr(st, '_session_state'):
        st._session_state.active_page = 'Página Inicial'
 
    # Adicione um seletor de página
    pagina = st.sidebar.radio('Navegar', ('Página Inicial', 'Página Secundária'))
 
    # Atualize o estado da página ativa
    if ctx.session_state.active_page != pagina:
        ctx.session_state.active_page = pagina
 
    # Renderize a página correspondente com base na seleção
    if ctx.session_state.active_page == 'Página Inicial':
        pagina_inicial()
    elif ctx.session_state.active_page == 'Página Secundária':
        pagina_secundaria()
 
if __name__ == '__main__':
    main()
