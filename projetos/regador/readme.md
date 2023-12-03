# `Regador de Planta Automático`
# `Automatic Plant Watering System`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Chen Jiahao  | 195673  | Eng. Elétrica|
| Victor Loiola Lima  | 257028  | Eng. Elétrica|


## Descrição do Projeto
O objetivo principal do projeto é criar um sistema que possa irrigar a terra de plantas de forma automática. Este sistema é voltado para usuários amadores em jardinagem, que procuram uma solução barata e portátil para regar suas plantas quando necessário.
Como o cuidado de plantas é constante e pode ocorrer o esquecimento em fazê-lo, esse sistema propõe regá-las através de uma rotina elaborada com ações definidas para cada cenário onde a planta e o ambiente se encontram.
Apenas duas atividades manuais continuarão sendo necessárias: Preencher o reservatório com água e trocar a bateria.
Valor econômico estimado associado ao projeto:

 - Micro controlador ATTiny43U: R$20
 - Mini bomba d'água: R$20
 - Bateria: R$10
 - Tubo para regar plantas: R$5
 - Impressão da placa PCB: R$10
 - Componentes da placa: R$10
 - Sensor de nível d'água: R$20
 - Sensor de umidade: R$20

## Descrição Funcional

### Funcionalidades

 - Regar a planta. Quando o sistema julgar necessário, através do sensor de umidade e da contagem de tempo desde a última ação de regar a planta.

### Configurabilidade

 - O usuário pode escolher de quanto em quanto tempo o sistema verifica a umidade das plantas. Por default, é estabelecido um intervalo de 4 horas;
 - Por ser portátil, o sistema pode ser colocado em qualquer local do estabelecimento onde o usuário julgue que fique bom esteticamente, adaptando aos móveis;
 - O usuário pode escolher o tamanho do reservatório de água pois ele pode ser qualquer utensílio doméstico, por exemplo: Pote, garrafa d'água, balde, etc (desde que fechado e higienizado).

### Eventos
|Periódicos (Padrão de 4 horas ou definido pelo usuário) | Não-periódicos (Dependem dos eventos periódicos)|
|--|--|
|Umidade baixa|Acionamento da bomba de água|
|Reservatório baixo|-|
|Status da bateria|-|

### Tratamento de Eventos
O sistema irá tratar os eventos de acordo com o estado da máquina naquele momento. Por exemplo, caso a máquina esteja no estado inicial ela irá seguir com a rotina de checagem antes de entrar na etapa de irrigação, isto é, irá verificar se: a) Bateria baixa, b) Reservatório baixo, c) Umidade baixa e d) Acionamento da bomba.

 - a) Bateria baixa: O sistema irá verificar o nível da bateria e decidir se está em estado crítico ou não.
Em estado crítico será acionado um LED vermelho para alertar o usuário e irá manter o estado atual até trocar a bateria.
Caso o estado não seja crítico, permitirá o processamento em paralelo do restante do sistema.
A checagem da bateria é realizada a cada 10 minutos
- b) Reservatório baixo: Abaixo de certo nível de água no reservatório o programa acionará o LED vermelho de alerta e manterá o problema em loop até que o reservatório seja preenchido. Com checagem de nível a cada 30 minutos.
- c) Umidade baixa: O sensor irá retornar a umidade da terra, abaixo de certo nível irá acionar a bomba de água para regar a planta, caso a umidade esteja alta, após um tempo de 4 horas por padrão (configurável pelo usuário) ele irá retornar ao estado inicial e passando por cada checagem novamente.
- d) Acionamento da bomba: Após a leitura da umidade, através do evento de umidade baixa a bomba será acionada e irá bombear água para a planta e após 1 minuto contado pelo microcontrolador, a bomba irá desligar. Um LED azul estará aceso enquanto a bomba estiver em funcionamento.

## Descrição Estrutural do Sistema

![Fluxograma](flowchart/regador_flowchart.png)

## Especificações

### Especificação Estrutural

|Componente|Funcionalidade|
|--|--|
|ATTiny43U|Unidade Micro-Controladora|
|LED Vermelho|Nível de água e bateria crítico|
|LED Amarelo|Nível de bateria baixo|
|LED Azul|Bombeamento de água ativo|
|Resistor|Para polarizar os LEDs (4 de 1kOhm)|
|Sensor de umidade|Verificar umidade do solo|
|Sensor de nível de água|Verificar nível do reservatório|
|Transistor|Acionamento da bomba|

|Item|Funcionalidade|
|--|--|
|Bateria 5V|Alimentar a UMC e demais componentes|
|Mini bomba d'água|Bombear água para a planta|
|Tubo|Levar água à planta|

O sensor de umidade será conectado a algum pino da entrada analógica digital do ATTiny43U.

Os LEDs serão conectados às entradas de propósito geral do ATTiny43U (GPIO) para pull-up.

O módulo responsável pela irrigação é composto por uma conexão para alimentar o sistema com água sendo um tubo e uma mini bomba d'água. O módulo precisará do sinal do sensor de umidade para irrigar a horta quando necessário. O sensor de umidade será conectado à um pino de entrada analógica do microcontrolador. Na parte de atuação do módulo de irrigação, será necessário uma saída de propósito geral para o sinal de controle do transistor que irá ativar/desativar a mini bomba d'água.

### Especificação de Algoritmos

Com base no fluxograma apresentado na descrição estrutural do sistema, definimos as seguintes variáveis e registradores utilizados para armazenar os dados do programa:

- 3 variáveis de 2 bytes para contar tempo

- 2 variáveis de 2 bytes para medir a bateria (VOLTAGE LOW e VOLTAGE HIGH)

- 2 variáveis de 2 bytes para armazenar o nível do sensor de nível de água (LIMIT LOW e LIMIT HIGH)

- 2 variáveis de 2 bytes para armazenar o nível do sensor de umidade (LIMIT LOW e LIMIT HIGH)

- 1 variável de 2 bytes para verificar o nível de bateria

- 1 registrador de 1 byte para utilização dos LEDs

- 1 bit para acionar o pino de controle da bomba

- 1 ADC de 10 bits para utilização do sensor de nível de água

- 1 ADC de 10 bits para utilização do sensor umidade

Verificação no datasheet do micro-controlador para medir o nível dela através do microcontrolador:

|ATtiny devices|Have ADC|Vbg as input|VCC as VREF|Conclusion|
|--|--|--|--|--|
|ATTiny43U|Yes|Yes, 1.1V|Yes|OK|

Snippet do código para verificar o nível da bateria utilizando o ADMUX interno.
```c++
1. Let Vbg act as ADC input.
ADC0.MUXPOS = ADC_MUXPOS_INTREF_gc /* ADC internal reference, the Vbg*/;
1. Let VCC act as ADC reference.
ADC0.CTRLC = ADC_PRESC_DIV2_gc /* CLK_PER divided by 2 */
 | ADC_REFSEL_VDDREF_gc /* Vdd (Vcc) be ADC reference */
 | 0 << ADC_SAMPCAP_bp /* Sample Capacitance Selection: disabled */;
1. Start the ADC and calculate the result.
float Vcc_value = 0 /* measured Vcc value */;
ADC0.CTRLA = 1 << ADC_ENABLE_bp /* ADC Enable: enabled */
 | 1 << ADC_FREERUN_bp /* ADC Free run mode: enabled */
 | ADC_RESSEL_10BIT_gc /* 10-bit mode */;
ADC0.COMMAND |= 1; // start running ADC
while(1) {
 if (ADC0.INTFLAGS)
 {
 Vcc_value = ( 0x400 * 1.1 ) / ADC0.RES /* calculate the Vcc value */;
 }
 }
```

## Referências

https://grupolenotre.com/post/qual-o-melhor-horario-para-regar-o-seu-jardim

https://www.amazon.com/ALAMSCN-Submersible-Aquariums-Fountain-Hydroponics/dp/B08PBQ1N1G/ref=sr_1_5?keywords=5v+water+pump&qid=1694209040&sr=8-5

https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-battery-life

https://curtocircuito.com.br/blog/Categoria%20Arduino/como-usar-um-sensor-de-nivel-de-agua

https://www.electronicshub.org/transistor-as-a-switch/#:~:text=Both%20NPN%20and%20PNP%20transistors,drive%20the%20high%2Dpower%20transistor

Datasheets:

https://curtocircuito.com.br/datasheet/sensor/nivel_de_agua_analogico.pdf

https://5.imimg.com/data5/IQ/GJ/PF/SELLER-1833510/dc-mini-submersible-water-pump.pdf

https://www.eletrogate.com/modulo-sensor-de-umidade-de-solo

https://www.e-lab.de/downloads/DOCs/Tiny43U.pdf

https://www.circuitlab.com/editor/#?id=wb7uaq4s4fb6

https://www.yuden.co.jp/productdata/catalog/mlcc06_e.pdf

https://assets.nexperia.com/documents/data-sheet/PMEG2010AEH_PMEG2010AET.pdf

https://www.mouser.com/datasheet/2/597/lps6235-270704.pdf

https://ww1.microchip.com/downloads/en/Appnotes/00002447A.pdf

https://www.molex.com/en-us/products/part-detail/510210200

http://www.diodes.com/assets/Datasheets/DMN10H220L.pdf

https://www.diodes.com/assets/Datasheets/DMP10H400SE.pdf