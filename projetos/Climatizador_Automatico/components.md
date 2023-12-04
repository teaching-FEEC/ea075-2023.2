## Circuito

### Relê: 

https://www.circuitbasics.com/wp-content/uploads/2015/11/SRD-05VDC-SL-C-Datasheet.pdf 

Foi escolhido por conta da alimentação de 5V que facilita o projeto levando em conta que já temos uma saída 5V da placa utilizada, além de que ele tem uma grande capacidade de chaveamento de corrente para acionar as cargas, com um contato capaz de receber até 30A, mais do que o suficiente para acionar as ventoinhas e os demais componentes.

### Transistor BC548:

https://html.alldatasheet.com/html-pdf/857905/SUNMATE/BC548/292/1/BC548.html

Foi escolhido por conta da capacidade de corrente de coletor de 100mA que é mais do que o suficiente para acionar as bobinas dos relês e chavear o acionamento deles dissipando potência suficiente para o funcionamento correto.

### Fonte 12 V

https://produto.mercadolivre.com.br/MLB-2011902230-fonte-12v-5a-bivolt-preta-5-amperes-plug-p4-_JM

Escolhida pois é a maior tensão utilizada no circuito, foi feita também uma retificação para 9V e 5V. Além de ter corrente de 5A, que é mais do que o suficiente para alimentar todo o circuito.

### Conector da fonte:

https://www.baudaeletronica.com.br/produto/jack-p4-femea-para-placa-de-circuito-impresso-21-5x5mm.html

Escolhido para ser compatível com o conector da fonte (Jack P4)

### Zener:

https://www.alldatasheet.com/datasheet-pdf/pdf/1241411/BYTESONIC/1N4733.html

Escolhido por ter 9V de tensão Zenner para alimentar algumas partes do circuito, além de ter corrente e potência necessária para alimentar o circuito, foi a forma que achamos mais fácil de regular a tensão já retificada da fonte.

### Regulador de 5V:

https://www.sparkfun.com/datasheets/Components/LM7805.pdf

Escolhido para a alimentação 5V, foi escolhido pois já é comunmente usado em soluções, é de fácil uso e ocupa pouco espaço na placa.

### Microcontrolador

https://www.nxp.com/docs/en/data-sheet/KL25P80M48SF0.pdf

Escolhido com base na capacidade de I/Os que são suficientes para nossa aplicação que usa uma quantidade relativamente alta de entradas e saídas ele tem uma memória embutida para carregar o código de controle do climatizador e ele tem um bom custo beneficio de micro-controlador com memória.

## Dispositivos de Entrada

### DHT 11:

https://pdf1.alldatasheet.com/datasheet-pdf/download/1440068/ETC/DHT11.html 

Foi escolhido pois ter o melhor custo beneficio para a nossa aplicação em comparação com outros sensores apresentando uma precisão dentro do valor esperadop por um baixo custo.

## Dispositivos de Saída

### Ventoinhas:

https://produto.mercadolivre.com.br/MLB-3343399239-kit-3-pecas-ventilador-cooler-ventoinha-80x80x25mm-12v-_JM

Foi escolhido esse conjunto de ventoinhas pois são compatíveis em tensão e corrente com nosso circuito e tem capacidade suficiente de extrair o calor do lado quente da pastilha térmica assim como realizar a circulação do ar através do dissipador no lado frio.

### Atomizador para o humidificador de ar:

https://pt.aliexpress.com/item/32848489683.html

Escolhido por ser de fácil aplicação e baixo custo, além de uma ótima capacidade de umidificação do ar, o que o torna ideal para nossa aplicação

### Pastilha térmica:

https://produto.mercadolivre.com.br/MLB-2796487260-pastilha-termoeletrica-peltier-tec1-12710-40x40mm-12v-92w-_JM 

Foi escolhida por ser compatível com a tensão de alimentação do nosso circuito, além de uma alta capacidade de resfriar rapidamente, que é o desejado para a nossa aplicação, e possui um ótimo custo benefício para o projeto.

### display LCD:

https://www.es.co.th/Schemetic/PDF/LCD-016N002L.PDF 

Foi escolhido por possuir 12 colunas e 2 linhas que é o suficiente para mostrar as informações e menus que a gente precisa, e funciona com 8 bits, ou seja não vai demandar um numero excessivo de saídas do micro, sobrando assim espaço para outros componentes I/O.
