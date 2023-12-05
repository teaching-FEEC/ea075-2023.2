# `Manta e sistema de controle de aquecimento para procedimentos hospitalares.`
# `Heating system for hospital procedures`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 |Guilherme Lehmann Concentino  | 173805  | Eng. Elétrica |
 |Pedro Henrique Moraes Dos Santos  | 243528 | Eng. Elétrica |

## Descrição do Projeto

Com o objetivo de promover uma significativa melhoria na qualidade de vida e na humanização do tratamento oferecido aos pacientes em ambientes hospitalares, desenvolvemos uma inovadora manta aquecedora para o controle preciso da temperatura.

Dentre os diversos procedimentos nos quais a manutenção contínua da temperatura se revela crucial, destacam-se: a necessidade de aquecimento prévio durante a transfusão de concentrado de hemácias, a fim de evitar coagulação; o suporte à analgesia da pele suprapúbica durante a inserção de um DIU; o aquecimento direto para recém-nascidos nos primeiros minutos de vida; e o condicionamento térmico de uma bolsa de ocitocina antes de sua infusão no pós-parto (período de grenberg). Adicionalmente, a consideração do conforto térmico do paciente é fundamental, uma vez que o frio presente em clínicas e hospitais, embora necessário, pode ser desagradável para muitos.

O produto em questão é composto por dois elementos essenciais: um controlador de aquecimento e uma malha resistiva, disponível em diferentes tamanhos. Destaca-se a versatilidade do controlador, que pode ser utilizado em malhas variando desde 20x20 cm até 2x1 m, proporcionando uma distribuição constante e eficaz do calor. O dispositivo opera com uma configuração pré-definida de 37,5 °C, mantendo o equilíbrio térmico, e está equipado com um termômetro que monitora a temperatura do paciente, quantificando a quantidade necessária de calor a ser transmitida.

Ademais, o produto oferece modos rápido e lento de aquecimento, proporcionando flexibilidade no tratamento. Além disso, apresenta a opção de alimentação por tomada elétrica ou bateria, garantindo praticidade e mobilidade em diferentes contextos hospitalares. Essas características tornam nossa manta aquecedora não apenas uma solução eficaz para os desafios térmicos em procedimentos médicos, mas também um instrumento versátil e adaptável às diversas necessidades clínicas.

## Descrição Funcional

O controle de temperatura é realizado por meio de um microcontrolador, permitindo ao operador configurar e monitorar a temperatura por meio de sensores especializados. Este inovador dispositivo apresenta uma série de características essenciais para garantir um tratamento térmico eficaz e seguro:

1. **Configuração Flexível de Temperatura:**
   - O equipamento oferece a conveniência de um pré-set inicial de temperatura em 37,5°C, facilitando a operação, mas permitindo ajustes conforme necessário.

2. **Modos de Aquecimento Rápido e Lento:**
   - Conta com dois modos de aquecimento distintos, um rápido e outro lento, proporcionando flexibilidade e adaptabilidade aos diferentes requisitos clínicos.

3. **Operação Silenciosa:**
   - Garante um ambiente tranquilo no ambiente hospitalar, evitando qualquer interferência sonora, assegurando conforto tanto para pacientes quanto para profissionais de saúde.

4. **Indicador de Temperatura do Paciente:**
   - Apresenta um indicador claro da temperatura do paciente, permitindo uma monitorização constante e eficaz do estado térmico.

5. **Sinalizador de Alerta:**
   - Incorpora um sinalizador que alerta a equipe no caso de o paciente não conseguir manter a temperatura adequada sem o dispositivo, garantindo intervenção rápida.

6. **Monitoramento Inteligente pós-Homeostase:**
   - Após atingir a homeostase, o dispositivo continua monitorando o paciente. Em caso de uma queda de temperatura fora da faixa adequada, reinicia automaticamente o aquecimento e notifica a equipe.

7. **Segurança contra Queimaduras:**
   - Trabalha na região de homeostase, mantendo uma temperatura uniforme que evita riscos de queimaduras aos pacientes.

8. **Mínimo Risco de Contaminação:**
   - No caso de contato direto com a pele, o dispositivo é projetado para oferecer o menor risco possível de contaminação, cumprindo rigorosos padrões de segurança.

9. **Autodesligamento e Sinalização de Problemas:**
   - Em situações adversas, o equipamento é capaz de se autodesligar e sinalizar o problema por meio de uma Interface Homem-Máquina (IHM), proporcionando segurança adicional.

10. **Métodos Não Invasivos e Toque Confortável:**
    - O dispositivo utiliza métodos não invasivos, garantindo conforto ao paciente, inclusive ao toque, sem comprometer a segurança ou eficácia do tratamento térmico.


### Funcionalidades

- O sistema apresenta capacidade para monitorar três diferentes temperaturas: a corporal do usuário, a ambiente e a interna do cobertor;

- Os usuários podem facilmente selecionar a temperatura desejada por meio de uma intuitiva interface com o operador;

- Monitoramento completo de todas as temperaturas é possível através da interface com o operador;

- O sistema oferece tanto opções de aquecimento lento quanto rápido;

- Inclusão de um timer para ajustar períodos específicos de aquecimento;

- Proteção contra superaquecimento integrada;

- Sinalizadores para situações de emergência, assegurando rápida intervenção;

- Indicador de nível de bateria para acompanhamento do status energético.


### Configurabilidade

O sistema permite a configuração da temperatura desejada entre o cobertor e o usuário, sendo adaptável a diferentes malhas de tamanhos distintos;

Compatibilidade com a rede elétrica convencional (AC) e a opção de operação por baterias.

### Eventos

O sistema é projetado para ler as temperaturas do ambiente e ajustar a corrente fornecida às resistências, manipulando assim a temperatura gerada pela malha térmica. O ciclo de operação do sistema segue a seguinte lógica:

1. O operador deve verificar qual forma de alimentação será utilizada, AC ou bateria.

2. Ligar a chave geral de operação do equipamento para ativá-lo.

3. Após a ativação, o microcontrolador detectará se a manta térmica está conectada a ele.

         - 3-A. Se a condição anterior for atendida, o sistema avançará para a próxima etapa; caso contrário, seguirá para o item 3-B.
        
         - 3-B. O controlador indicará a existência de um problema com a malha, permanecendo travado nessa condição até ser liberado pelo reset (liga e desliga geral do equipamento).

4. O controlador verificará se os sensores de temperatura estão conectados e prontos para operar; em caso contrário, ocorrerá a mesma situação descrita no item 3-B, indicando qual sensor apresenta problemas.

5. Com todas as condições atendidas, a Interface Homem-Máquina (IHM) é liberada para configuração.
    
       - 5-A. O controlador permite o ajuste da temperatura de aquecimento, iniciando por padrão em 37,5°C.
      
       - 5-B. Após o ajuste da temperatura, o operador pode escolher entre os modos de aquecimento rápido e lento.
      
       - 5-C. Por fim, o operador ajusta o tempo de operação.

6. Após a configuração, o operador inicia o ciclo de aquecimento pressionando o botão correspondente.

7. Durante o ciclo de aquecimento, o sistema atua com uma rotina inteligente de monitoramento do paciente e da temperatura. No entanto, algumas condições podem interromper o ciclo:

       - 7-A. Superaquecimento do paciente;
       
       - 7-B. Sobrecorrente no sistema;
       
       - 7-C. Detecção de fuga de corrente;
       
       - 7-D. Baixo ganho de temperatura.

8. Após a conclusão do ciclo de aquecimento, o controlador sinaliza que o processo foi finalizado, exibindo parâmetros como tempo médio de aquecimento.

9. O sistema permite a realização de um novo ciclo.


## Descrição Estrutural do Sistema

A partir da descrição funcional foi montado a primeira versão do fluxo de processo dos projetos indicando correlação e passagem de informações, além de mapear os processos.

![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/5921b9f8-3f4e-4447-9a88-d9aad45b788a)

## Especificações

### Especificação Estrutural

 A elicitação dos requistos está sendo feito [via Sheet](https://docs.google.com/spreadsheets/d/1-1rj091qlxhiRs93vTr5_trmvLaekvoHrqH35_JUYkg/edit?usp=sharing). A primeira aba do documento  "Requisito Sistêmico" contém uma lista de processos sistêmicos (hardware e software) que foram extraído a partir da descrição do projeto e que compõem o fluxo gerado na Descrição Estrutural do Sistema, cada item da lista é referente a um processo mapeado e suas ramificações recebeu um *RS-SAXX* para ser identificado. Segue a imagem.
 
  ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/b796bf82-d057-45c4-8fe2-b529ad15c862)

Na segunda aba do arquivo “Requisito Funcional”, cada processo gerou um conjunto de requisitos funcionais, RF-SAXX, para esclarecer e identificar o que cada função e componente do processo deve fazer. Além de já conter a indicação de componente de possam atender a demanda. Conforme a imagem abaixo.

<div align="center">
 
   ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/cc66dbc1-754a-4a36-815e-c2141c1f1384)
   
</div> 

Por fim, com base nos componentes foi feita a primeira versão das ligações do circuito.

<div align="center">
 
  ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/ced7a3a6-e7b0-4d8c-9839-f94df5a13b11)
  
</div>

**Processo M1**

     **Título:** Detecção de alta impedância
     
     **Parâmetros de entrada:** Sinal digital convertido pelo MCP3301, conectado ao pino B0 do PIC.
     
     **Parâmetros de saída:** Sinalização intermitente no LED, conectado ao pino A1 do PIC.
     
     **Função:** Indicar se a malha resistiva está conectada corretamente ou com problemas.
     
     **Processo dependente direto:** Processo S1 e S2.


**Processo M2 e M3**

    **Título:** Interrompe o funcionamento do circuito em caso de fuga de corrente maior que 0.1 mA
    
    **Entrada:** Sinal digital convertido pelo MCP3301, pino B0
    
    **Saída:** Conectado ao pino A0 do PIC;
    
    **Função:** Realiza a função diferencial residual nas entradas da malha.
    
    **Processo dependente direto:** Processo S1
    

**Processo M4 e P1:**

    **Título:** Leitura da temperatura da malha
    
    **Entrada:** Parâmetros obtidos a partir da interface serial com o sensor MLX90614, conectado aos pinos A2 e A3 do PIC, respectivamente.
    
    **Saída:** Os parâmetros são usados no processo S4.
    
    **Função:** Faz a leitura do parâmetro para temperatura.
    
    **Processo dependente direto:** Processo S3


**Processo M5**

    **Título:** Condicionamentos do sinal de acionamento.
    
    **Entrada:** Conectado ao pino A0 do PIC.
    
    **Saída:** Conectado à malha.
    
    **Função:** Amplifica o sinal PWM para a malha.
    
    **Processo dependente direto:** Não há

 
**Processo F2**

    **Título:** Seletor de alimentação.
    
    **Entrada:** Bateria e tomada
    
    **Saída:** F2 e F1
    
    **Função:** Seleciona se será usada bateria ou rede elétrica.


**Processo F1**

    **Título:** Carregador de bateria
    
    **Entrada:** Tensão da rede.
    
    **Saída:**
    
    **Função:** Garantir que a bateria esteja carregada.
    

**Processo F3**

    **Título:** Reguladores de tensão
    
    **Entrada:** Tensão da rede
    
    **Saída:** Tensão de 12V e 5V,
    
    **Função:** Alimentação dos componentes.

### Especificação de Algoritmos 



Estão presentes no processo descritos no  [Sheet](https://docs.google.com/spreadsheets/d/1-1rj091qlxhiRs93vTr5_trmvLaekvoHrqH35_JUYkg/edit?usp=sharing), contudo serão passados algoritimos.

**Processo S1**

    **Título:** Problemas na malha
    
    **Entrada:** Processo M1, M2 e M3, usando conectado ao pino B0 do PIC
    
    **Saída:** Interrupção do microcontrolador, via software; interrupção do sinal PWM; e sinalização intermitente no LED, conectado ao pino A1 do PIC.
    
    **Função:** Interrompe o funcionamento do circuito em caso de fuga de corrente maior que 0.1 mA.
    
    **Processo dependente direto:** Processo S2 e S3.


**Processo S2**

    **Título:** Preset equipamento - IHM
    
    **Entrada:** Potenciômetro, conectado ao pino A5 do PIC, com a função de alterar a escala de temperatura. Chave tátil, conectada ao pino A4 do PIC, usada para mudar as opções no menu de configuração.

(descrito no menu no [MANUAL DE OPERAÇÃO 1](https://github.com/piaiman/phms.2023.s2-feec-ea075/blob/main/projetos/Cobertor/images/MANUAL%20DO%20USU%C3%81RIO/2.png) [MANUAL DE OPERAÇÃO 2](https://github.com/piaiman/phms.2023.s2-feec-ea075/blob/main/projetos/Cobertor/images/MANUAL%20DO%20USU%C3%81RIO/3.png) [MANUAL DE OPERAÇÃO 3](https://github.com/piaiman/phms.2023.s2-feec-ea075/blob/main/projetos/Cobertor/images/MANUAL%20DO%20USU%C3%81RIO/4.png)).
    
    **Saída:** Parâmetro de temperatura desejada para o S3 e tempo.
    
    **Função:** Descrito no MANUAL DE OPERAÇÃO.
    
    **Processo dependente direto:** Processo S3.

**Processo S3**

    **Título:** Controle de temperatura
    
    **Entrada:** Os parâmetros de temperatura desejada e tempo são  passados pelo processo S2.
    
    **Saída:** Sinal PWM, pino A0.
    
    **Função:** Gerar um sinal PWM de acordo com a necessidade de aquecimento.
    
    **Processo dependente direto:** Processo M5.


## Projeto

### Esquemático do sistema

![Schematic_Manta_2023-12-03](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/144074445/eaad8ceb-9140-46fb-bbba-3637c0e00c55)

![enter image description here](https://private-user-images.githubusercontent.com/62679350/287906035-e38ef9bc-06b2-4033-b79c-a3fc54d72496.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDE3ODAxMDgsIm5iZiI6MTcwMTc3OTgwOCwicGF0aCI6Ii82MjY3OTM1MC8yODc5MDYwMzUtZTM4ZWY5YmMtMDZiMi00MDMzLWI3OWMtYTNmYzU0ZDcyNDk2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjA1VDEyMzY0OFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY2OTIzYWFmMzIwNmM5ZmIxMTQ5NjBiZWJhMjljMjkyZjQ0MGMyMGJjNzZjMTI3ZTVjMTY3OWEyY2RiZDZhYTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.b9omPI6ba5a3M4zMbjPtaIV8Ir8UAls7AKpy5iT1iLI)

![enter image description here](https://private-user-images.githubusercontent.com/62679350/287907779-872f6e52-c6d6-4b93-af93-de5428ac77db.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDE3ODAxMDgsIm5iZiI6MTcwMTc3OTgwOCwicGF0aCI6Ii82MjY3OTM1MC8yODc5MDc3NzktODcyZjZlNTItYzZkNi00YjkzLWFmOTMtZGU1NDI4YWM3N2RiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjA1VDEyMzY0OFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM1ZTM0OWFmM2RmYTcwZDZjMDJhY2IwZWExOWEzNGIzNWVhNDY1ZGQ4MjY2Mzc4NzU5MTViOWU4YTFlODc4OTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.aJPXv57E8MLFYFf1_cUOyks8Y_5hBHwJT7UbU_AGzKI)

### Descrição

* Alimentação é de entrada de tensão AC com retificador e abaixador de tensão. A bateria é para suprir possíveis faltas de energia.
* O controle do sistema é feito por sensores de temperatura e podem ser monitorados por indicadores visuais, LEDs e Display.
* Há o sistema de segurança que atua em casos de sobre corrente.

## Referências

[ABNT NBR IEC 60601-1-2010: Equipamento eletromédico Parte 1: Requisitos gerais para segurança básica e desempenho essencial](https://www.zambini.org.br/pdfs/ABNT%20NBR%20IEC%2060601-1-2010%20Emenda%201-2016%20-%20Equipamento%20eletrom%C3%A9dico%20-%20Parte%201-%20Requisitos%20gerais%20para%20seguran%C3%A7a%20b%C3%A1sica%20e%20desempenho%20essencial.pdf)


