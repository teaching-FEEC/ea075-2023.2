# `Caixa Preta`
# `Black Box`

## Apresentação
O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Caio Ruiz Coldebella  | 232621  | Eng. de Computação|
| Gustavo de Souza dos Reis  | 217425  | Eng. de Computação|

## Descrição do Projeto
O Black Box é um sistema de registro e transmissão de dados de vôo de um foguete, ele foi pensado para
atender uma demanda da equipe Antares Unicamp, aonde se viu a necessidade de análise de informações do lançamento.

Dessa forma, mesmo que haja um acidente que comprometa o vôo, o sistema deve ser seguro e resistente o suficiente para
resistir ao impacto da queda e permitir a leitura de informações sobre o lançamento ao ser encontrado em terra, além disso
é necessário que seja de baixo custo.

## Descrição Funcional
O sistema será projetado utilizando uma plataforma de IOT NodeMCU Amica baseada no microcontrolador ESP8266, juntamente com um barômetro BMP280, funcionando como altímetro,
que será responsável por fornecer com precisão os dados de altitude. 

A vantagem de utilizarmos o ESP8266 é que este possui uma memória EEPROM de 4MB, além de uma flash de 32MB, nas quais podemos salvar os dados do sensor de forma segura. Tem também um  módulo wi-fi para podermos receber com praticidade os dados de log do vôo. Além disso ele possui outros pontos positivos como bluetooth, um microprocessador de baixa potência,
 antena embutida, conversor USB serial integrado e porta micro USB para alimentação e programação. 

### Funcionalidades
As funcionalidades planejadas para o sistema serão:

- Detecção de Apogeu (altitude máxima de vôo)
- Tempo de Apogeu
- Variação da altitude ao longo de itervalos de tempo 

### Configurabilidade
Os modos de funcionamento do sistema serão configurados por meio de um switch RBF (Remove Before Flight).

- Se o RBF estiver inserido no sistema, estaremos com o modo de leitura ativado, sendo possível ler os dados do último vôo via wifi
- Se o RBF for removido, estaremos no modo escrita, no qual o microcontrolador salva os dados lidos pelo altímetro, com destaque para o apogeu.

### Eventos
- Inserção do RBF
	- Comunicação via wi-fi (não periódico)

- Remoção do RBF
	- Leitura do altímetro (periódico, ~20ms)
	- Registro de leitura do altímetro (periódico, ~100ms)

### Tratamento de Eventos
- Inserção do RBF: ao inserir o RBF, o sistema deve para de escrever os dados na memória, habilitar o web-server e a interface wifi e disponibilizar os dados lidos na interface.
- Remoção do RBF: ao remover o RBF, o sistema deve coletar as leituras do altímetro, filtrá-las (média móvel) e salvar na memória.

## Descrição Estrutural do Sistema
![Diagrama Estrutural](./Diagrama_black_box.drawio.png)

## Referências

- [Descrição ESP8266](https://www.huinfinito.com.br/home/1145-modulo-wifi-esp8266-nodemcu-esp-12e.html)
- [Usando a EEPROM ESP8266](https://www.aranacorp.com/pt/usar-a-eeprom-com-um-esp8266/)
