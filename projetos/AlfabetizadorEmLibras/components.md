## Introdução
Este arquivo tem como objetivo listar os componentes escolhidos para a elaboração do projeto Alfabetizador em Libras, no qual será citada a justificativa de seu uso e seu respectivo datasheet, quando disponível para acesso.

## Componentes
- **Botão**: Push button GV4-C-008 de 6x6x5mm, com tensão máxima de operação em 12V, corrente máxima de 0,5A e peso de 0,3g. Foi escolhido para o projeto devido ao baixo custo (R$0,25 por unidade) e atendimento do requisito para acionamento do circuito através da lógica de pull-up, a fim de evitar variações desnecessárias na entrada do microcontrolador. Este item não possui datasheet, porém o link para especificações está disponível em: https://www.eletrogate.com/push-button-chave-tactil-6x6x6mm

- **Sensor**: Microfone com amplificador no modelo MAX4466. Foi escolhido por conta da baixa voltagem de operação (2.4V a 5.5V) e por ser especificado como ideal para utilização em ambientes ruidosos, uma vez que é necessário minimizar o ruído do sinal captado devido a necessidade do processamento de voz no projeto.
Seu datasheet está disponível em: https://pdf1.alldatasheet.com/datasheet-pdf/view/73367/MAXIM/MAX4466.html

- **Filtro**: Após análise do circuito com o auxílio do PAD da disciplina, identificamos que não será necessária a utilização do filtro que faria conexão entre o sensor e o microcontrolador, dessa forma, esse componente não fará mais parte do circuito pois o sinal analógico emitido pelo sensor é diretamente compatível com a entrada analógica do microcontrolador.
(substituir por divisor de tensão)

- **Microcontrolador**: O microcontrolador escolhido foi o ESP32, devido a sua possibilidade de uso com aplicações de audio, entrada analógica de sinal (necessária devido a saída analógica do sensor) e quantidade suficiente de pinos para a conexão com os treze atuadores. Seu datasheet está disponível em: https://pdf1.alldatasheet.com/datasheet-pdf/view/1148023/ESPRESSIF/ESP32.html.

- **Conversor de nível lógico 3,3V-5V**: O conversor de nível lógico 3.3V-5V bidirecional com 8 canais **CNL8** foi substituído pelo conversor de nível lógico bidirecional 3,3V-5V no modelo **BSS138**, pois ele é ideal para aplicações com baixa corrente como é o caso da utilização de servo-motores, que é o previsto para esse projeto, além do tamanho físico reduzido em comparação ao CNL8. Seu datasheet está disponível em: https://cdn.awsli.com.br/945/945993/arquivos/BSS138.pdf. 

- **Servo motores**: 13 micro servo-motores 9g SG90 com tamanho aproximado de 22.2x11.8x31mm e voltagem de operação de 4.8V (aproximadamente 5V). Foram escolhidos devido ao tamanho adequado para montagem da estrutura física da mão robótica em tamanho real. Seu datasheet está disponível em: https://pdf1.alldatasheet.com/datasheet-pdf/view/1572383/ETC/SG90.html.

- **Fonte de alimentação**: Para o circuito, a fonte escolhida é uma fonte LiPO de 5V para alimentação da ESP32 com conector micro-USB e uma segunda fonte com as mesmas especificações para a alimentação dos servo-motores, porém com conexão a um adaptador DC Power Jack de dois fios. Modelos semelhantes aos esperados podem ser encontrados em: 
https://www.robocore.net/acessorios-raspberry-pi/fonte-chaveada-5v-3a?gad_source=1&gclid=Cj0KCQiA67CrBhC1ARIsACKAa8S9v4JIgiPzvwi2AIoa48Tf8U4bnOohH93T4OX_Son_fc5yCwUwXCcaAr4SEALw_wcB
https://www.amazon.com.br/Fonte-Estabilizada-Chaveada-Bivolt-5-5mm/dp/B082XK9F28/ref=asc_df_B082XK9F28/?tag=googleshopp00-20&linkCode=df0&hvadid=647747402352&hvpos=&hvnetw=g&hvrand=6919078278302083958&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001729&hvtargid=pla-2066362067708&psc=1&mcid=912931c701d93237b38bd582d6f24841

