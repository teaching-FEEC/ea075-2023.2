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
- Inserção do RBF: ao inserir o RBF, o sistema deve parar de escrever os dados na memória, habilitar o web-server e a interface wifi e disponibilizar os dados lidos na interface.
- Remoção do RBF: ao remover o RBF, o sistema deve coletar as leituras do altímetro, filtrá-las (média móvel) e salvar na memória.

## Descrição Estrutural do Sistema
![Diagrama Estrutural](./Diagrama_black_box.drawio.png)

## Especificações

### Especificação Estrutural

### Especificação de Algoritmos
![Diagrama de Algoritmos](./Especificacao_software.drawio.png)

[Pseudocódigo de especificação do algoritmo](./Especificacao_algoritmos.txt)

Para realizar a estimativa do tamanho que o código irá ocupar na memória, utilizamos o auxílio do ChatGPT para analisar o pseudocódigo, já que não temos como realizar a sua compilação. Para isso foram levados em conta os seguintes fatores:

1. *Inclusão de Bibliotecas*: A inclusão de bibliotecas específicas para o ESP8266.

2. *Código de Configuração*: Funções como `setup()` e `loop()` que possuem pouca complexidade.

3. *Funções Adicionais*: As funções adicionais, como `setup_provide_data()`, `setup_flight()`, `provide_flight_data()`, `read_flight_data()`, `handle_OnConnect()`, e `handle_NotFound()`.

4. *Operações de I2C e EEPROM*: Operações de leitura/gravação na EEPROM e comunicação I2C podem adicionar código extra, mas o tamanho exato depende da implementação específica dessas operações.

5. *Manipulação de Variáveis e Controle de Fluxo*: O código que lida com variáveis, estruturas de controle de fluxo e lógica condicional também contribuirá para o tamanho do código.

Dado esse conjunto de fatores e com a premissa de que o código não é excessivamente complexo e não inclui bibliotecas extremamente grandes, a estimativa de 20 KB a 50 KB parece uma faixa razoável.

## Referências

- [Descrição ESP8266](https://www.huinfinito.com.br/home/1145-modulo-wifi-esp8266-nodemcu-esp-12e.html)
- [Usando a EEPROM ESP8266](https://www.aranacorp.com/pt/usar-a-eeprom-com-um-esp8266/)
