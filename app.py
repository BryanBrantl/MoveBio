import streamlit as st

st.set_page_config(page_title="Relatórios - BioMove", layout="centered")

# Título geral
st.markdown("<h1 style='color: #4CAF50; text-align: center;'>📚 Relatórios do Projeto BioMove</h1>", unsafe_allow_html=True)
st.markdown("___")  # linha horizontal

# Índice de seções
st.markdown(
    """
    <div style="background-color: #2C2C2C; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
        <a href="#proposta" style="color: #4CAF50; margin-right: 15px; text-decoration: none;">▶ Proposta de Projeto</a>
        <a href="#pre-projeto" style="color: #4CAF50; margin-right: 15px; text-decoration: none;">▶ Pré-Projeto</a>
        <a href="#testes-hardware" style="color: #4CAF50; text-decoration: none;">▶ Relatório de Testes</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Seção Proposta de Projeto ---
st.markdown('<h2 id="proposta">📄 Proposta de Projeto  (11/04/2025)</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image("image/preview_proposta.png", width=120)
with col2:
    st.write(
        """
        Nesta seção, está disponibilizada a proposta de projeto do BioMove. O documento reúne 
        informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.  
        Palavras-chave: **Escopo**, **Objetivo**, **Diagrama de Blocos**, **Requisitos Funcionais**.
        """
    )
    st.markdown(
        """
        <a href="https://docs.google.com/document/d/1uJpoXcehrK1Lv2cPMxUtHkvSNNtmgnatSJdmxfzy8gc/edit?usp=sharing" 
           target="_blank" 
           style="
               background-color: #4CAF50; 
               color: white; 
               padding: 8px 16px; 
               text-decoration: none; 
               border-radius: 5px; 
               font-size: 14px;
           ">
            ▶ Abrir Proposta (PDF)
        </a>
        """,
        unsafe_allow_html=True
    )
st.markdown("---")

# --- Seção Pré-Projeto (Exemplo de relatório antigo) ---
with st.expander("📄 Pré-Projeto – Documento Inicial (data anterior)", expanded=False):
    st.write(
        """
        Esse relatório contém as ideias iniciais, problematização e proposta preliminar do BioMove.
        Inclui diagrama de blocos, lista de componentes e estimativa de custos.
        """
    )
    st.markdown(
        """
        <a href="https://docs.google.com/document/d/seu_link_pre_projeto" 
           target="_blank" 
           style="
               background-color: #2196F3; 
               color: white; 
               padding: 8px 16px; 
               text-decoration: none; 
               border-radius: 5px; 
               font-size: 14px;
           ">
            ▶ Abrir Relatório Pré-Projeto
        </a>
        """,
        unsafe_allow_html=True
    )
st.markdown("---")

# --- Seção Relatório de Testes de Hardware (Exemplo adicional) ---
with st.expander("📄 Relatório de Testes de Hardware  (23/05/2025)", expanded=False):
    st.write(
        """
        Detalha os testes realizados nos componentes do carrinho (motores DC, ponte H, ESP32, bateria),
        resultados de medição de corrente e tensão, ajustes em protótipos de PCB do módulo EMG, etc.
        """
    )
    st.markdown(
        """
        <a href="https://docs.google.com/document/d/seu_link_relatorio_testes" 
           target="_blank" 
           style="
               background-color: #FF9800; 
               color: white; 
               padding: 8px 16px; 
               text-decoration: none; 
               border-radius: 5px; 
               font-size: 14px;
           ">
            ▶ Abrir Relatório de Testes
        </a>
        """,
        unsafe_allow_html=True
    )
st.markdown("---")

st.markdown("<p style='text-align: center; color: gray;'>UTFPR Curitiba • Engenharia Eletrônica • 2025</p>", unsafe_allow_html=True)
