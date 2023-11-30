# `Componentes Utilizados`

## Placa Wemos D1 Mini Pro Wifi ESP8266
[Datasheet](./datasheets/ESP8266EX.PDF)

Escolhemos utilizar esse módulo porque este possui uma memória EEPROM de 4MB, além de uma flash de 32MB, nas quais podemos salvar os dados do sensor de forma segura. Tem também um  módulo wi-fi para podermos receber com praticidade os dados de log do vôo. Além disso, o layout da placa é compacto, e conta com o necessário para o nosso projeto, o tamanho e consumo reduzidos são essenciais para o projeto, pois ele deve interferir minimamento no peso e na aerodinâmica do foguete.

## Sensor de Pressão e Temperatura BMP280
[Datasheet](./datasheets/BST-BMP280-DS001-11.pdf)

A ideia é comunicar o módulo BMP280 com o ESP8266 via I2C, pois ambos os dispositivos fornecem essa interface. Como vamos fazer uma leitura a cada 50ms, não é necessário um protocolo mais veloz, que seria o caso do SPI, além de que o I2C necessita de menos conexões. Além disso, o BMP280 possui uma acuracia de $\pm 0.12hPa (1m)$ e implementa um filtro IIR, que pode ser configurado via Software. Sua tensão de operação é de 1.8V a 3.6V, sendo a saída de 3.3V do microcontrolador suficiente para alimentação, e seu consumo de corrente em operação é de $2.7 \mu A$.

## Borne KRE KF128 2 Vias
[Datasheet](./datasheets/KF128.PDF)

Será utilizado para fabricar o switch RBF , e possuirá um jumper conectado. Essa interface conta com dois pinos, sendo um deles o VCC e outro uma GPIO do microcontrolador. Quando o RBF estiver inserido, o pino estará conectado ao VCC. Quando estiver removido, o pino estará conectado ao GND por meio de um sistema de pull-down.

## Chave Gangorra KCD1-106N
[Datasheet](./datasheets/KCD1-104.PDF)

## Regulador de Tensão Ajustável TL431
[Datasheet](./datasheets/tl431.pdf)

O componente fornecerá a tensão correta (3.3V) na entrada da placa, conectando este à alimentação da bateria

## Bateria LiIon 18650
[Datasheet](./datasheets/SAMSUNG%20INR18650-25R.pdf)

Essa bateria possui uma carga de 2500mAh, o que, considerando um consumo típico do ESP8266 de 70mA, é suficiente para aproximadamente 28 horas de operação. 