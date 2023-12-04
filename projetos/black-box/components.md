# `Componentes Utilizados`

## Placa Wemos D1 Mini Pro Wifi ESP8266
[Datasheet](./datasheets/ESP8266EX.PDF)

Antes desse módulo ser escolhido, escolhemos que iríamos utilizar o microcontrolador ESP8266. Essa escolha foi feita levando em consideração a memória para salvarmos os dados, já que ele emula um trecho da memória flash como EEPROM, possibilitando a leitura e escrita persistente de valores. Ele também oferece uma comunicação via wifi, tornando possível a comunicação sem fio para recuperação dos dados. Tudo isso é feito com um baixo consumo de energia, e com alta frequência de operação do microcontrolador.
Tendo isso em vista, escolhemos o Wemos-D1-Mini por ser um módulo que oferece todas essas funcionalidades do ESP8266 com um tamanho físico reduzido e com um número de pinos também reduzidos, porém mais que suficientes para a aplicação aqui desenvolvida.

Escolhemos utilizar esse módulo porque este possui uma memória EEPROM de 4MB, além de uma flash de 32MB, nas quais podemos salvar os dados do sensor de forma segura. Tem também um  módulo wi-fi para podermos receber com praticidade os dados de log do vôo. Além disso, o layout da placa é compacto, e conta com o necessário para o nosso projeto, o tamanho e consumo reduzidos são essenciais para o projeto, pois ele deve interferir minimamento no peso e na aerodinâmica do foguete.

## Sensor de Pressão e Temperatura BMP280
[Datasheet](./datasheets/BST-BMP280-DS001-11.pdf)

O módulo barômetro BMP280 foi escolhido como altímetro pois é um dispositivo amplamente utilizado em aplicações semelhantes a descrita nesse projeto. Isso faz com que hajam diversas referências sobre como utilizar o dispositivo, além de ser mais fácil/barato de adquirir. Além disso, ele disponibiliza interfaces de comunicação I2C e SPI, possibilitando a interface com um microcontrolador.
A ideia é comunicar o módulo BMP280 com o ESP8266 via I2C, pois ambos os dispositivos fornecem essa interface. Como vamos fazer uma leitura a cada 50ms, não é necessário um protocolo mais veloz, que seria o caso do SPI, além de que o I2C necessita de menos conexões. Além disso, o BMP280 possui uma acuracia de $\pm 0.12hPa (1m)$ e implementa um filtro IIR, que pode ser configurado via Software. Sua tensão de operação é de 1.8V a 3.6V, sendo a saída de 3.3V do microcontrolador suficiente para alimentação, e seu consumo de corrente em operação é de $2.7 \mu A$.

## Borne KRE KF128 2 Vias
[Datasheet](./datasheets/KF128.PDF)

Será utilizado para fabricar o switch RBF , e possuirá um jumper conectado. Essa interface conta com dois pinos, sendo um deles o VCC e outro uma GPIO do microcontrolador. Quando o RBF estiver inserido, o pino estará conectado ao VCC. Quando estiver removido, o pino estará conectado ao GND por meio de um sistema de pull-down.

## Regulador de Tensão Ajustável TL431
[Datasheet](./datasheets/tl431.pdf)

O regulador foi escolhido entre os reguladores disponíveis na loja em que foram comprados os demais módulos. A escolha foi feita levando em consideração a capacidade de oferecer 3.3v aos dispositivos a partir de 3.7v de entrada (bateria) que pode diminuir com o tempo, conforme a bateria for sendo utilizada. Para isso, também é necessário utilizar três resistores (82Ω, 1kΩ e 3kΩ) e um capacitor de desacoplamento (100nF).

## Bateria LiIon 18650
[Datasheet](./datasheets/SAMSUNG%20INR18650-25R.pdf)

Essa bateria possui uma carga de 2500mAh, o que, considerando um consumo típico do ESP8266 de 70mA, é suficiente para aproximadamente 28 horas de operação. 


