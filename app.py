import streamlit as st
import base64

st.set_page_config(page_title="Projeto - BioMove", layout="wide")

# Título ou seção principal
st.markdown("## BIOMOVE")
abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

# -------- HOME --------
with abas[0]:
    # Título principal
    st.markdown("""<h1>Home</h1>""", unsafe_allow_html=True)

    # Descrição do site logo abaixo do título
    st.markdown("""
        <p style='font-size:18px;'>
            Este site é dedicado às informações e atualizações do desenvolvimento do projeto <strong>BioMove</strong>.
        </p>
    """, unsafe_allow_html=True)

    # Texto adicional abaixo da descrição
    st.markdown("""
        <p style='font-size:16px; color:gray;'>
            Abaixo você encontrará os integrantes do projeto, suas informações de contato e matrícula.
        </p>
    """, unsafe_allow_html=True)

    # Novo título para a seção de membros
    st.markdown("""<h2>Membros</h2>""", unsafe_allow_html=True)

    # 👤 Perfis dos integrantes com imagens personalizadas
    colunas = st.columns(4)
    fotos = [
        "image/foto_01.png",
        "image/foto_02.png",
        "image/foto_03.png",
        "image/foto_04.png"
    ]
    nomes = [
        ("Bryan Alexandre de Lima Brantl", "2414139", "brantl@alunos.utfpr.edu.br", "(41) 99278-3929"),
        ("João Roberto Klassen",         "2414155", "joaoklassen@alunos.utfpr.edu.br", "41 99742-4536"),
        ("Leonardo Amancio",             "2402580", "leonardoamancio@alunos.utfpr.edu.br", "41 99805-1279"),
        ("Luiz Prado",                   "2402629", "luizoliveira.2002@alunos.utfpr.edu.br", "41 99815-6532")
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

# -------- BIOMOVE (Overview do Projeto) --------
with abas[1]:
    # Título da seção Overview
    st.markdown("""<h1 style='text-align: center; color: #6A0DAD;'>Overview do Projeto BioMove</h1>""", unsafe_allow_html=True)

    # ▶️ Placeholder de vídeo introdutório
    st.markdown("<!-- Aqui será inserido um vídeo introdutório futuramente -->")
    st.markdown("<p style='text-align: center; font-style: italic; color: gray;'>[Vídeo introdutório do projeto]</p>", unsafe_allow_html=True)

    st.markdown("---")

    # 📋 Problemática e Objetivo
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        # st.image("caminho/para/imagem_problemática.png", width=150)
        st.markdown("<!-- Imagem ilustrativa da Problemática -->")
    with col2:
        st.markdown("### 📋 Problemática e Objetivo")
        st.write("""
        O projeto **BioMove** surge para **melhorar a interação do paciente com a fisioterapia**, tornando-a
        mais motivadora e eficaz, com objetivo de acelerar o progresso de reabilitação. Muitos pacientes
        desistem antes de alcançar melhora significativa devido a:
        - Métodos tradicionais repetitivos e pouco engajadores;
        - Dificuldade em perceber progresso imediato, causando desmotivação;
        - Falta de acesso a equipamentos modernos que estimulem o tratamento.
        
        A proposta central é **estabelecer uma base de gamificação** para o tratamento, inspirando-se em
        exemplos como o Instituto Albert Einstein, para tornar o processo mais **dinâmico** e **envolvente**.
        """)

    st.markdown("---")

    # 📑 Proposta e Escopo
    col3, col4 = st.columns([2, 1], gap="large")
    with col3:
        st.markdown("### 📑 Proposta e Escopo")
        st.write("""
        - O sistema **BioMove** utiliza **sensores EMG caseiros** (montados a partir de amplificadores de
          instrumentação e filtros analógicos) para captar sinais musculares do paciente.
        - Estes sinais são processados (amplificação, filtragem, retificação e análise digital) para
          serem transformados em comandos de controle de um carrinho autônomo.
        - O projeto prioriza a qualidade do controle baseado em EMG, em vez de funcionalidades avançadas
          no robô, concentrando esforços na aquisição e interpretação dos sinais.

        **Funcionamento Básico**:
        1. Eletrodos posicionados em músculos-alvo (bíceps direito e esquerdo).
        2. Captação do sinal EMG e processamento para identificar ativação muscular.
        3. Tradução em comandos para mover o carrinho:
           - Ambos músculos ativados → carrinho anda para frente.
           - Somente esquerdo ativado → carrinho vira à direita.
           - Somente direito ativado → carrinho vira à esquerda.
           - Sem ativação → carrinho parado.
        4. Comunicação entre módulo EMG e carrinho via **Wi-Fi** ou **Bluetooth** (ambos rodando ESP32).

        **Diagrama em Blocos**:
        - Módulo EMG (ESP32) → Capta, processa e envia sinais → Módulo Carrinho (ESP32) → Aciona motores DC.
        """)
    with col4:
        # st.image("caminho/para/imagem_proposta.png", width=150)
        st.markdown("<!-- Imagem ilustrativa da Proposta e Diagrama em Blocos -->")

    st.markdown("---")

    # ✅ Cronograma e Entregáveis
    col5, col6 = st.columns([1, 2], gap="large")
    with col5:
        # st.image("caminho/para/imagem_cronograma.png", width=150)
        st.markdown("<!-- Imagem ilustrativa do Cronograma e das Tarefas -->")
    with col6:
        st.markdown("### ✅ Cronograma e Entregáveis")
        st.write("""
        **Principais Entregáveis e Prazos**:
        1. **Plano de Projeto (Proposta)**: 11/04/2025
        2. **Blog do Projeto (Link Inicial)**: 11/04/2025
        3. **Projeto e Testes de Hardware**: 23/05/2025
        4. **Projeto e Testes de Software**: 04/07/2025
           - Relatório final, vídeo demonstrativo e blog atualizados.
        5. **Integração, Testes Funcionais e Demonstração**: 11/07/2025 (apresentação à banca)

        **Resumo do Cronograma**:
        - Abril a Maio: Desenvolvimento do módulo EMG (projeto da PCB, amplificação e filtragem do sinal).
        - Maio a Junho: Integração com carrinho (configuração da ponte H, motores DC, chassi em MDF/3D).
        - Julho: Testes finais, ajustes no controle via sinais EMG e gamificação do ambiente de fisioterapia.

        **Análise de Riscos**:
        - **Leitura/Calibração do Sinal EMG**: Pode haver ruído; mitigar com filtros adequados.
        - **Tempo de Resposta do Carrinho**: Otimizar frequência de leitura e processamento.
        - **Queima de Componentes**: Testes em bancada e estoque de peças sobressalentes.
        - **Problemas com Baterias**: Testar autonomia e escolher fonte adequada.

        **Custos Estimados**:
        - **Sistema do Módulo EMG**: R$ 193,74 (ESP32, PCB, componentes analógicos, eletrodos, bateria, etc.).
        - **Sistema do Carrinho**: R$ 173,00 (ESP32, motores DC, ponte H, chassi, bateria, etc.).
        """)
    st.markdown("---")

    # Footer dentro da aba BioMove (opcional)
    st.markdown("<p style='text-align: center; color: gray;'>UTFPR Curitiba • Engenharia Eletrônica • 2025</p>", unsafe_allow_html=True)

# -------- ATUALIZAÇÃO SEMANAL --------
with abas[2]:
    # === Atualização Semanal #1 ===
    st.markdown(f"""
    <div style="background-color:#1C1C1C; padding:15px; border-radius:10px; margin-bottom: 20px;">
        <h4 style="color:#DC143C;">#1 - Atualização Semanal - 09/05/2025</h4>
        <ul style="color:#FFFFFF;">
            <li>Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.</li>
            <li>Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do <b>Eagle</b> para o desenvolvimento do carrinho e do sistema EMG.</li>
            <li>Modelo do site finalizado.</li>
            <li>Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.</li>
            <li>Decisões sobre o projeto: Definido que será utilizado baterias 18650 (4.2v) para alimentação dos sistemas.</li>
            <li>Simulação EMG em andamento.</li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_simulacao_emg.gif", width=200) -->
            <img src="data:image/gif;base64,{base64.b64encode(open('image/gif3.gif','rb').read()).decode('utf-8')}"
                 style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover;"
                 alt="GIF redondo">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # === Atualização Semanal #2 (Exemplos para alterar depois) ===
    st.markdown(f"""
    <div style="background-color:#1C1C1C; padding:15px; border-radius:10px;">
        <h4 style="color:#DC143C;">#2 - Atualização Semanal - 16/05/2025</h4>
        <ul style="color:#FFFFFF;">
            <li>Exemplo 1: Ajustar parâmetros de filtragem do sinal EMG (filtro passa-banda).</li>
            <li>Exemplo 2: Validar comunicação entre ESP32 do Módulo EMG e ESP32 do carrinho via Bluetooth.</li>
            <li>Exemplo 3: Construir protótipo inicial da PCB do sensor EMG e testar na bancada.</li>
            <li>Exemplo 4: Implementar controle proporcional de velocidade com base na intensidade do sinal.</li>
            <li>Exemplo 5: Definir layout do chassi em MDF e iniciar cortes ou impressão 3D.</li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_exemplo_atualizacao2.png", width=200) -->
            <img src="data:image/png;base64,{base64.b64encode(open('image/foto_03.png','rb').read()).decode('utf-8')}"
                 style="width: 200px; height: 200px; border-radius: 10px; object-fit: cover;"
                 alt="Exemplo atualização 2">
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------- RELATÓRIOS --------
with abas[3]:
    st.markdown("### Proposta de projeto")
    st.markdown(f"""
    <p style="text-align: justify;">
        Nesta seção, está disponibilizada a proposta de projeto do BioMove.
        O documento reúne informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.
    </p>
    <p style="text-align: justify;"> 
        Você pode acessar o documento completo clicando no botão abaixo:
    </p>
    """, unsafe_allow_html=True)

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
    <p style="text-align: center;">
        (Para acessar utilize o e-mail institucional)
    </p>
    """, unsafe_allow_html=True)

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
