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
        st.image("image/emg1.png", width=450)
        st.markdown("Ação de gamificação promovida no Instituto Albert Einstein")
    with col2:
        st.markdown("### 1. Problemática e Objetivo")
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
        st.markdown("### 2. Proposta e Escopo")
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
        st.image("image/emg2.png", width=400)
        st.markdown("Imagem ilustrativa da Proposta")

    st.markdown("---")

    # ✅ Cronograma e Entregáveis
    col5, col6 = st.columns([1, 2], gap="large")
    with col5:
        st.image("image/emg3.png", width=350)
        st.markdown("Imagem ilustrativa das direções do carrinho")
    with col6:
        st.markdown("### 3. Cronograma e Entregáveis")
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
        # === Atualização Semanal #4  ===
    st.markdown(f"""
    <div style="background-color:#1C1C1C; padding:15px; border-radius:10px;">
        <h4 style="color:#DC143C;">#4 - Atualização Semanal - 30/05/2025</h4>
        <ul style="color:#FFFFFF;">
            <li>
	    	Nesta semana, avançamos na produção da placa de circuito impresso (PCI) para o nosso projeto. Reproduzimos o modelo utilizando novamente o filtro notch para testes. No entanto, enfrentamos alguns contratempos que impactaram o andamento do cronograma.
     	    	Durante a etapa de montagem e teste da placa, identificamos problemas relacionados ao roteamento do circuito e à soldagem de alguns componentes. Esses erros comprometeram o funcionamento esperado da PCI, impossibilitando a continuidade dos testes nesta fase.
	    	Estamos trabalhando na correção do layout e no aprimoramento do processo de soldagem para evitar recorrência desses problemas nas próximas versões.
     	    </li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_exemplo_atualizacao2.png", width=200) -->
            <img src="data:image/png;base64,{base64.b64encode(open('image/emg4.jpg','rb').read()).decode('utf-8')}"
                 style="width: 600px; height: 500px; border-radius: 10px; object-fit: cover;"
                 alt="Circuito montado">
        </div> 
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
	
        # === Atualização Semanal #3  ===
    st.markdown(f"""
    <div style="background-color:#1C1C1C; padding:15px; border-radius:10px;">
        <h4 style="color:#DC143C;">#3 - Atualização Semanal - 23/05/2025</h4>
        <ul style="color:#FFFFFF;">
            <li>Finalizado a montagem do carrinho.</li>
            <li>Adição de novos filtros no esquemático do EMG.</li>
            <li>Montagem do circuito EMG em placa perfurada para melhorar os testes quando comparado a protoboard.</li>
            <li>Filtro Notch não apresentou resultado esperado, levantado a hipótese de utilizar filtros digitais
				para melhorar a performance.</li>
            <li>Circuito montado em placa perfurada:</li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_exemplo_atualizacao2.png", width=200) -->
            <img src="data:image/png;base64,{base64.b64encode(open('image/emg4.jpg','rb').read()).decode('utf-8')}"
                 style="width: 600px; height: 500px; border-radius: 10px; object-fit: cover;"
                 alt="Circuito montado">
        </div> 
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)


    # === Atualização Semanal #2 ===
    st.markdown(f"""
    <div style="background-color:#1C1C1C; padding:15px; border-radius:10px;">
        <h4 style="color:#DC143C;">#2 - Atualização Semanal - 16/05/2025</h4>
        <ul style="color:#FFFFFF;">
            <li>Definido a utilização de um Kit chassi para a construção do carrinho.</li>
            <li>Montagem do sensor EMG em protoboard baseado no esquemático da semana anterior.</li>
            <li>Validamos o sinal no osciloscópio, detectado presença de ruído da rede.</li>
            <li>Definido a necessidade de implementar mais filtros no circuito para reduzir o ruído.</li>
            <li>Circuito montado em protoboard:</li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_exemplo_atualizacao2.png", width=200) -->
            <img src="data:image/png;base64,{base64.b64encode(open('image/Protoboard.jpg','rb').read()).decode('utf-8')}"
                 style="width: 600px; height: 225px; border-radius: 10px; object-fit: cover;"
                 alt="Circuito montado">
        </div>
        <ul style="color:#FFFFFF;">
            <li>Sinal no osciloscópio:</li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_exemplo_atualizacao3.png", width=200) -->
            <img src="data:image/png;base64,{base64.b64encode(open('image/Osciloscopio_Protoboard.jpg','rb').read()).decode('utf-8')}"
                 style="width: 600px; height: 400px; border-radius: 10px; object-fit: cover;"
                 alt="Sinal gerado">
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

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
            <li>Construção do esquemático EMG:</li>
        </ul>
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <!-- st.image("caminho/para/imagem_simulacao_emg.gif", width=200) -->
            <img src="data:image/png;base64,{base64.b64encode(open('image/ESQUEMATICO_Semana1.JPG','rb').read()).decode('utf-8')}"
                 style="width: 660px; height: 300px; border-radius: 10px; object-fit: cover;"
                 alt="Exemplo atualização 2">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # === Atualização Semanal #2 (Exemplos para alterar depois) ===

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
