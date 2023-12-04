# ` Sistema de Irrigação Inteligente `

# ` Smart Watering System `

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 | Felipe Rezende Gardin | 215766  | Eng. Elétrica|
 | Igor Silva Mota | 199009 | Eng. Elétrica|
 | Vinicius Errero| 206768 | Eng. Computação(AB)|

## Arquivos Importantes

[Esquemático em PDF](https://github.com/frgardin/ea075-2023.2/blob/main/projetos/sistema-de-irriga%C3%A7%C3%A3o/pdf/esquema_eletrico.pdf)

[Lista de Componentes](https://github.com/frgardin/ea075-2023.2/blob/main/projetos/sistema-de-irriga%C3%A7%C3%A3o/componentes.md)

[PCB](https://github.com/frgardin/ea075-2023.2/tree/main/projetos/sistema-de-irriga%C3%A7%C3%A3o/images)

## Descrição do Projeto

O "Smart Watering System" tem por objetivo principal o fornecimento de uma solução capaz de irrigar pequenas hortas de forma automatizada, visando a economia de água e independência do fator humano. Este produto busca atingir pessoas aquelas que não possuem tempo disponível para fazer o cuidado adequado no que diz respeito a atividade de irrigação, ou entusiastas de automações residenciais.

Além disso, o sitema é capaz de entender a real necessidade dessa atividade, tentando evitar ao máximo irrigar o solo em momentos inapropriados através de informações obtidas por seus sensores.

Utilizando, sensores de umidade e temperatura, sensor de umidade do solo, display LCD, e ainda, reles e motores (relacionados a bomba d'agua), o valor econômico do projeto navega ao redor de R$ 100,00.

## Descrição Funcional

O projeto contará como componentes principais:

- **microcontrolador PIC18F4550:**
  - Este que será reponsável por ser o cérebro do projeto podendo tomar decisões a partir dos dados coletados por meio dos sensores a serem especificados.
- **Sensores:**
  - Sensor de Umidade do Solo (Solo Moisture Sensor) FC-28.
  - Sensor de Temperatura e Umidade do Ar DHT-11.
- **Atuador:**
  - Atuador é composto de um sistema envolvendo relé e válvula solenóide.
- **Visualizador:**
  - Display LCD para visualizar as informações obtidas pelos sensores.
- **Fonte de Alimentação:**
  - Fonte de alimentação típica de 5V.

Além dos items citados, a construção dependerá também de outros componentes, como resistores, capacitores, cristal, dentre outros.

### Funcionalidades

Esse sistema possui em suma apenas uma funcionalidade: **Irrigar a plantação**.

Claro que, para se demonstrar útil, essa funcionalidade, como descrito anteriormente deve ocorrer em determinados momentos de acordo com a leitura dos sensores de umidade e temperatura.

Além disso, pode-se destacar que caso o usuário deste produto queira obter informações, estas podem ser visualizadas a partir do display LCD.

### Configurabilidade

A princípio a ideia era manter o sistema 100% automático não dando opção ao usuário de se dispor de vários modos de operação.

Portanto, atualmente o sistema é considerado "Plug and Play", ou seja, tendo conectado a fonte de alimentação e disposto de forma correta o sensor de umidade do solo e atuadores, já estaria pronto para uso.

Mas, conforme o desenvolvimento do projeto estudaremos a possibilidade de adicionar novos modos de operação.

Vale a pena ressaltar que o display LCD abrande o protocolo I2C, tendo um CI intermediário que realiza essa conversão.

P.S.: O modo de operação será descrito no subtópico Eventos e Tratamento de Eventos

### Eventos

Utilizando o temporizador presente no microcontrolador, iremos verificar a cada minuto, a umidade do solo utilizando o sensor FC-28 e a umidade e temperatura do ar utilizando o sensor DHT-11, e utilizar esses parâmetros para determinar a ativação do relé responsável pela irrigação.

### Tratamento de Eventos

Utilizando a informação dos sensores DHT-11 e FC-28 descritos acima, o sistema irá determinar se o solo deverá ser irrigado e a quantidade de água que será liberada.
O principal indicador será a umidade do solo, com o solo estando mais seco, mais água será liberada. Além disso, caso a temperatura do ar esteja alta e/ou a umidade do ar estiver baixa, a quantidade de água a ser irrigada será maior.
Por fim, os valores de temperatura, umidade do solo e umidade do ar da última medição serão mostrados no display LCD

## Descrição Estrutural do Sistema

Para o tratamento de eventos, o sistema deverá seguir conforme abaixo:

1) Utilizando os sensores disponíveis, o sistema irá medir a umidade do solo, além da umidade e temperatura do ar
2) Essas informações serão disponibilizadas no display LCD
3) Utilizando as informações, irá decidir se o mesmo irrigará ou não
4) Caso positivo, irá mandar um sinal para o atuador com fim de irrigar o solo
5) Caso negativo, esse sinal não será enviado
6) O sistema espera 60 segundos e retorna ao passo 1

### Diagrama

<h1 align="center"><img src="/projetos/sistema-de-irrigação/ea075-e1.drawio-att.png"/></h1>

### Estrutura e funcionamento do sistema

  O sistema será composto por um microcontrolador, dois sensores, um relé e uma válvula solenóide, um display LCD e uma fonte de alimentação de 5V. Basicamente, o funcionamento será de forma automática, sendo que ao alimentar o sistema, os sensores irão realizar medições dos parâmetros (umidade e temperatura), periodicamente, e assim, enviará os valores para o microcontrolador que irá decidir se a irrigação deverá ou não ser ativada, considerando um valor limite para os parâmetros medidos. Quando é medido o valor mínimo para a umidade do solo, o microcontrolador aciona o relé e a válvula solenóide para fazer a irrigação, até que seja atingido o valor ideal de umidade especificado. O display LCD, será utilizado para mostrar continuamente os valores de umidade e temperatura do solo e do ar.

## Especificações

### Especificação Estrutural

  Abaixo especifica-se os principais materiais necessários aos subsistemas deste projeto, não está especificado por exemplo os resistores, pois entende-se que o intuito desta tabela é
  apenas listar componentes chaves:

  |P.N.| Nome |Qtde. | Funcionalidade | Observação | Link-datasheet |
  |--|--|--|--|--|--|
  | PIC18F4550 | Microcontrolador PIC18 | 1  | "Cérebro" do Sistema | Microcontrolador| <https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/39632e.pdf> |
  | LM16255K | Display LCD 16x2 | 1 | Mostrar as medidas captadas pelos sensores | Faz parte da categoria visualizadores| <https://pdf.datasheetcatalog.com/datasheet/Sharp/mXvtrzw.pdf> |
  | PCF8574 | Expansor de I/O remoto de 8 bits para barramento I2C | 1 | Realizar intermediário entre a comunicação serial do MC e a paralela do display LCD | - | <https://www.ti.com/lit/ds/symlink/pcf8574.pdf> |
  | FC-28 | Sensor de Umidade do Solo | 1 |  Através de suas pontas de prova, medir a resistência do solo | Faz parte da categoria sensores|<https://datasheethub.com/wp-content/uploads/2022/08/SEN0114_Web.pdf> |
  | DHT-11 | Sensor de Umidade e Temperatura | 1 |  Medir temperatura e umidade do ar | Faz parte da categoria sensores|<https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf> |
  | HC-49S | Cristal Oscilador 20 MHz | 1 | Gerar sinal de clock ao microcontrolador | - | <https://datasheet.lcsc.com/lcsc/2008251934_HD-71008000RW1_C655216.pdf> |
  | BC547 | Transistor de silício epitaxial NPN | 1 |  Componente auxiliar do circuito do acionamento do motor | Faz parte da categoria atuadores | <https://www.sparkfun.com/datasheets/Components/BC546.pdf> |
  | JQC-3F | Relé | 1 |  Relé que aciona a valvula solenóide | Faz parte da categoria atuadores |<https://pdf.voron.ua/files/pdf/relay/JQC-3F(T73).pdf> |
  | 1N4007 | Retificador de plástico de uso geral | 1 |  Diodo de proteção do relé | Faz parte da categoria atuadores |<https://www.vishay.com/docs/88503/1n4001.pdf> |
  | - | Válvula de Vazão Solenóide Água 12VDC | 1 |  Realizar a irrigação do solo | Faz parte da categoria atuadores |<https://www.makerhero.com/produto/valvula-de-vazao-solenoide-agua-12vdc/#tab-description> |

  O microcontrolador escolhido para realizar a tarefa escolhida pelo projeto foi o PIC18F4550, este que conta com mais de uma entrada analógica,
  conta com suporte ao protocolo de comunicação serial I2C, e clahttps://repositorio.ufpe.br/bitstream/123456789/48412/1/TCC%20Railton%20Silva%20Rocha%20Junior.pdf2 para 8 portas, com isso, poderia por exemplo, utilizar outras portas do microcontrolador para outra
  tarefa por exemplo, ou adicionar mais "features" ao meu projeto futuramente.

  De início, não identificamos a necessidade de circuitos auxiliares para leitura das informações medidas pelos sensores FC-28 e DHT-11, onde pretende-se utilizar duas entradas analógicas
  que o microcontrolador fornece, sendo elas (RA0 / AN0) e (RA1 / AN1). Com isso, tendo essas tensões lidas pelo MC, ocorre a conversão desses valores para as gradezas de cada sensor, e a
  partir da lógica definida na subseção "Especificação de Algoritmos", ocorre a comunicação com o atuador.
  
  Já para a configuração de oscilação, procurando no datasheet do microcontrolador, identificou-se que existem diversas possibilidades de configuração de clock, onde
  para esta aplicação escolheu-se o cristal de 20 MHz, juntamente com os capacitores de cerâmica de 15 pF.

  Para o circuito do atuador [1], pensou-se em um circuito de chaveamento com transistores, onde o transistor aciona um relé, este que aciona a válvula solenóide.

  Por fim, o sensor FC-28 precisa estar infincado ao solo, enquanto o restante pode estar sobre a pcb mesmo, espera-se deixar uma quantidade considerável de área para o microcontrolador
  e para o transistor e relé, no momento, não identifica-se a necessidade de um dissipador de calor.
  
  <!-- (Se preferir, adicione um link para o documento de especificação estrutural)

  Entende-se por estrutural a descrição tanto das características elétricas e temporais como das  restrições físicas de cada bloco funcional.
  Nessa etapa do projeto, ainda não será solicitado o diagrama elétrico mas espera-se que já  estejam identificados os componentes e circuitos integrados propostos
  para implementação do sistema embarcado proposto.

  Como o projeto de um sistema embarcado é centralizado nas tarefas, recomenda-se iniciar com a definição dos periféricos de entrada e saída (atuadores e/ou sensores) apropriados para o
  sistema. Pode ser necessário definir um endereço distinto para cada um deles.
  Este endereço será utilizado pela unidade micro-controladora para acessá-los tanto para leitura como para escrita.
  Nesta etapa do projeto espera-se que a unidade micro-controladora seja definida.
  Tendo definidos os periféricos e a memória, é possível projetar um decodificador de endereços
  que converte o endereço referenciado no programa em sinal *Chip Select – CS* do dispositivo
  correspondente, habilitando-o para realizar um ciclo de leitura ou de escrita.

  Nesta etapa do projeto espera-se que sejam identificada também a eventual necessidade do  projeto de circuitos de interface para os periféricos do projeto.
  Assim, devem ser incluídos na especificação, se necessário:

- conversores AD e DA;
- padrões de comunicação a serem adotados;
- circuitos de sincronização de sinais temporais.

  Finalmente, deve-se especificar as restrições físicas e ambientais de funcionamento do  circuito, tais como limites mecânicos
  (altura, largura, profundidade) e limites de dissipação térmica. -->


### Especificação de Algoritmos

  <!-- (Se preferir, adicione um link para o documento de especificação de algoritmos).

  Deve ser elaborado para CADA evento o algoritmo de tratamento deste evento. Com base no
  tamanho de cada algoritmo, estima-se o tamanho de memória necessária para armazenar todos
  os programas e os dados associados. Isso permitirá especificar a memória a ser utilizada e o
  espaço onde serão armazenados os programas. O algoritmo de tratamento de evento pode
  ser representado graficamente por um fluxograma. Recomenda-se usar símbolos gráficos consistentes
  com a norma internacional ISO 1028-1973 e IS0 2972-1979. -->

  A fim de representar o algoritmo utilizado para efetuar a irrigação do solo periodicamente, dependendo das variavéis de umidade (solo e ar), e temperatura (ar).
  Criou-se um pseudo-código que representa o algoritmo a ser utilizado, onde suas variáveis são:

- Variáveis:
  - Umidade do ar
  - Umidade do solo
  - Temperatura do ar
- Temporização de 60s
- Display LCD
- Válvula de irrigação

Pseudoalgoritmo(C):  

```text
  Inclusão das bibliotecas dos sensores, display e temporização

  Declaração do modo de operação do timer

  Declaração do endereço onde está mapeado o FC-28 na variável sensor_fc
  Declaração do endereço onde está mapeado o DHT_11 na variável sensor_dht

  Declaração da variável UmiSolo com valor inicial Null
  Declaração da variável UmiAr com valor inicial Null
  Declaração da variável Temp com valor inicial Null
  Declaração da variável Duracao_Irrigacao com valor inicial Null

  Declaração da variável UmiSolo-min com valor inicial 800

  interrupção {

    a cada 10 segundos atualizar display via protocolo i2c

  }

  loop infinito {

    sleep/delay 60s

    Ler umidade do solo e armazenar em UmiSolo
    Ler temperatura do solo e armazenar em Temp
    Ler umidade do ar e armazenar em UmiAr

    VR-UmiSolo = -0,17*UmiSolo + 171,4

    Se(If) VR-UmiSolo > UmiSolo-min:
     Pular para próximo loop

    Calcular Duracao_Irrigacao com as variaveis
    Abrir relés por Duracao_Irrigacao

}  

```

  Para atualização do display, optou-se por utilizar interrupção, a fim de que o
  usuário possa obter a informação dos sensores em tempo real, como o período de irrigação se da por uma espera longa, de início especificou-se 60 segundos.

  Ainda, sabendo que o sensor se trata de "medidor de grandeza fisíca", onde o valor de tensão medido na entrada analógica é proporcional a grandeza medida.
  No caso do sensor FC-28, afirma-se que percentagem de umidade do solo pode ser dada por:

  $$
    y = -0.17 x + 171.4
  $$  

  Onde $y$ se trata da umidade relativa do solo, e $x$ o valor de entrada do microcontrolador.

## Referências

  [1] Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. Academia.edu. Disponível em: <https://www.academia.edu/24415757/Auto_Irrigation_System_using_Soil_Moisture_Sensor_and_PIC_Microcontroller>. Acesso em: 07 de setembro de 2023.

  [2] SILVA, DANILO EDUARDO LASTÓRIA. Sistema Automático de Irrigação. Disponível em: <https://lyceumonline.usf.edu.br/salavirtual/documentos/1898.pdf>. Acesso em: 07 de setembro de 2023.

  [3] ELECTRONICS HUB. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. Disponível em: <https://www.electronicshub.org/auto-irrigation-system-using-soil-moisture-sensor-and-pic-microcontroller/>. Acesso em: 07 de setembro de 2023.

  [4] MICROCONTROLLERS LAB. Solar Power Auto Irrigation System using Microcontroller. Disponível em: <https://microcontrollerslab.com/solar-power-auto-irrigation-system-using-microcontroller/>. Acesso em: 07 de setembro de 2023.

  [5] WR KITS. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. YouTube, Data de publicação. URL: <https://www.youtube.com/playlist?list=PLZ8dBTV2_5HS_YaI8C4hsTzehRSgPjuxQ>.

  [6] SPARKFUN. Soil Moisture Sensor. GitHub. Disponível em: <https://github.com/sparkfun/Soil_Moisture_Sensor>. Acesso em: 07 de setembro de 2023.

  [7] DATTA, Sumon; TAGHVAEIAN, Saleh; OCHSNER, Tyson; MORIASI, Daniel; GOWDA, Prasanna; STEINER, Jean. Performance Assessment of Five Different Soil Moisture Sensors under Irrigated Field Conditions in Oklahoma. MDPI. Disponível em: <https://www.mdpi.com/1424-8220/18/11/3786>. Acesso em: 10 de setembro de 2023.

  [8] ALBERT, Stephen. Soil and Air Temperatures for Growing Vegetables. Harvest to Table. Disponível em: <https://harvesttotable.com/soil-and-air-temperatures-for-growing-vegetables/>. Acesso em: 10 de setembro de 2023.

  [9] JUNIOR, Railton Silva Rocha. Sistema embarcado para automação da irrigação por pulsos acionada por v´alvulas solenoides tipo latching. Disponível em: <https://repositorio.ufpe.br/bitstream/123456789/48412/1/TCC%20Railton%20Silva%20Rocha%20Junior.pdf>. Acesso em 03 de dezembro de 2023.
