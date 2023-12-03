# `<Gerenciamento das condições internas de uma residência: controle de temperatura e ventilação>`
# `<Management of a house's internal conditions: temperature and ventilation control>`

## Apresentação (MANTER)

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas.
> |Nome  | RA | Curso|
|--|--|--|
| Bruno Moreira Pilarski | 195119 | Eng. Elétrica|
| Felipe Martins Nogueira | 167263 | Eng. Elétrica|

## Arquivos Importantes (:warning: NOVO :warning:)

>[Esquemático em PDF](link para imagens/pdf esquemático)
>
>[Lista de Componentes](link para components.md)
>
>[PCB](link para imagens/pdf PCB)

## Descrição do Projeto (:warning: ATUALIZAR :warning:)

O propósito deste projeto é empregar uma variedade de sensores capazes de diagnosticar as condições climáticas, tais como umidade e temperatura, a fim de auxiliar no gerenciamento das condições internas de um espaço fechado. Esse conceito pode ser extrapolado para uma ampla gama de ambientes que buscam o controle da temperatura interna, fazendo uso das condições externas favoráveis, como exemplificado pelo caso de um Contêiner Data Center. Apesar de possuir a possibilidade de tais extrapolações, este projeto será conduzido tomando como base o controle interno de uma residência. Com o dispositivo em mãos, o usuário diminuirá o tempo despendido no gerenciamento e controle da temperatura da sua residência. A instalação deve ser conduzida a partir das instruções apresentadas no manual.

O presente projeto não apresenta um nível de complexidade elevado. A configurabilidade tende a evoluir à medida que o know-how e conhecimento interdiciplinar evoluirem. Ao longo do processo de desenvolvimento do projeto, não forma observados potências trade offs que pudessem comprometer o desenvolvimento do projeto. A velocidade de processamento das informações, eficiência energética, e risco à segurança do usuário foram alguns dos fatores considerados e que, em última instância, apresentam um baixo nível de comprometimento ao desenvolvimento do projeto. 


## Descrição Funcional (:warning: ATUALIZAR :warning:)

O sistema em questão deve ser capaz de diagnosticar, por meio de sensores, as mudanças de temperatura externa e a presença de chuva. A partir desses dados, ou variáveis de controle, o sistema embarcado determinará se a janela ou permanecerá aberta ou fechada, bem como o ligamento do ar condicionado.. Ou seja, há dois inputs principais a serem considerados neste projeto. Faaz-se necessário retificar que o projeto é orientado ao atendimento de demandas em residências.


### Funcionalidades (ATUALIZAÇÃO NECESSÁRIA)

Detectar a presença de chuva e solicitar o fechamento das janelas;
Comparar o nível de temperatura interna e externa. A partir dessa diferença, liga ou desliga o ar condicionado, bem como indicar se a janela deverá ou não ser fechada.

### Configurabilidade

O desenvolvimento do projeto em questão considera duas possíveis configurações de operação. A primeira delas consiste na operação padrão do dispositivo. O sensor estão configirurado para operar em uma temperatura de 22ºC. Dessa forma, as regras de controle obedecerão e critério de decisão obederão esse padrão de temperatura.

Já no modo híbrido, é possível  modificar o valor da temperatura de acordo com o desejado pelo cliente. O range de temperatura varia de 16ºC a 30ºC. Essa faixa de temperatura tem como referência a própria capacidade de resfriamento do ar-condicionado padrão.

### Eventos

O dispositivo, a princípio, tem seu desenvolvimento orientado a climas tropicais. Em algumas regiões do Brasil, por exemplo, podemos identificar fenômenos climáticos endêmicos,isto é, próprios do local considerado. De forma geral, o sistema embarcado é capaz de lidar com os seguintes eventos: Medição de temperatura e humidade interna: ao aferir a temperatura, o dispositivo comparará com o valor e temperatura definido e fara a conferência, conforme apresentado no fluxo, das informações obtidas pelos sensores. Assim, a primeira frente de tratamento de eventos está voltada ao tratamento de humidade e temperatura. 

Detecção de Chuva - O sistema é capaz de detectar a presença da chuva em diferentes intensidades, isto é, fraca, média e forte ( no fluxograma, a chuva não foi considerada ). Ao identificar que a chuva está chegando, as janelas serão fechadas e o ar condicionado, ligado. 

Os eventos relacionados a temperatura, humidade e chuva podem sofrer alterações de forma gradual ou abrupta. Podemos citar a chuva como exemplo. Às vezes, é um chuva muito breve, causada pela passagem de uma núvem específica. Por esse motivo, a conferênciaas das variávris e feita a cada três minutos, a fim de evitar que a janela permança fechada na ausência de chuva.  


### Tratamento de Eventos

Para os dispositivos de saída não sejam alterados a cada grande mudança na abertura da janela ou no ar-condicionado, o sistema fará uma inspeção, a cada 3 min, das variáveis de entrada. No entanto, ao fim do período de coleta dos dados, antes da N-ésima tomade de decisão, cerca de 5% dos dados encontrados serão expurgados. Esse valor é pensado para os casos em que uma mudança pontual ocorra no sistema ( ambiente ) mas que não representada o estado em regime permanente daquele sistema.

No primeiro bloco de tratamento, o conjunto de eventos considerados está relacionado à interrupção por chuva. O segundo bloco de eventos está relacionado ao tratamento avaliação da humidadade do interior da casa ou quarto considerado. 

Neste projeto, estamos considerando que a leitura dos dois tipos de eventos seguem alógica OR, pois eles podem estar ocorrendo simultaneamente.  Em aplicações futuras, será possível adicionar critérios de interrupação mais precisos, que também considerem a ação do vento. 


## Descrição Estrutural do Sistema (:warning: ATUALIZAR :warning:)
> A descrição estrutural do sistema ( modificada ) é dada por:

[Descrição estrutural do sistema.pdf](https://github.com/f741963/ea075-2023.2/files/13539960/Descricao.estrutural.do.sistema.pdf)


## Especificações (:warning: ATUALIZAR :warning:)

### Especificação Estrutural

Na PCB desenvolvida temos a presença dos seguintes componentes::

Botão Switch - Responsável pelo ligamento de desligamento do circuito;
3 Reles do tipo biestável 314A24 ( Datasheet ) 
Atmega328 
Placas de cobre para forma a PCB. 
3 Resistores;
2 sensores digitais de humidade e temperatura DHT22 ( Datasheet ) 

Os  componentes externos à placa são: 

1 Módulo sensore de chuva - Datasheet
1 Módulo fim de curso ( Datasheet )
1 Motor para controlar a abertura da janela. 


O Atmega328 é o CI principal responsável pelo gerenciamento das informações. Por meio dos inputs obtidos durante o perído de amostragem, ele produz os outputs necessários para executar as ações prestabelcidas.  Os periféricos de entrada são: sensores de temperatura e humidade, detector de chuva, módulo fiim de curso. Os periféricos de saída são: motores e reles. A temporização e controles de temporização estão definidos no CI. 

É recomendável que o embarcado esteja em um posição do ambiente isenta de influência de outros equipamentos emissores de energia que  podem, eventualmente, produzir inputs indesejados na entrada dos sensores ( fogueira, equipamentos com alta dissipação de calor e afins ). 


### Especificação de Algoritmos (:warning: ATUALIZAR :warning:)

## Referências (:warning: ATUALIZAR :warning:)
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
