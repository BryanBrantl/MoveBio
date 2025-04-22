import streamlit as st
import base64

st.set_page_config(page_title="Projeto - BioMove", layout="wide")

# Título ou seção
st.markdown("## Projeto")
abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

with abas[0]:
    st.markdown("""<h1>Home</h1>""", unsafe_allow_html=True)

    # 👤 Perfis dos integrantes com imagens personalizadas
    colunas = st.columns(4)
    fotos = ["image/foto_01.png", "image/foto_02.png", "image/foto_03.png", "image/foto_04.png"]
    nomes = [
        ("Bryan Alexandre de Lima Brantl", "2414139", "email@alunos.utfpr.edu.br", "41 992783929"),
        ("João Roberto Klassen", "2414XXX", "email@alunos.utfpr.edu.br", "41 992783929"),
        ("Leonardo Amancio", "240XXX", "email@alunos.utfpr.edu.br", "41 992783929"),
        ("Luiz Prado", "240XXX", "email@alunos.utfpr.edu.br", "41 992783929")
    ]

    for col, foto, (nome, ra, email, tel) in zip(colunas, fotos, nomes):
        with col:
            st.image(foto, width=500)
            st.markdown(f"""
                <div style='text-align: center;'>
                    <p><b>{nome}</b></p>
                    <p>RA: {ra}</p>
                    <p>Email: {email}</p>
                    <p>Contato: {tel}</p>
                </div>
            """, unsafe_allow_html=True)

# Estilo customizado
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .custom-img {
        border-radius: 12px;
        box-shadow: 0 0 15px #DC143C;
        width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

file_path = "image/gif3.gif"
with open(file_path, "rb") as f:
    data = f.read()
    encoded_gif = base64.b64encode(data).decode("utf-8")

# Exibe o GIF redondo
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/gif;base64,{encoded_gif}"
             style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover;"
             alt="GIF redondo">
    </div>
    <p style="text-align: center;">(GIF)</p>
    """,
    unsafe_allow_html=True
)

# Texto descritivo
st.markdown("""
<p style="text-align: justify;">
<b><span style="color:#DC143C;">BioMove</span></b> é um projeto de um <span style="color:#DC143C;">carrinho controlado por sinais EMG</span>, criado para auxiliar na <span style="color:#DC143C;">fisioterapia interativa</span>. Utilizando <span style="color:#DC143C;">sensores musculares caseiros</span>, o sistema interpreta os sinais do corpo e os converte em comandos para movimentar o carrinho. A ideia é unir <span style="color:#DC143C;">tecnologia</span> e <span style="color:#DC143C;">gamificação</span> como forma de tornar o processo de reabilitação mais <span style="color:#DC143C;">dinâmico</span> e <span style="color:#DC143C;">motivado</span>.
</p>
""", unsafe_allow_html=True)
