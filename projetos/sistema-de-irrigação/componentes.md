# Componentes

## Microcontrolador PIC18F4550

[Datasheet Link](https://www.microchip.com/en-us/product/pic18f4550)

Este microcontrolador possui 8 entradas analógicas, que são mais do que o suficientes para os sensores que serão utilizados. Para armazenar os dados dos sensores, o dispositivo disponibiliza duas memórias não voláteis: uma EEPROM  de 256 Kbytes, possibilitando realizar a leitura e escrita de dados; uma memória Flash com capacidade de 32 KB de memória (neste caso, para armazenamento de programas). Para comunicação serial, oferece uma comunicação serial que utiliza o o módulo com protocolo I2C, possibilitando enviar dados ao display. Além disso, possui uma estrutura de oscilação flexível, por exemplo possui quatro modos Crystal, dois modos de relógio externo (até 48 MHz). Por fim, O microcontrolador possui uma tecnologia de nanoWatt, que é para baixo consumo, que é importante para o projeto visto que será utilizado por períodos longos.

## Display LCD 16x2 - LM16255K

[Datasheet Link](https://pdf.datasheetcatalog.com/datasheet/Sharp/mXvtrzw.pdf)

Este display pode operar em um range de temperatura -25 a 70 °C, sendo importante para o projeto, pois pode ser aplicado para diversos ambientes (temperaturas muito diferentes). Possui entradas digitais para receber os dados da comunicação serial (protocolo I2C).

## Expansor PCF8574

[Datasheet Link](https://www.nxp.com/docs/en/data-sheet/PCF8574_PCF8574A.pdf)

Este dispositivo fornece uma expansão de E/S remota de uso geral para a maioria das famílias de microcontroladores por meio da interface I2C, que é a interface de comunicação serial do microcontrolador. Além disso, oferece um baixo consumo de corrente de Standby de 10 μA (máximo). O PCF8574 fornece 8 pinos de E/S digitais configuráveis, sendo que cada pino pode ser utilizado como entrada ou saída. 

## Sensor FC-28

[Datasheet Link](https://www.datasheethub.com/wp-content/uploads/2022/08/SEN0114_Web.pdf)

O sensor de umidade do solo FC-28 opera com uma faixa de voltagem de 3.3V a 5V, com uma corrente de operação inferior a 20mA. Seu design modular permite fácil integração, e sua saída analógica varia de acordo com os níveis de umidade do solo. 

## Sensor DHT-11

[Datasheet Link](https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf)

O Sensor de umidade e temperatura DHT-11 é compatível com uma faixa de operação de 3.3V a 5V. Oferece uma precisão de ±5% para umidade e ±2°C para temperatura, aliada à saída digital, torna-o ideal para aplicações que demandam controle climático, como em sistemas de monitoramento ambiental e automação residencial.

## Cristal oscilador HC-49S

[Datasheet Link](https://pdf1.alldatasheet.com/datasheet-pdf/download/136608/KSS/HC49S.html)

O Cristal Oscilador HC-49S é um componente eletrônico que realiza a geração de sinais estáveis em circuitos. Com um invólucro metálico, o HC-49S, incorpora um cristal de quartzo interno que vibra quando energizado, oferecendo uma referência precisa de frequência.
<!-- 
## Capacitor GCM1885C1H150JA16D

O Capacitor GCM1885C1H150JA16D é um componente eletrônico essencial para armazenar e liberar carga em circuitos. Pertencente à série GCM, possui uma capacitância de 15 pF, uma tensão nominal de 50 V e uma tolerância de ±5%. -->

## Transistor BC547

[Datasheet Link](https://pdf1.alldatasheet.com/datasheet-pdf/download/586720/FAIRCHILD/BC547.html)

Este transistor NPN possui uma corrente de coletor baixa de 100mA, que neste caso permite ter um consumo reduzido para o projeto. Também oferece um ganho de corrente em DC de no mínimo de 110 e no máximo 800 (para uma tensão entre o coletor e emissor de VCE = 5V, e uma corrente de coletor de IC = 2mA), com isso, pode-se utilizar para amplificar o sinal de saída do microcontrolador e enviar para o sistema Relé-Solenóide.

## Relé ADW11

[Datasheet Link](https://www.mouser.com/datasheet/2/316/mech_eng_dw-481172.pdf)

O Relé ADW11 é um dispositivo eletromecânico versátil usado para controlar circuitos elétricos de alta potência por meio de um sinal de baixa potência. Ele possui quatro terminais principais, sendo comumente usado para alternar entre circuitos abertos e fechados em aplicações industriais e automotivas.

## Retificador 1N4007

[Datasheet Link](https://www.diodes.com/assets/Datasheets/ds28002.pdf)

O Retificador 1N4007 é um diodo retificador de uso geral que converte corrente alternada (CA) em corrente contínua (CC). Pertencente à série 1N, este diodo é eficiente em aplicações de baixa frequência e alta corrente.

## Válvula de Vazão Solenóide Água 12VDC

[Datasheet Link](https://www.moduloeletronica.com.br/produto/valvula-de-vazao-solenoide-12v-12-polegadas-dn15/4787557)

A Válvula de Vazão Solenóide para Água 12VDC é um componente eletromecânico que controla o fluxo de água em sistemas automatizados. Operando mediante o princípio de um solenoide, esta válvula é projetada para ser acionada por uma tensão de 12 volts.