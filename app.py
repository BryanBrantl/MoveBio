import streamlit as st

# Título principal
st.title("Projeto - Carrinho Controlado por EMG")

# Abas principais
tab_resumo, tab_cronograma, tab_sobre = st.tabs(["Resumo", "Cronograma", "Sobre"])

# Aba: Resumo (exemplo simples)
with tab_resumo:
    st.header("Resumo do Projeto")
    st.write("""
        Este projeto tem como objetivo desenvolver um carrinho controlado por sinais EMG (eletromiográficos),
        com foco na aplicação de instrumentação biomédica e controle embarcado.
    """)

# Aba: Cronograma (com HTML)
with tab_cronograma:
    st.header("Cronograma do Projeto – Carrinho Controlado por EMG")

    cronograma_html = """
    <h3 style="color: #ff4b4b;">Entregáveis</h3>
    <ul>
      <li><b>11/04:</b> Entregável #1 – Plano de Projeto</li>
      <li><b>11/04:</b> Entregável #2 – Blog do Projeto (link inicial)</li>
      <li><b>23/05:</b> Entregável #3 – Projeto e testes de Hardware</li>
      <li><b>04/07:</b> Entregável #4 – Projeto e testes de Software (relatório, vídeo e blog)</li>
      <li><b>11/07:</b> Entregável #5 – Integração e Demonstração para banca</li>
    </ul>

    <h3 style="color: #ff4b4b;">Atividades</h3>
    <table style="width:100%; border-collapse: collapse;" border="1">
      <tr style="background-color: #333; color: white;">
        <th>Atividade</th><th>Responsável</th><th>Início</th><th>Fim</th><th>Duração</th>
      </tr>
      <tr><td>Montagem do carrinho</td><td>Leonardo</td><td>08/04</td><td>10/04</td><td>2 dias</td></tr>
      <tr><td>Projeto circuito EMG</td><td>Bryan</td><td>10/04</td><td>13/04</td><td>3 dias</td></tr>
      <tr><td>Simulação circuito EMG</td><td>Bryan</td><td>13/04</td><td>14/04</td><td>1 dia</td></tr>
      <tr><td>Montagem EMG protoboard</td><td>João</td><td>12/04</td><td>13/04</td><td>2 dias</td></tr>
      <tr><td>Calibração do sinal EMG</td><td>João</td><td>13/04</td><td>14/04</td><td>1 dia</td></tr>
      <tr><td>Montagem dos motores</td><td>Luiz</td><td>18/04</td><td>19/04</td><td>1 dia</td></tr>
      <tr><td>Leitura do sinal EMG</td><td>Luiz</td><td>20/04</td><td>21/04</td><td>2 dias</td></tr>
      <tr><td>Interpretação sinais EMG</td><td>Bryan</td><td>22/04</td><td>24/04</td><td>2 dias</td></tr>
      <tr><td>Controle do carrinho</td><td>Todos</td><td>26/04</td><td>28/04</td><td>3 dias</td></tr>
      <tr><td>Testes com voluntário</td><td>Todos</td><td>29/04</td><td>30/04</td><td>2 dias</td></tr>
      <tr><td>Ajustes finais</td><td>Todos</td><td>01/05</td><td>02/05</td><td>2 dias</td></tr>
    </table>

    <h3 style="color: #ff4b4b; margin-top: 40px;">Resumo por Responsável</h3>
    <ul>
      <li><b>Leonardo:</b> 2 dias</li>
      <li><b>Bryan:</b> 6 dias</li>
      <li><b>João:</b> 5 dias</li>
      <li><b>Luiz:</b> 4 dias</li>
      <li><b>Total do Projeto:</b> 21 dias</li>
    </ul>
    """

    st.markdown(cronograma_html, unsafe_allow_html=True)

# Aba: Sobre (exemplo simples)
with tab_sobre:
    st.header("Sobre")
    st.write("Aplicação desenvolvida por alunos de Engenharia Eletrônica para a disciplina de Oficina de Integração.")
