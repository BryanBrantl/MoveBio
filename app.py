import streamlit as st
import base64

st.set_page_config(page_title="Projeto - BioMove", layout="wide")

# Título ou seção
st.markdown("## BIOMOVE")
abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

# -------- HOME --------
with abas[0]:
    st.markdown("""<h1>Home</h1>""", unsafe_allow_html=True)

    # 👤 Perfis dos integrantes com imagens personalizadas
    colunas = st.columns(4)
    fotos = ["image/foto_01.png", "image/foto_02.png", "image/foto_03.png", "image/foto_04.png"]
    nomes = [
        ("Bryan Alexandre de Lima Brantl", "2414139", "brantl@alunos.utfpr.edu.br", "(41) 99278-3929"),
        ("João Roberto Klassen", "2414155", "joaoklassen@alunos.utfpr.edu.br", "41 99742-4536"),
        ("Leonardo Amancio", "2402580", "leonardoamancio@alunos.utfpr.edu.br", "41 99805-1279"),
        ("Luiz Prado", "2402629", "luizoliveira.2002@alunos.utfpr.edu.br", "41 99815-6532")
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

# -------- BIOMOVE --------
with abas[1]:
	file_path = "image/gif3.gif"
	file_path1 = "image/7.gif"
	
	with open(file_path, "rb") as f:
	    data = f.read()
	    encoded_gif = base64.b64encode(data).decode("utf-8")
	
	with open(file_path1, "rb") as f:
	    data1 = f.read()
	    encoded_gif1 = base64.b64encode(data1).decode("utf-8")
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/gif;base64,{encoded_gif}"
                 style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover;"
                 alt="GIF redondo">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <p style="text-align: justify;">
    <b><span style="color:#DC143C;">BioMove</span></b> é um projeto de um <span style="color:#DC143C;">carrinho controlado por sinais EMG</span>, criado para auxiliar na <span style="color:#DC143C;">fisioterapia interativa</span>. Utilizando <span style="color:#DC143C;">sensores musculares</span>, o sistema interpreta os sinais do corpo e os converte em comandos para movimentar o carrinho. A ideia é unir <span style="color:#DC143C;">tecnologia</span> e <span style="color:#DC143C;">gamificação</span> como forma de tornar o processo de reabilitação mais <span style="color:#DC143C;">dinâmico</span> e <span style="color:#DC143C;">motivador</span>.
    </p>
    """, unsafe_allow_html=True)

# -------- ATUALIZAÇÃO SEMANAL --------
with abas[2]:
    st.markdown("""
    <div style="background-color:#1C1C1C; padding:15px; border-radius:10px;">
        <h4 style="color:#DC143C;">#1 - Atualização Semanal - 09/05/2024</h4>
        <ul style="color:#FFFFFF;">
            <li>Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.</li>
            <li>Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do <b>Eagle</b> para o desenvolvimento do carrinho e do sistema EMG.</li>
            <li>Modelo do site finalizado.</li>
            <li>Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.</li>
            <li>Decisões sobre o projeto: Definido que será utilizado baterias 18650 (4.2v) para alimentação dos sistemas.</li>
            <li>simulação EMG:</li>    
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <img src="data:image/gif;base64,{encoded_gif}"
                 style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover;"
                 alt="GIF redondo">
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------- RELATÓRIOS --------
with abas[3]:

    st.markdown("### Proposta de projeto")
    st.markdown(f"""
    <p style="text-align: justify;">
        Nesta seção, está disponibilizada a proposta de projeto do Biomove.
        O documento reúne informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.
    </p>
    <p style="text-align: justify;"> 
	Você pode acessar o documento completo clicando no botão abaixo:
    </p>
    """, unsafe_allow_html=True)

    # Link bonito (exemplo de link)
    link_doc = "https://docs.google.com/document/d/1uJpoXcehrK1Lv2cPMxUtHkvSNNtmgnatSJdmxfzy8gc/edit?usp=sharing"
    st.markdown(f"""
        <div style='text-align: center; margin-top: 20px;'>
            <a href="{link_doc}" target="_blank" style="
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            ">
                Acessar Proposta
            </a>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
     	<br>
	<p style= "text-align: center;">
            (Para acessar utilize o e-mail institucional)
        </p>
	""",unsafe_allow_html=True)

# -------- CRONOGRAMA --------
with abas[4]:
    st.markdown("### Cronograma e Custos do Projeto")
    st.markdown("""
    <p style="text-align: justify;">
    Nesta seção, está disponibilizado o cronograma completo juntamente com os custos previstos e realizados do projeto <b><span style="color:#DC143C;">BioMove</span></b>.

    Você pode acessar o documento completo clicando no botão abaixo:
    </p>
    """, unsafe_allow_html=True)

    link_drive = "https://docs.google.com/spreadsheets/d/1Fb5_otX8z50tuy9RbcGGC89BLKfErs_SCnML-JGeyQU/edit?usp=sharing"
    st.markdown(f"""
        <div style='text-align: center; margin-top: 20px;'>
            <a href="{link_drive}" target="_blank" style="
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            ">
                Acessar Cronograma e Custos
            </a>
        </div> 
	""", unsafe_allow_html=True)
