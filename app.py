import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from pathlib import Path

st.set_page_config(page_title="BIOMOVE", layout="wide")

########################################################### Título principal ##########################################################
st.markdown("<h1 style='color:white;'>BIOMOVE</h1>", unsafe_allow_html=True)

# Menu horizontal com abas
selected = option_menu(
    menu_title=None,
    options=["Home", "BioMove", "Atualização Semanal", "Relatórios", "Custos e Cronograma"],
    orientation="horizontal",
    default_index=0,
    icons=["house", "bar-chart", "calendar", "file-earmark-text", "clock"],
    styles={
        "container": {"padding": "0!important", "background-color": "#0E1117"},
        "icon": {"color": "white", "font-size": "16px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "white"},
        "nav-link-selected": {"background-color": "#0E1117", "color": "teal", "border-bottom": "2px solid teal"},
    }
)


############################################ IMAGENS ############################################
# Usando um bloco try-except para evitar que o app quebre se uma imagem não for encontrada
try:
    img1 = Image.open("imagem/foto_01.png")
    img2 = Image.open("imagem/foto_02.png")
    img3 = Image.open("imagem/foto_03.png")
    img4 = Image.open("imagem/foto_04.png")
    img5 = Image.open("imagem/gamificacao.jpg")
    img6 = Image.open("imagem/Musculo_0.png")
    img7 = Image.open("imagem/Musculo_1.png")
    img8 = Image.open("imagem/pcb1.png")
    img9 = Image.open("imagem/pcb2.jpg")	
    img10 = Image.open("imagem/pcb3.jpg")
    img11 = Image.open("imagem/sinal_emg1.png")
    img12 = Image.open("imagem/Diagrama_EMG.png")
    img13 = Image.open("imagem/Diagrama_Hardware_carrinho.png")
    img14 = Image.open("imagem/Esquematico_EMG.jpg")
    img15 = Image.open("imagem/ESQUEMATICO_Semana1.jpg")	
    img16 = Image.open("imagem/Protoboard.jpg")
    img17 = Image.open("imagem/Osciloscopio_Protoboard.jpg")	
    img18 = Image.open("imagem/Placa_Perfurada.jpg")
    
    img19 = Image.open("imagem/EMG1.jpg")
    img20 = Image.open("imagem/EMG2.jpg")
    img21 = Image.open("imagem/EMG3.jpg")
    img22 = Image.open("imagem/Notch_EMG.png")
    img23 = Image.open("imagem/ruido_EMG.png")
	
    img24 = Image.open("imagem/Caixa.jpg")	
    img25_r = Image.open("imagem/carrinho_final.jpg")
    img25 = img25_r.rotate(-90, expand=True)	
except FileNotFoundError:
    st.error("Uma ou mais imagens não foram encontradas. Verifique os caminhos dos arquivos.")
    # Atribui None para evitar mais erros
    img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18 = (None,)*18

video1 = "https://www.youtube.com/shorts/GlK9RndNrzY"
video2 = "https://youtube.com/shorts/xoU3nnxIE90"

proposta_url ="https://drive.google.com/file/d/1rYrxMrfTaIwfsUZtwLDXWOBLR937v-OY/view?usp=sharing"
relatorio_final_url ="https://drive.google.com/file/d/1le6f5-uIZGDcE8AVq8N2wSxk400Y54E8/view?usp=sharing"
cronograma_url = "https://drive.google.com/file/d/1dAj2meYaIEoVXa1U7aTqnkUymjawkRhC/view?usp=drive_link"
tabeladecusto_url ="https://drive.google.com/file/d/1DMyMVpQ_crz_cCb9aD9ab3RmOMVNSeU4/view?usp=sharing"

############################################ Conteúdo de acordo com o menu selecionado ############################################
################################################################################################   HOME    #################################
if selected == "Home" and all([img1, img2, img3, img4]):
    st.markdown("<h1 style='text-align: center; color: #008080;'> DEMONSTRAÇÃO DO PROJETO: BIOMOVE </h1>", unsafe_allow_html=True)
	
    st.markdown("""
    <div style="text-align: center;">
        <iframe width="640" height="360" 
        src="https://www.youtube.com/embed/MNt9wBUUIjA" 
        title="YouTube video" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #008080 ;'>MEMBROS</h1>", unsafe_allow_html=True)
    st.write("") # Espaço

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(img1, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'> Bryan Alexandre de Lima Brantl</span></strong><br><br>
                 RA: 2414139<br>
                 E-mail: brantl@alunos.utfpr.edu.br<br>
                 Contato: (41) 99278-3929
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.image(img2,width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>João Roberto Klassen</span></strong><br><br>
                RA: 2414155<br>
                E-mail: joaoklassen@alunos.utfpr.edu.br<br>
                Contato: (41) 99742-4536
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.image(img3, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Leonardo Amancio</span></strong><br><br>
                RA: 2402580<br>
                E-mail: leonardoamancio@alunos.utfpr.edu.br<br>
                Contato: (41) 99805-1279
            </div>
            """, unsafe_allow_html=True)
    
    with col4:
        st.image(img4, width=500)
        st.markdown(
            """
            <div style='text-align: center'>
                <strong><span style='color: #008080;'>Luiz Eduardo Prado de Oliveira</span></strong><br><br>
                RA: 2402629<br>
                E-mail: luizoliveira.2002@alunos.utfpr.edu.br<br>
                Contato: (41) 99815-6532
            </div>
            """, unsafe_allow_html=True)
######################################### ##################################################
######################################   BIOMOVE    ########################################

elif selected == "BioMove" and all([img5, img6, img7]):
    st.markdown("<h1 style='text-align: center; color: #008080;'>OVERVIEW DO PROJETO</h1>", unsafe_allow_html=True)
    st.divider()

    # Bloco 1
    B1col1, B1col2 = st.columns(2)
    with B1col1:
        vazia, img_col_b1, vazia2 = st.columns([1, 4, 1])
        with img_col_b1:
            st.image(img5)
    with B1col2:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Problemática e Objetivo</h2>
                <p>O projeto BioMove surge para <span style='text-decoration: underline; text-decoration-color: #008080;'>melhorar a interação do paciente com a fisioterapia</span>, tornando-a mais motivadora e eficaz, com objetivo de <span style='text-decoration: underline; text-decoration-color: #008080;'>acelerar o progresso de reabilitação</span>. Muitos pacientes desistem antes de alcançar melhora significativa devido a:</p>
                <ul>
                    <li>Métodos tradicionais repetitivos e pouco engajadores;</li>
                    <li>Dificuldade em perceber progresso imediato, causando desmotivação;</li>
                    <li>Falta de acesso a equipamentos modernos que estimulem o tratamento.</li>
                </ul>
                <p>A proposta central é <span style='text-decoration: underline; text-decoration-color: #008080;'>estabelecer uma base de gamificação</span> para o tratamento, inspirando-se em exemplos como o Instituto Albert Einstein, para tornar o processo mais dinâmico e envolvente.</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    B2col1, B2col2 = st.columns([2, 1.5])
    with B2col1:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Proposta e Escopo</h2>
                <p>O sistema BioMove utiliza <strong style='color: #008080;'>sensores EMG</strong> (montados a partir de amplificadores de instrumentação e filtros analógicos) para captar sinais musculares do paciente.</p>
                <p>Estes sinais são processados (amplificação, filtragem, retificação e análise digital) para serem transformados em comandos de controle de um carrinho autônomo.</p>
                <p>O projeto prioriza a qualidade do controle baseado em EMG, em vez de funcionalidades avançadas no robô, concentrando esforços na aquisição e interpretação dos sinais.</p>
            </div>
        """, unsafe_allow_html=True)
    with B2col2:
        vazia1, img_col, vazia2 = st.columns([1, 4, 1])
        with img_col:
            st.image(img6)
    
    st.divider()
    
    # Bloco 3
    B3col1, B3col2 = st.columns([1.5, 2])
    with B3col1:
        vazia3, img_col2, vazia4 = st.columns([1, 4, 1])
        with img_col2:
            st.image(img7)
    with B3col2:
        st.markdown("""
            <div style='text-align: justify;'>
                <h2 style='color: #008080; text-align: center;'>Funcionamento Básico</h2>
                <p>Eletrodos são posicionados em músculos-alvo (por exemplo, bíceps direito e esquerdo) para captar o sinal EMG e processá-lo, identificando a ativação muscular.</p>
                <p>Os sinais são traduzidos em comandos para mover o carrinho, conforme a lógica:</p>
                <ul>
                    <li><strong>Ambos músculos ativados:</strong> carrinho anda para frente.</li>
                    <li><strong>Somente esquerdo ativado:</strong> carrinho vira à direita.</li>
                    <li><strong>Somente direito ativado:</strong> carrinho vira à esquerda.</li>
                    <li><strong>Sem ativação:</strong> carrinho permanece parado.</li>
                </ul>
                <p>A comunicação entre o módulo EMG e o carrinho é feita via <strong style='color: #008080;'>Wi-Fi</strong> ou <strong style='color: #008080;'>Bluetooth</strong>, já que ambos os módulos rodam com um ESP32.</p>
            </div>
        """, unsafe_allow_html=True)
    
##########################################################################################
##########################   ATUALIZAÇÃO SEMANAL    ########################################

elif selected == "Atualização Semanal":
	####################################### ENTREGA INTEGRAÇÃO ############################
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	st.markdown("<h1 style='text-align: center; color: #008080;'>INTEGRAÇÃO - 04/06</h1>", unsafe_allow_html=True)
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	
	st.markdown("""
	<div style='text-align: justify; font-size: 16px;'>
	    <span style='color: #008080; font-weight: bold;'>OBS:</span> 
	    O funcionamento desta entrega está disponível na página 
	    <span style='color: #008080; font-weight: bold;'>HOME</span>, com o projeto já testado em sua totalidade, integrando as etapas de 
	    <span style='color: #008080; font-weight: bold;'>MECÂNICA</span>, 
	    <span style='color: #008080; font-weight: bold;'>SOFTWARE</span> e 
	    <span style='color: #008080; font-weight: bold;'>HARDWARE</span>.
	</div>
	""", unsafe_allow_html=True)
	st.divider()	
	st.write("") # Espaço
	
	st.markdown("""
	    <h3>Integração do Circuito Clamper</h3>
	    <div style='text-align: justify;'>
	        Durante a última etapa do projeto, foi integrado ao sistema o <b>Circuito Clamper</b>, com o objetivo de adicionar um <i>offset</i> ao sinal EMG, convertendo-o em um sinal de corrente contínua (DC).<br><br>
	        Essa modificação facilita o processamento digital do sinal, permitindo que o microcontrolador interprete corretamente os picos de ativação muscular.
	    </div>
	""", unsafe_allow_html=True)
	st.divider()	
	st.markdown("""
	    <h3>Comunicação entre Módulos ESP32</h3>
	    <div style='text-align: justify;'>
	        Foi implementado o sistema de comunicação entre os dois módulos <b>ESP32</b> utilizados no projeto. A troca de dados ocorre de forma eficiente por meio da comunicação serial utilizando o protocolo <b>ESP-NOW</b>.<br><br>
	        Esse protocolo permite baixa latência e comunicação direta entre os dispositivos, sem a necessidade de um roteador Wi-Fi intermediário.
	 
	    </div>
	""", unsafe_allow_html=True)
	st.divider()
	st.markdown("""
	    <h3>Mecânica do Projeto</h3>
	    <div style='text-align: justify;'>
     		A parte mecânica deste projeto foi planejada de forma simples e funcional. <br>
       		<ul>
			<li>Finalizado o funcionamento básico do carrinho, garantindo que ele respondesse adequadamente aos sinais EMG recebidos.<br>
	        	<li>Foi desenvolvido e impresso um compartimento físico para acomodar e proteger o circuito eletrônico, incluindo o <b>ESP32</b>, a fonte de alimentação e os demais componentes, assegurando praticidade e organização durante o uso.
	 	</ul>
	    </div>
	""", unsafe_allow_html=True)
	st.write("") # Espaço
	i1, i2 = st.columns(2)
	with i1:
		st.image(img24, caption="CAIXA FEITA EM IMPRESSÃO 3D",use_container_width=True)	
	with i2:
		st.image(img25, caption="CARRINHO",use_container_width=True)
	####################################### ENTREGA SOFTWARE ############################
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	st.markdown("<h1 style='text-align: center; color: #008080;'>ENTREGA SOFTWARE - 27/06</h1>", unsafe_allow_html=True)
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	#
	col1, col2 = st.columns(2)
	with col1:
	    st.image(img19, caption="STATECHART: SINAL EMG", use_container_width=True)
	with col2:
		st.markdown("""
		    <h3>Statechart do Sistema EMG</h3>
		    <div style='text-align: justify;'>
		        O sistema inicia realizando a leitura dos sinais dos canais <b>A</b> e <b>B</b>. Em seguida, aplica-se um filtro <i>notch</i> para remoção do ruído de 60 Hz. Após essa etapa, o sistema verifica se há conexão disponível com o carrinho.<br><br>
		        Caso a conexão esteja estabelecida, os dados são processados e convertidos em comandos apropriados, que são então enviados ao carrinho para controle dos movimentos.
		    </div>
		""", unsafe_allow_html=True)
	st.divider()	
	col3, col4 = st.columns(2)
	with col3:
	    st.image(img20, caption="STATECHART: MOVIMENTOS",use_container_width=True)
	with col4:
	    st.markdown("""
	        <h3>Statechart dos Movimentos</h3>
	        <div style='text-align: justify;'>
	            Representa as possíveis movimentações do sistema e as transições entre elas, de acordo com os comandos detectados.<br><br>
	            Os principais estados envolvem deslocamentos para frente, para os lados ou parada total, dependendo do tipo de estímulo recebido do sistema de leitura EMG.
	        </div>
	    """, unsafe_allow_html=True)
	st.divider()	
	col5, col6 = st.columns(2)
	with col5:
	    st.image(img21, caption="STATECHART: COMPORTAMENTO DO CARRINHO",use_container_width=True)
	with col6:
	    st.markdown("""
	        <h3>Statechart do Carrinho</h3>
	        <div style='text-align: justify;'>
	            Mostra o comportamento do carrinho ao receber os comandos. Após a inicialização, o carrinho permanece parado até que seja estabelecida a conexão com o sistema de leitura EMG.<br><br>
	            Uma vez conectado, ele interpreta o tipo de sinal recebido para decidir a ação a ser tomada: mover para a esquerda, direita, avançar ou parar. Essa decisão é baseada nos dados recebidos do módulo EMG.
	        </div>
	    """, unsafe_allow_html=True)
	st.divider()
	

	####################################### entrega e validação ############################
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	st.markdown("<h1 style='text-align: center; color: #008080;'>ENTREGA E VALIDAÇÃO DO HARDWARE - 06/06</h1>", unsafe_allow_html=True)
	st.markdown(
	    """
	    <hr style="border: 2px solid #008080; border-radius: 2px;">
	    """,
	    unsafe_allow_html=True
	)
	#######################################################################################
	A0_col1, A0_col2, A0_col3 = st.columns([1, 0.05, 3])
	with A0_col1:
		st.image(img11, caption="Trecho do vídeo - Circuito EMG", use_container_width=True)
		st.link_button("▶", video1, use_container_width=True)
	with A0_col3:
		st.markdown("""
		    <div style='text-align: justify;'>
		        <h3>Demonstração do Circuito EMG e Próximos Passos no Tratamento de Ruído:</h3>
		        <ul>
		            <li>A equipe realizou uma demonstração do funcionamento do circuito EMG.</li>
		            <li>O vídeo com essa demonstração foi postado no YouTube.</li>
		            <li>Conforme planejado nas semanas anteriores, a equipe decidiu tratar a interferência do ruído via software, através da implementação de um filtro digital, que será desenvolvido nas próximas semanas.</li>
		        </ul>
		    </div>
		""", unsafe_allow_html=True)
	#########	
	st.subheader("Produção da Nova Versão da Placa de Circuito Impresso (PCI)")
	A0_col3_2, A0_col4, A0_col5 = st.columns([1, 2, 1])
	with A0_col3_2:
		st.image(img9, caption="PCI Soldada com Componentes",use_container_width=True)
	with A0_col4:
	        st.markdown("""
	            <div style='text-align: justify;'>
	                Na tentativa de reduzir significativamente o ruído, confeccionamos uma <span style='color: #008080;'>segunda e nova versão da Placa de Circuito Impresso</span>. Esta versão apresenta um <span style='color: #008080;'>roteamento otimizado e diferente</span>, com a implementação de um <span style='color: #008080;'>plano terra</span>, visando aprimorar a performance e reduzir interferências.
	                <br><br>
	                As imagens ao lado ilustram este progresso: à esquerda, temos a PCI já soldada com seus componentes, pronta para uso; e à direita, a visualização do layout da PCB no KiCad, detalhando o novo roteamento.
	            </div>
	        """, unsafe_allow_html=True)
	with A0_col5:
		st.image(img10, caption="Layout da PCI no KiCad", width=400)
	###########	
	
	A0_col6_1, A0_col6_2 = st.columns(2)
	with A0_col6_1:
		st.markdown("""
  			<h3>Descritivo de Hardware do Carrinho</h3>
		    <div style='text-align: justify;'>
		        O sistema do carrinho é composto por um <span style='color: #008080;'>ESP-32</span>, responsável pelo controle, enviando sinais de comando para a <span style='color: #008080;'>ponte H L298N</span>, que atua como driver dos dois motores DC (esquerdo e direito). Ambos os módulos (ESP-32 e L298N) são alimentados por uma única fonte de alimentação, que fornece energia tanto para o funcionamento do sistema quanto para a tração dos motores.
		    </div>
		""", unsafe_allow_html=True)
	with A0_col6_2:
		st.markdown("<br><br>", unsafe_allow_html=True)
		st.image(img12, caption="Diagrama de Hardware EMG", use_container_width=True)

	A0_col7_1, A0_col7_2 = st.columns(2)
	with A0_col7_1:
		st.markdown("<br><br>", unsafe_allow_html=True)
		st.image(img13, caption="Diagrama de Hardware do Carrinho", use_container_width=True)
	with A0_col7_2:
		st.markdown("""
  			<h3>Descritivo de Hardware do EMG</h3>
		    <div style='text-align: justify;'>
		        O diagrama de blocos representa um sistema de aquisição de sinais EMG. O sinal é captado por eletrodos, amplificado na etapa de pré-amplificação, e então filtrado por um filtro passa-faixa de 20 a 500 Hz. Após o condicionamento final do sinal, ele é enviado ao microcontrolador ESP32 por uma porta ADC para processamento.
		    </div>
		""", unsafe_allow_html=True)

	st.subheader("Esquemático do Circuito EMG Apresentado")
	st.markdown("""
	    <div style='text-align: justify;'>
	        Esquemático apresentado no entregavel de hardware:
	    </div>
	""", unsafe_allow_html=True)
	st.image(img14, caption="Esquemático Eletrônico Detalhado", use_container_width=True)
	st.divider()
	

########################### atualizacao 4 ##########################################################3
	
	st.markdown("""
	    <h2 style='color: #008080; text-align: center;'> #4 - Atualização Semanal - 30/05/2025 </h2>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Desafios na Produção da Placa de Circuito Impresso (PCI):</h3>
	        <ul>
	            <li>Avançamos na produção da placa de circuito impresso (PCI) para o projeto, reproduzindo o modelo com o filtro notch para testes.</li>
	            <li>Enfrentamos contratempos significativos durante a montagem e teste da placa, identificando problemas no roteamento do circuito e na soldagem de componentes.</li>
	            <li>Esses erros comprometeram o funcionamento da PCI, impossibilitando a continuidade dos testes nesta fase.</li>
	            <li>Estamos trabalhando na correção do layout e no aprimoramento do processo de soldagem para evitar recorrências.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Desenvolvimento do Sistema de Controle do Carrinho:</h3>
	        <ul>
	            <li>Conforme informado na semana passada, a montagem do carrinho foi finalizada.</li>
	            <li>Nesta semana, a equipe desenvolveu o software que permite controlar o carrinho por meio de um joystick no celular, utilizando conexão via Bluetooth.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Demonstração do Controle do Carrinho:</h3>
	        <ul>
	            <li>Foi adicionado um vídeo no YouTube demonstrando o funcionamento básico do carrinho via controle Bluetooth.</li>
	            <li>Para visualizar, clique no botão abaixo.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	st.link_button("▶", video1, type="secondary")
	
	st.divider()
#####################################################################################################		
	#semana3
	st.markdown("""
	    <h2 style='color: #008080; text-align: center;'> #3 - Atualização Semanal - 23/05/2025 </h2>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Montagem do Carrinho e Otimização do Circuito EMG:</h3>
	        <ul>
	            <li>Finalizada a montagem do carrinho.</li>
	            <li>Adição de novos filtros no esquemático do EMG.</li>
	            <li>Montagem do circuito EMG em placa perfurada para melhorar os testes quando comparado a protoboard.</li>
	            <li>O filtro Notch não apresentou o resultado esperado, levantando a hipótese de utilizar filtros digitais para melhorar a performance.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Circuito EMG em Placa Perfurada:</h3>
	        <ul>
	            <li>Circuito montado em placa perfurada:</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	st.image(img18, caption="Circuito do sensor EMG montado em placa perfurada.")
#####################################################################################################
	#semana2
	st.markdown("""
	    <h2 style='color: #008080; text-align: center;'> #2 - Atualização Semanal - 16/05/2025 </h2>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Desenvolvimento e Validação do Circuito EMG:</h3>
	        <ul>
	            <li>Definida a utilização de um Kit chassi para a construção do carrinho.</li>
	            <li>Montagem do sensor EMG em protoboard baseado no esquemático da semana anterior.</li>
	            <li>Validamos o sinal no osciloscópio, detectando presença de ruído da rede.</li>
	            <li>Definida a necessidade de implementar mais filtros no circuito para reduzir o ruído.</li>
	        </ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.subheader("Detalhes do Circuito e Sinal:")
	A4_col1, A4_col2 = st.columns(2)
	with A4_col1:
		st.markdown("""
		    <div style='text-align: justify;'>
		        <ul>
		            <li>Circuito montado em protoboard:</li>
		        </ul>
		    </div>
		""", unsafe_allow_html=True)
		st.image(img16, caption="Circuito montado em protoboard")
	with A4_col2:
		st.markdown("""
		    <div style='text-align: justify;'>
		        <ul>
		            <li>Sinal no osciloscópio:</li>
		        </ul>
		    </div>
		""", unsafe_allow_html=True)
		st.image(img17, caption="Sinal do sensor EMG capturado no osciloscópio", width = 480)
	st.divider()
#####################################################################################################
	#semana1
	st.markdown("""
 		<h2 style='color: #008080; text-align: center;'> #1 - Atualização Semanal - 09/05/2025 </h2>
 	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
		 <h3>Progresso e Decisões Iniciais do Projeto:</h3>
		<ul>
			<li>Realizados testes nos principais componentes do carrinho (motor DC, ESP32 e ponte H), sem identificação de defeitos.</li>
			<li>Conduzido estudo sobre softwares de modelagem 3D. Optou-se pela utilização do Eagle para o desenvolvimento do carrinho e do sistema EMG.</li>
			<li>Modelo do site finalizado.</li>
			<li>Proposta e cronograma revisados e atualizados conforme a devolutiva, já disponíveis no site.</li>
		<ul>
	    </div>
	""", unsafe_allow_html=True)
	
	st.markdown("""
	    <div style='text-align: justify;'>
	        <h3>Decisões sobre o projeto:</h3>
	        <ul>
	            <li>Definido que serão utilizadas baterias 18650 (4.2V) para alimentação dos sistemas.</li>
	        </ul>
	        <h3>Construção do esquemático EMG:</h3>
	    </div>
	""", unsafe_allow_html=True)
	st.image(img15)
	st.divider()
############################################################################################
###################################   RELATORIO    ########################################
elif selected == "Relatórios":
	def bloco_informacao(titulo_bloco, texto_descricao, texto_botao, url_botao):
	    st.markdown(f"""
	        <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
	            <h4 style="color:white; margin-top:0;">{titulo_bloco}</h4>
	            <p style="color:gray; font-size:16px;">{texto_descricao}</p>
	            <div style="margin-top: 15px; text-align: center;"> 
	                <a href="{url_botao}" target="_blank" style="
	                    text-decoration: none; 
	                    display: inline-block; 
	                    padding: 10px 20px; 
	                    background-color: #008080; 
	                    color: white; 
	                    border-radius: 5px; 
	                    text-align: center; 
	                    cursor: pointer;
	                    font-weight: bold;
	                    transition: background-color 0.3s ease;
	                ">
	                    {texto_botao}
	                </a>
	            </div>
	        </div>
	    """, unsafe_allow_html=True)
	
	# Título principal da seção de RELATÓRIOS
	st.markdown("<h1 style='text-align: center; color: #008080;'>RELATÓRIOS</h1>", unsafe_allow_html=True)
	
	# Bloco para a Proposta do Projeto
	bloco_informacao(
	    titulo_bloco="Proposta do Projeto",
	    texto_descricao="Nesta seção, está disponibilizada a proposta de projeto do BioMove. O documento reúne informações detalhadas sobre o escopo do projeto, sendo esta proposta já aprovada.",
	    texto_botao="ACESSAR PROPOSTA",
	    url_botao=proposta_url
	)
 
	# Bloco para o Relatório Final do Projeto
	bloco_informacao(
	    titulo_bloco="Relatório Final do Projeto",
	    texto_descricao="O relatório final do projeto BioMove, contendo todos os resultados, análises e conclusões, também pode ser acessado através do botão abaixo:",
	    texto_botao="ACESSAR RELATÓRIO FINAL",
	    url_botao=relatorio_final_url
	)
	st.markdown("<h1 style='text-align: center; color: #008080;'> VÍDEO FINAL </h1>", unsafe_allow_html=True)

	st.markdown("""
	<div style="text-align: center;">
	    <iframe width="640" height="360"
	    src="https://www.youtube.com/embed/eqlHAxxmIHE"
	    frameborder="0" allowfullscreen></iframe>
	</div>
	""", unsafe_allow_html=True)
############################################################################################
###################################   CRONOGRAMA    ########################################
elif selected == "Custos e Cronograma":
	def bloco_informacao(titulo_bloco, texto_descricao, texto_botao, url_botao):
	    st.markdown(f"""
	        <div style="background-color:#1e1e1e; padding:20px; margin-bottom:10px; border-radius:10px; border-left: 5px solid teal;">
	            <h4 style="color:white; margin-top:0;">{titulo_bloco}</h4>
	            <p style="color:gray; font-size:16px;">{texto_descricao}</p>
	            <div style="margin-top: 15px; text-align: center;"> 
	                <a href="{url_botao}" target="_blank" style="
	                    text-decoration: none; 
	                    display: inline-block; 
	                    padding: 10px 20px; 
	                    background-color: #008080; 
	                    color: white; 
	                    border-radius: 5px; 
	                    text-align: center; 
	                    cursor: pointer;
	                    font-weight: bold;
	                    transition: background-color 0.3s ease;
	                ">
	                    {texto_botao}
	                </a>
	            </div>
	        </div>
	    """, unsafe_allow_html=True)
     
	bloco_informacao(
	    titulo_bloco="Cronograma Detalhado",
	    texto_descricao="Acesse a planilha detalhada com todas as fases, tarefas e prazos do projeto BioMove.",
	    texto_botao="ABRIR CRONOGRAMA",
	    url_botao=cronograma_url
	)

 	 	# Bloco para a tabela de custos
	bloco_informacao(
	    titulo_bloco="Tabela de Custos",
	    texto_descricao="O relatório final do projeto BioMove, contendo todos os resultados, análises e conclusões, também pode ser acessado através do botão abaixo:",
	    texto_botao="ACESSAR TABELA DE CUSTOS",
	    url_botao=tabeladecusto_url
	) 
# Rodapé
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0E1117;
            color: #888888;
            text-align: center;
            padding: 10px;
            font-size: 15px;
            border-top: 1px solid #262730;
        }
    </style>
    <div class="footer">
        UTFPR - Universidade Tecnológica Federal do Paraná - Engenharia Eletrônica - 2025
    </div>
""", unsafe_allow_html=True)
