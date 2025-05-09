import streamlit as st
import base64

st.set_page_config(page_title="Projeto - BioMove", layout="wide")

# Título ou seção
st.markdown("## BIOMOVE")
abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

with abas[0]:
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
	
	    # ➕ Adição dos vídeos e SVGs da pasta "svg"
	    st.markdown("<hr><h2>Vídeos e SVGs</h2>", unsafe_allow_html=True)
	
	    for i in range(1, 9):
	        st.markdown(f"<h4>Item {i}</h4>", unsafe_allow_html=True)
	        st.video(f"svg/{i}.mp4")
	        try:
	            with open(f"svg/{i}.svg", "r", encoding="utf-8") as file:
	                svg_content = file.read()
	                st.markdown(svg_content, unsafe_allow_html=True)
	        except FileNotFoundError:
	            st.warning(f"Arquivo svg/{i}.svg não encontrado.")
with abas[1]:
    # Carrega o GIF e converte para base64
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
    <b><span style="color:#DC143C;">BioMove</span></b> é um projeto de um <span style="color:#DC143C;">carrinho controlado por sinais EMG</span>, criado para auxiliar na <span style="color:#DC143C;">fisioterapia interativa</span>. Utilizando <span style="color:#DC143C;">sensores musculares</span>, o sistema interpreta os sinais do corpo e os converte em comandos para movimentar o carrinho. A ideia é unir <span style="color:#DC143C;">tecnologia</span> e <span style="color:#DC143C;">gamificação</span> como forma de tornar o processo de reabilitação mais <span style="color:#DC143C;">dinâmico</span> e <span style="color:#DC143C;">motivadoe</span>.
    </p>
    """, unsafe_allow_html=True)

with abas[2]:
	st.markdown(f"""
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

with abas[3]:
    st.markdown("""
    <div style="background-color:#DFFFE0; padding:20px; border-radius:10px;">
        <h4 style="color:#000000;">Proposta de projeto</h4>
        <p style="color:#2F4F2F; text-align: justify;">
            Nesta seção, está disponibilizada a proposta de projeto do Biomove.
            O documento reúne informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.
        </p>
        <p style="color:#2F4F2F; text-align: justify;">
            Você pode acessar o documento completo clicando no botão abaixo:
        </p>
        <div style='text-align: center; margin-top: 20px;'>
            <a href="https://docs.google.com/document/d/1uJpoXcehrK1Lv2cPMxUtHkvSNNtmgnatSJdmxfzy8gc/edit?usp=sharing" target="_blank" style="
                background-color: #4CAF50;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 8px;
                font-size: 17px;
            ">
                Acessar Proposta
            </a>
        </div>
	<br>
	<p style="color:#2F4F2F; text-align: center;">
            (Para acessar utilize o e-mail institucional)
        </p>
    </div>
    """, unsafe_allow_html=True)


with abas[4]:
    st.markdown("### Cronograma e Custos do Projeto")
    st.markdown("""
    <p style="text-align: justify;">
    Nesta seção, está disponibilizado o cronograma completo juntamente com os custos previstos e realizados do projeto <b><span style="color:#DC143C;">BioMove</span></b>.
    
    Você pode acessar o documento completo clicando no botão abaixo:
    </p>
    """, unsafe_allow_html=True)

    # Link bonito (exemplo de link)
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


