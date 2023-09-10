# ` Sistema de Irrigação Inteligente `
# ` Smart Watering System `

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).


> |Nome  | RA | Curso|
> |--|--|--|
> | Felipe Rezende Gardin | 215766  | Eng. Elétrica|
> | Igor Silva Mota | 199009 | Eng. Elétrica|
> | Vinicius Errero| 206768 | Eng. Computação(AB)|


## Descrição do Projeto

O "Smart Watering System" tem por objetivo principal o fornecimento de uma solução capaz de irrigar pequenas hortas de forma automatizada, visando a economia de água e independência do fator humano. Este produto busca atingir pessoas aquelas que não possuem tempo disponível para fazer o cuidado adequado no que diz respeito a atividade de irrigação, ou entusiastas de automações residenciais.

Além disso, o sitema é capaz de entender a real necessidade dessa atividade, tentando evitar ao máximo irrigar o solo em momentos inapropriados através de informações obtidas por seus sensores.

Utilizando, sensores de humidade e temperatura, sensor de humidade do solo, display LCD, e ainda, reles e motores (relacionados a bomba d'agua), o valor econômico do projeto navega ao redor de R$ 100,00.

## Descrição Funcional

O projeto contará como componentes principais:

- **microcontrolador PIC18F4550:**
  - Este que será reponsável por ser o cérebro do projeto podendo tomar decisões a partir dos dados coletados por meio dos sensores a serem especificados.
- **Sensores:** 
  - Sensor de Umidade do Solo (Solo Moisture Sensor) FC-28.
  - Sensor de Temperatura e Umidade do Ar DHT-22.
- **Atuador:**
  - Atuador é composto de um sistema envolvendo relé e válvula solenoide.
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
A cada 6 horas, o sistema irá verificar a umidade do solo utilizando o sensor FC-28 e a umidade e temperatura do ar utilizando o sensor DHT-22.

### Tratamento de Eventos
Utilizando a informação dos sensores, o sistema irá determinar se o solo deverá ser irrigado e a quantidade de água que será liberada.
O principal indicador será a umidade do solo, com o solo estando mais seco, mais água será liberada. Além disso, caso a temperatura do ar esteja alta e/ou a umidade do ar estiver baixa, a quantidade de água a ser irrigada será maior.

## Descrição Estrutural do Sistema
Para o tratmaneto de eventos, o sistema deverá seguir conforme abaixo:
1) O sistema irá medir a umidade do solo e ver se está abaixo de um valor pré-definido.
2) Se estiver acima do valor, o sistema irá esperar 3h
3) Se estiver abaixo, o sistema ira medir a umidade e temperatura do ar
4) Após a medição, o sistema deverá calcular o quanto de água é preciso para a irrigação
5) Após o cálculo, o sistema irá realizar a irrigação e esperar 3h. 


## Referências

ACADÊMIA, Autor. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. Academia.edu. Disponível em: https://www.academia.edu/24415757/Auto_Irrigation_System_using_Soil_Moisture_Sensor_and_PIC_Microcontroller. Acesso em: 07 de setembro de 2023.

SILVA, DANILO EDUARDO LASTÓRIA. Sistema Automático de Irrigação. Disponível em: https://lyceumonline.usf.edu.br/salavirtual/documentos/1898.pdf. Acesso em: 07 de setembro de 2023.

ELECTRONICS HUB. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. Disponível em: https://www.electronicshub.org/auto-irrigation-system-using-soil-moisture-sensor-and-pic-microcontroller/. Acesso em: 07 de setembro de 2023.

MICROCONTROLLERS LAB. Solar Power Auto Irrigation System using Microcontroller. Disponível em: https://microcontrollerslab.com/solar-power-auto-irrigation-system-using-microcontroller/. Acesso em: 07 de setembro de 2023.

WR KITS. Auto Irrigation System using Soil Moisture Sensor and PIC Microcontroller. YouTube, Data de publicação. URL: https://www.youtube.com/playlist?list=PLZ8dBTV2_5HS_YaI8C4hsTzehRSgPjuxQ.

SPARKFUN. Soil Moisture Sensor. GitHub. Disponível em: https://github.com/sparkfun/Soil_Moisture_Sensor. Acesso em: 07 de setembro de 2023.

https://www.mdpi.com/1424-8220/18/11/3786
