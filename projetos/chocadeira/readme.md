# `Chocadeira Automatizada`
# `Automatic Chicken Brooder`

## Apresentação
O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).


 |Nome  | RA | Curso|
|--|--|--|
| Pedro Henrique Ricci Sesti  | 185734  | Eng. Elétrica|
| Matheus Acauã Dias          | 241617  | Eng. Elétrica|


## Descrição do Projeto
A indústria agrícola é um pilar essencial da nossa sociedade, alimentando bilhões de pessoas em todo o mundo. No entanto, enfrenta desafios significativos, como a necessidade de aumentar a eficiência, reduzir o desperdício de recursos e atender à crescente demanda por alimentos de qualidade. A incubação de ovos é uma parte fundamental desse processo, mas é notoriamente trabalhosa e propensa a variações que podem resultar em perdas significativas.

É aqui que entra a nossa Chocadeira Automatizada. Nosso projeto tem como objetivo principal resolver o problema da incubação de ovos de maneira eficiente, confiável e sustentável.

## Descrição Funcional
### Funcionalidades
A Chocadeira Automatizada é um dispositivo projetado para incubação artificial de ovos de aves, como galinhas, patos ou codornas, em um ambiente controlado. Ela automatiza e monitora o processo de incubação, fornecendo condições ideais de temperatura, umidade e viragem dos ovos para garantir taxas de eclosão bem-sucedidas. A Chocadeira Automatizada desse projeto consiste em:

1. **Sistema de aquecimento:** o projeto consiste em um sistema de aquecimento controlado através da dimmerização de uma lâmpada que mantém a temperatura interna da chocadeira na faixa ideal para a incubação dos ovos.

2. **Controle de umidade:** a chocadeira possui um sistema para manter níveis de umidade adequados.

3. **Viragem automática:** para evitar que o embrião grude na casca e promover seu desenvolvimento uniforme, a Chocadeira Automatizada gira os ovos em intervalos regulares.

### Configurabilidade
**Temperatura:** A temperatura da chocadeira é ajustada de acordo com as especificações da espécie. Isso pode incluir a capacidade de ajustar a temperatura de incubação e, em alguns casos, a temperatura de eclosão. No caso para ovos de galinha a temperatura será fixa em 37,7 °C.

**Umidade:** A configurabilidade da umidade é fundamental para criar as condições ideais para o desenvolvimento dos embriões. Para ovos de galinha o ideal é que a humidade esteja em torno de 70%.

**Viragem dos ovos:** a chocadeira permite que o usuário configure a frequência da viragem automática dos ovos. Além disso, a viragem automática será desativada quando faltar menos de 4 dias para a eclosão.

### Eventos
#### Periódicos:

1. **Viragem automática dos ovos:** a viragem dos ovos é um evento periódico que ocorre a cada hora durante os primeiros 18 dias de incubação.

2. **Monitoramento da temperatura:** o monitoramento da temperatura é um evento periódico que ocorre continuamente, com leituras geralmente feitas a cada poucos minutos para garantir que a temperatura permaneça dentro da faixa ideal.

3. **Monitoramento da umidade:** o monitoramento da umidade é outro evento periódico que ocorre continuamente, com leituras geralmente feitas a cada poucos minutos para garantir que a umidade esteja dentro da faixa desejada.

#### Não-Periódicos:

1. **Inserção dos ovos:** quando o usuário prepara a chocadeira para uma nova incubação, insere os ovos no início do processo.

2. **Configuração inicial:** o usuário configura os parâmetros iniciais, como temperatura, umidade e frequência de viragem, no início do processo.

3. **Fim da incubação:** quando a incubação atinge seu término, ocorre o evento de eclosão, onde os pintinhos nascem dos ovos.

4. **Manutenção e limpeza:** a manutenção e a limpeza da chocadeira são eventos não-periódicos, mas importantes, que podem ocorrer em intervalos irregulares, dependendo da necessidade 

### Tratamento de Eventos

![Draw.io](https://github.com/pedrosesti/ea075-2023.2/blob/main/projetos/chocadeira/chocadeira.drawio.png)

## Especificação Estrutural

### Unidade Micro-Controladora:
1. A unidade micro-controladora escolhida para o projeto é o Microcontrolador AVR ATmega328P, devido à sua confiabilidade e ampla aceitação na comunidade de projetos embarcados.

### Periféricos de Entrada e Saída:
1. **Sensor de Temperatura e Umidade:** Será utilizado um sensor DHT11 para monitorar a temperatura e a umidade dentro da chocadeira.
2. **Atuador de Aquecimento:** Um elemento de aquecimento será controlado para manter a temperatura interna dentro dos limites desejados.
3. **Ventilador:** Um ventilador será usado para garantir a circulação adequada do ar dentro da chocadeira.
4. **Tela de Exibição:** Uma tela LCD será utilizada para mostrar informações relevantes aos usuários, como temperatura, umidade e status dos ovos.
   
### Circuitos de Interface:
1. **Conversor Analógico-Digital (ADC):** Um ADC será utilizado para converter sinais analógicos do sensor de temperatura e umidade para valores digitais processáveis pelo microcontrolador.
2. **Conversor Digital-Analógico (DAC):** Um DAC pode ser utilizado para controlar o aquecedor, ajustando a potência de acordo com a temperatura desejada.
3. **Comunicação:** A comunicação será realizada principalmente via I2C para garantir uma transferência de dados eficiente entre os dispositivos periféricos e o microcontrolador.
4. **Circuito de Sincronização de Sinais Temporais:** Um circuito de sincronização será implementado para garantir a sincronia adequada entre os diferentes componentes, especialmente o ventilador e o aquecedor.

### Restrições Físicas e Ambientais:

1. **Dimensões:** A chocadeira terá dimensões de 50 cm (largura) x 50 cm (altura) x 60 cm (profundidade) para acomodar uma quantidade significativa de ovos.
2. **Dissipação Térmica:** O sistema será projetado para dissipar calor de forma eficiente, evitando superaquecimento e mantendo uma temperatura interna estável.
   
## Especificação de Algoritmos

## Algoritmo de Controle de Temperatura e Umidade:
### Inicialização:
1. Inicializar o sistema e calibrar os sensores.
2. Configurar os pinos de entrada/saída do microcontrolador.
3. Inicializar a tela LCD para exibir informações.

### Loop Principal:
1. Ler os valores do sensor de temperatura e umidade.
2. Comparar os valores lidos com os limites predefinidos.
3. Ativar o aquecedor ou o ventilador conforme necessário para manter a temperatura e umidade dentro dos limites aceitáveis.
4. Atualizar a tela LCD com os valores atuais de temperatura e umidade.


## Referências
Material da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*
Standalone arduino: https://www.youtube.com/watch?v=RvBLmwF8JIE&t=477s
Datasheet do display: https://www.usinainfo.com.br/index.php?controller=attachment&id_attachment=131
Datasheet do cristal oscilador: https://www.eletrogate.com/cristal-oscilador-16mhz
Datasheet do micocontrolador ATMEGA328P: https://www.ic-components.hk/files/cb/DEV-14083.pdf
Dimmer arduino: https://www.youtube.com/watch?v=_vMG9QmPtNE&t=356s
