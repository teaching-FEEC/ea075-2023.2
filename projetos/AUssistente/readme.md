# `AUssistente`
# `Pet Care Assistant`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

## Integrantes

|Nome  | RA | Curso|
|--|--|--|
| Betania Eugenia Rodrigues da Silva  | 167508  | Eng. Elétrica|
| Vinícius de Oliveira Peixoto Rodrigues  | 245294  | Eng. de Computação |


## Descrição do Projeto
> Descrição do objetivo principal do projeto, incluindo contexto gerador, motivação.

O objetivo do presente projeto é desenvolver um sistema que auxilie os donos de animais de estimação, com foco em cães e gatos, a facilitar o monitoramento da saúde de seus pets em tempo real. Esta iniciativa surge em resposta à crescente demanda por cuidados mais especializados e personalizados para nossos queridos animais de estimação, que estão cada vez mais integrados à vida familiar. O sistema atuará como um 'companheiro canino e felino inteligente', oferecendo uma solução completa para monitorar e melhorar o bem-estar de nossos bichinhos, garantindo que eles desfrutem de uma vida feliz e saudável ao nosso lado.

> Qual problema vocês pretendem solucionar?

Nosso projeto tem como objetivo resolver diversos desafios enfrentados pelos donos de animais de estimação. O primeiro grande problema a ser abordado é a perda de animais de estimação quando eles escapam, o que é uma preocupação frequente para muitos proprietários. Para resolver essa questão, haverá um sistema de geolocalização que permite localizar os animais rapidamente, facilitando o reencontro com seus donos.

Além disso, nosso sistema visa melhorar o cuidado com a saúde dos animais de estimação de maneira mais abrangente. Ele monitorará constantemente os batimentos cardíacos dos animais e notificará os proprietários se os batimentos cardíacos saírem do normal, permitindo uma resposta rápida em caso de problemas de saúde. Além do mais, o sistema será capaz de aferir o sono e o padrão de alimentação dos animais, o que ajuda os donos a garantir que seus bichinhos tenham um estilo de vida saudável. Isso não só aumenta a qualidade de vida dos animais de estimação, mas também antecipa possíveis agravantes para sua saúde, permitindo intervenções precoces quando necessário.

> Quem são os potenciais usuários?
 
Donos de animais de estimação em um geral.
 
> É possível estabelecer um valor econômico associado?

Sim, é possível, mas primeiramente é necessário realizar um levantamento dos componentes a serem utilizados.


## Descrição Funcional

### Funcionalidades
- Rastreamento de GPS
- Monitoramento Cardíaco
- Acompanhamento dos Níveis de Atividades
- Aferição de Hábitos Diários como frequência e nutrição das refeições e padrões de sono
- Alertas de saída da área pré determinada pelo dono
- Alertas de temperatura corporal do pet
- Análise dos dados diários através gráficos para melhor entendimento do dono

### Configurabilidade

- Pareamento BLE: o dispositivo pode ser configurado por meio de um botão para se conectar a um dispositivo (smartphone, assistente virtual, etc.) por Bluetooth para transmitir dados
- Perfil de energia: o modo de funcionamento do dispositivo pode ser configurado de modo a controlar o consumo de energia, prolongando assim o tempo de atividade antes de ser necessário carregar o aparelho

### Eventos
- Ativação do botão de ligar/desligar
- Leitura de sensores (feitas por meio de interrupção de hardware): os sensores serão configurados para, em intervalos regulares, reportarem para o microcontrolador os valores medidos. Estimativa dos intervalos de leituras:
    - Sensor inercial (IMU): entre 200ms e 2s
    - Sensor de batimentos cardíacos/oxigenação sanguínea: entre 1s e 10s
    - Sensor de temperatura: entre 15s e 1m
    - Sensor de nível de bateria: entre 15s e 1m
    - GPS: entre 15s e 1m
- Ativação do botão de pareamento BLE
- Requisição recebida por BLE
- Valores críticos de batimento cardíaco/oxigenação/temperatura
- Nível crítico de bateria

### Tratamento de Eventos
- Ativação do botão de ligar/desligar
    - Dispositivo desligado ou em _deep sleep_: carrega dados de configuração da memória flash ou da SRAM, realiza o boot e o bringup dos componentes
    - Dispositivo ativo ou _idle_: realiza a rotina de shutdown, escrevendo dados relevantes na memória não-volátil e desligando a placa

- Leitura de sensores: armazena os dados em um buffer circular na memória RAM
    - Caso o buffer circular esteja cheio: armazena os dados na SRAM ou na memória não-volátil

- Ativação do botão de pareamento BLE: executa a rotina de pareamento para se conectar ao smartphone

- Requisição recebida por BLE: invoca a rotina adequada para responder à requisição de maneira assíncrona (sem interromper o fluxo de leitura de sensores)

- Valores críticos de batimento cardíaco/oxigenação/temperatura: toca um aviso sonoro e envia uma mensagem de alerta para o dispositivo conectado por Bluetooth (caso haja um)

- Nível crítico de bateria: envia uma mensagem de alerta para o dispositivo conectado por Bluetooth, escreve dados relevantes na SRAM, desativa os sensores e entra em _deep sleep_

## Descrição Estrutural do Sistema
> Junto com a descrição do comportamento do sistema, deve-se especificar, em nível de bloco ou sistema, a estrutura necessária 
> para captar os eventos do mundo externo, para alojar e processar o programa de tratamento de eventos, e para atuar sobre o mundo externo.
>
> Para essa descrição recomenda-se a criação de diagramas de blocos.
> Nesse diagrama, devem ser destacados os blocos funcionais que compõem o sistema, incluindo uma síntese das funcionalidades de cada bloco.
> Além disso, deve-se esclarecer também o relacionamento entre estes blocos, incluindo os principais sinais de comunicação entre
> os blocos de forma a assegurar a execução de todas as tarefas que o sistema deve realizar.
> 
> Você sabia? Ferramentas como o `draw.io` permitem integração com o Github.
> 

## Referências
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
