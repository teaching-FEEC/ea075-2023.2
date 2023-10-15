# ` Sistema de Irrigação Inteligente `

# ` Smart Watering System `

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 | Felipe Rezende Gardin | 215766  | Eng. Elétrica|
 | Igor Silva Mota | 199009 | Eng. Elétrica|
 | Vinicius Errero| 206768 | Eng. Computação(AB)|

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
  - Sensor de Temperatura e Umidade do Ar DHT-22.
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

P.S.: O modo de operação será descrito no subtópico Eventos e Tratamento de Eventos

### Eventos

Utilizando o temporizador presente no microcontrolador, iremos verificar a cada minuto, a umidade do solo utilizando o sensor FC-28 e a umidade e temperatura do ar utilizando o sensor DHT-22, e utilizar esses parâmetros para determinar a ativação do relé responsável pela irrigação.

### Tratamento de Eventos

Utilizando a informação dos sensores DHT-22 e FC-28 descritos acima, o sistema irá determinar se o solo deverá ser irrigado e a quantidade de água que será liberada.
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

<p align="center"
  <img src="/projetos/sistema-de-irrigação/ea075-e1.drawio-att.png" /
</p

### Estrutura e funcionamento do sistema

  O sistema será composto por um microcontrolador, dois sensores, um relé e uma válvula solenóide, um display LCD e uma fonte de alimentação de 5V. Basicamente, o funcionamento será de forma automática, sendo que ao alimentar o sistema, os sensores irão realizar medições dos parâmetros (umidade e temperatura), periodicamente, e assim, enviará os valores para o microcontrolador que irá decidir se a irrigação deverá ou não ser ativada, considerando um valor limite para os parâmetros medidos. Quando é medido o valor mínimo para a umidade do solo, o microcontrolador aciona o relé e a válvula solenóide para fazer a irrigação, até que seja atingido o valor ideal de umidade especificado. O display LCD, será utilizado para mostrar continuamente os valores de umidade e temperatura do solo e do ar.

## Especificações

### Especificação Estrutural

  (Se preferir, adicione um link para o documento de especificação estrutural)
  
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
  (altura, largura, profundidade) e limites de dissipação térmica.

### Especificação de Algoritmos

  (Se preferir, adicione um link para o documento de especificação de algoritmos).

  Deve ser elaborado para CADA evento o algoritmo de tratamento deste evento. Com base no
  tamanho de cada algoritmo, estima-se o tamanho de memória necessária para armazenar todos
  os programas e os dados associados. Isso permitirá especificar a memória a ser utilizada e o
  espaço onde serão armazenados os programas. O algoritmo de tratamento de evento pode
  ser representado graficamente por um fluxograma. Recomenda-se usar símbolos gráficos consistentes 
  com a norma internacional ISO 1028-1973 e IS0 2972-1979.

## Referências

- Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. Academia.edu. Disponível em: <https://www.academia.edu/24415757/Auto_Irrigation_System_using_Soil_Moisture_Sensor_and_PIC_Microcontroller. Acesso em: 07 de setembro de 2023.

- SILVA, DANILO EDUARDO LASTÓRIA. Sistema Automático de Irrigação. Disponível em: <https://lyceumonline.usf.edu.br/salavirtual/documentos/1898.pdf. Acesso em: 07 de setembro de 2023.

- ELECTRONICS HUB. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. Disponível em: <https://www.electronicshub.org/auto-irrigation-system-using-soil-moisture-sensor-and-pic-microcontroller/. Acesso em: 07 de setembro de 2023.

- MICROCONTROLLERS LAB. Solar Power Auto Irrigation System using Microcontroller. Disponível em: <https://microcontrollerslab.com/solar-power-auto-irrigation-system-using-microcontroller/. Acesso em: 07 de setembro de 2023.

- WR KITS. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. YouTube, Data de publicação. URL: <https://www.youtube.com/playlist?list=PLZ8dBTV2_5HS_YaI8C4hsTzehRSgPjuxQ.

- SPARKFUN. Soil Moisture Sensor. GitHub. Disponível em: <https://github.com/sparkfun/Soil_Moisture_Sensor. Acesso em: 07 de setembro de 2023.

- DATTA, Sumon; TAGHVAEIAN, Saleh; OCHSNER, Tyson; MORIASI, Daniel; GOWDA, Prasanna; STEINER, Jean. Performance Assessment of Five Different Soil Moisture Sensors under Irrigated Field Conditions in Oklahoma. MDPI. Disponível em: <https://www.mdpi.com/1424-8220/18/11/3786. Acesso em: 10 de setembro de 2023.

- ALBERT, Stephen. Soil and Air Temperatures for Growing Vegetables. Harvest to Table. Disponível em: <https://harvesttotable.com/soil-and-air-temperatures-for-growing-vegetables/. Acesso em: 10 de setembro de 2023.
