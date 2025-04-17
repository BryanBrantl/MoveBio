import streamlit as st

# 🔥 Definir configurações da página
st.set_page_config(page_title="Projeto de Oficina", layout="wide")

# 🔥 Estilo personalizado com CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .main-content {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
            color: #ffffff;
        }
        h1, h2 {
            text-align: center;
            font-weight: bold;
            color: #ffffff;
        }
        h1 { font-size: 42px; }
        h2 { font-size: 32px; margin-top: 20px; }
        p, li {
            font-size: 18px;
            line-height: 1.6;
            color: #bbbbbb;
        }
        .nav-bar {
            display: flex;
            justify-content: space-around;
            background-color: #1e1e1e;
            padding: 10px;
            border-radius: 8px;
        }
        .nav-item {
            padding: 10px 20px;
            border-radius: 8px;
            color: #ffffff;
            text-decoration: none;
            font-weight: bold;
        }
        .nav-item:hover {
            background-color: #333;
        }
        .nav-active {
            background-color: #ff4b4b;
            color: white;
        }
        .info-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
            margin-top: 20px;
            color: #ffffff;
        }
        .info-box h2 {
            color: #ff4b4b;
            font-size: 28px;
        }
        .info-box p {
            color: #bbbbbb;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Criação das abas
tabs = st.tabs(["Home", "Projetos", "Cronograma", "Atualização Semanal", "Materiais e Métodos", "Análise de Riscos"])

# ✅ ABA HOME
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bem-vindo(a) ao Projeto de Oficina!</h1>", unsafe_allow_html=True)
    
    # Container para as 4 imagens
    colunas = st.columns(4)
    nomes = ["Bryan A. L. Brantl", "Joao R. Klassen", "Leonardo Amancio", "Luiz Prado Oliveira"]
    periodos = ["5º", "7º", "6º", "7º"]
    emails = ["bryan.brantl@email.com", "joao.klassen@email.com", "leonardo.amancio@email.com", "luiz.oliveira@email.com"]
    telefones = ["(31) 98765-4321", "(31) 91234-5678", "(31) 99876-5432", "(31) 92345-6789"]
    imagens = ["image/foto_01.png", "image/foto_02.png", "image/foto_03.png", "image/foto_04.png"]

    for i, col in enumerate(colunas):
        with col:
            st.image(imagens[i], width=500)  # 🔥 Imagem maior
            st.markdown(f"""
                <div style='text-align: center;'>
                    <p><b style='color: #ffffff; font-size: 18px;'>{nomes[i]}</b></p>
                    <p style='color: #bbbbbb; font-size: 16px;'>Engenharia Eletrônica - {periodos[i]} Período</p>
                    <p style='color: #bbbbbb; font-size: 14px;'>{emails[i]}</p>
                    <p style='color: #bbbbbb; font-size: 14px;'>{telefones[i]}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # 🔥 Bloco de informações com contraste melhorado
    st.markdown("""
    <div style="
        background-color: #1e1e1e; 
        padding: 20px; 
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        margin-top: 20px;
    ">
        <h2 style="color: #ffffff;">O Processo de Criação</h2>
        <p style="color: #bbbbbb;">Desenvolvido com Streamlit e integrado ao GitHub para versionamento e colaboração. Interface estilizada com HTML/CSS personalizados.</p>
    </div>
    """, unsafe_allow_html=True)



# ✅ ABA PROJETOS
with tabs[1]:
    st.markdown("""
    <div class="main-content">
        <h2>Projetos</h2>
        <h3 style="color: #ff4b4b;">Proposta 01: Monitoramento Remoto de Saúde</h3>
        <p><b style="color: #ffffff;">Problema:</b> Em regiões afastadas, o acesso a serviços médicos é limitado. Pacientes crônicos precisam de acompanhamento constante.</p>
        <p><b style="color: #ffffff;">Solução:</b> Dispositivo vestível monitora sinais vitais (oxigenação, batimentos cardíacos, temperatura) e transmite via LoRa/GSM/WiFi para centros de saúde.</p>
        <h3 style="color: #ff4b4b;">Integração</h3>
        <ul>
            <li><b style="color: #ffffff;">Eletrônica:</b> Sensores biomédicos e circuito de aquisição de sinais.</li>
            <li><b style="color: #ffffff;">Eletrônica Digital:</b> Processamento de dados e envio de alertas.</li>
            <li><b style="color: #ffffff;">Microcontroladores:</b> ESP32 ou STM32 para comunicação remota.</li>
            <li><b style="color: #ffffff;">Computação:</b> Plataforma Web/App para monitoramento.</li>
        </ul>
        <h3 style="color: #ff4b4b;">Proposta 2</h3>
        <h3 style="color: #ff4b4b;">Proposta 3</h3>
    </div>
    """, unsafe_allow_html=True)

# ✅ ABA MATERIAIS E MÉTODOS
with tabs[4]:
    st.markdown("""
    <div class="main-content">
        <h2>Materiais e Métodos</h2>
        <ul>
            <li>ESP32</li>
            <li>Display TFT 1.28" (GC9A01)</li>
            <li>Sensores</li>
            <li>Módulos de comunicação sem fio</li>
        </ul>
        <p><b>Métodos:</b> Programação em C/C++, uso de bibliotecas específicas para ESP32 e comunicação SPI.</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ ABA ANÁLISE DE RISCOS
with tabs[5]:
    st.markdown("""
    <div class="main-content">
        <h2>Análise de Riscos</h2>
        <h3>Riscos Técnicos</h3>
        <ul>
            <li>Falha na comunicação com sensores.</li>
            <li>Problemas de compatibilidade com bibliotecas.</li>
        </ul>
        <h3>Riscos de Projeto</h3>
        <ul>
            <li>Atrasos no cronograma.</li>
            <li>Falta de componentes críticos.</li>
        </ul>
        <p><b>Mitigação:</b> Testes antecipados, backup de componentes e revisões semanais.</p>
    </div>
    """, unsafe_allow_html=True)
