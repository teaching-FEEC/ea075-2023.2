# `<Gerenciamento das condições internas de uma residência: controle de temperatura e ventilação>`
# `<Management of a house's internal conditions: temperature and ventilation control>`

## Apresentação (MANTER)

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas.
> |Nome  | RA | Curso|
> |--|--|--|
> | Bruno Moreira Pilarski | 195119 | Eng. Elétrica|
> | Felipe Martins Nogueira | 167263 | Eng. Elétrica|

## Arquivos Importantes (:warning: NOVO :warning:)

>[Esquemático em PDF](link para imagens/pdf esquemático)
>
>[Lista de Componentes](link para components.md)
>
>[PCB](link para imagens/pdf PCB)

## Descrição do Projeto (:warning: ATUALIZAR :warning:)
> Deve refletir a última versão do projeto.
>
>O propósito deste projeto é empregar uma variedade de sensores capazes de diagnosticar as condições climáticas, tais como umidade, velocidade relativa do vento e temperatura, a fim de auxiliar no gerenciamento das condições internas de um espaço fechado. Esse conceito pode ser extrapolado para uma ampla gama de ambientes que buscam o controle da temperatura interna, fazendo uso das condições externas favoráveis, como exemplificado pelo caso de um Contêiner Data Center. Apesar de possuir a possibilidade de tais extrapolações, este projeto será conduzido tomando como base o controle interno de uma residência. Com o dispositivo em mãos, o usuário diminuirá o tempo despendido no gerenciamento e controle da temperatura da sua residência. A instalação deve ser conduzida a partir das instruções apresentadas no manual.
>

## Descrição Funcional (:warning: ATUALIZAR :warning:)

 > O sistema em questão deve ser capaz de diagnosticar, por meio de sensores, as mudanças de temperatura externa, probabilidade de chuva e a temperatura relativa do vento. A partir desses dados, ou variáveis de controle, o dispositivo determinará o grau/nível de abertura das janelas e a temperatura gerada pelo ar-condicionado do local. Ou seja, há dois inputs principais a serem considerados neste projeto. Conforme mencionado inicialmente, o projeto é voltado para aplicações residenciais. Na figura a seguir, temos um exemplo de uma residência e a vista superior dela. A seta indica a janela em que o embarcado construído pode atuar.


### Funcionalidades (ATUALIZAÇÃO NECESSÁRIA)
> Detalhe todas as tarefas que o sistema será capaz de executar

### Configurabilidade
> Detalhe, se houver, todas as possíveis configurações do circuito e todos os pontos de alteração da configuração.

### Eventos
> Quais eventos o sistema deve tratar?
> Se aplicável, classifique os eventos que são periódicos (procure especificar a periodicidade) e os que são não-periódicos
> (qual o tempo mínimo entre dois eventos sucessivos)?

### Tratamento de Eventos
> Qual comportamento o sistema deve ter para tratar corretamente cada evento?

## Descrição Estrutural do Sistema (:warning: ATUALIZAR :warning:)
> Junto com a descrição do comportamento do sistema, deve-se especificar, em nível de bloco ou sistema, a estrutura necessária 
> para captar os eventos do mundo externo, para alojar e processar o programa de tratamento de eventos, e para atuar sobre o mundo externo.
>
> Para essa descrição recomenda-se a criação de diagramas de blocos.
> Nesse diagrama, devem ser destacados os blocos funcionais que compõem o sistema, incluindo uma síntese das funcionalidades de cada bloco.
> Além disso, deve-se esclarecer também o relacionamento entre estes blocos, incluindo os principais sinais de comunicação entre
> os blocos de forma a assegurar a execução de todas as tarefas que o sistema deve realizar.
Esq> 
> Você sabia? Ferramentas como o `draw.io` permitem integração com o Github.

## Especificações (:warning: ATUALIZAR :warning:)

### Especificação Estrutural

> (Se preferir, adicione um link para o documento de especificação estrutural)
> 
> Entende-se por estrutural a descrição tanto das características elétricas e temporais como das restrições físicas de cada bloco funcional.
> Nessa etapa do projeto, ainda não será solicitado o diagrama elétrico mas espera-se que já estejam identificados os componentes e circuitos integrados propostos
> para implementação do sistema embarcado proposto.
> 
> Como o projeto de um sistema embarcado é centralizado nas tarefas, recomenda-se iniciar com a definição dos periféricos de entrada e saída (atuadores e/ou sensores) apropriados para o
> sistema. Pode ser necessário definir um endereço distinto para cada um deles. 
> Este endereço será utilizado pela unidade micro-controladora para acessá-los tanto para leitura como para escrita.

> Nesta etapa do projeto espera-se que a unidade micro-controladora seja definida.
> Tendo definidos os periféricos e a memória, é possível projetar um decodificador de endereços
> que converte o endereço referenciado no programa em sinal *Chip Select – CS* do dispositivo
> correspondente, habilitando-o para realizar um ciclo de leitura ou de escrita.
> 
> Nesta etapa do projeto espera-se que sejam identificada também a eventual necessidade do projeto de circuitos de interface para os periféricos do projeto.
> Assim, devem ser incluídos na especificação, se necessário:
> - conversores AD e DA;
> - padrões de comunicação a serem adotados;
> - circuitos de sincronização de sinais temporais.
> 
> Finalmente, deve-se especificar as restrições físicas e ambientais de funcionamento do circuito, tais como limites mecânicos
> (altura, largura, profundidade) e limites de dissipação térmica.

### Especificação de Algoritmos (:warning: ATUALIZAR :warning:)

> (Se preferir, adicione um link para o documento de especificação de algoritmos).
> 
> Deve ser elaborado para CADA evento o algoritmo de tratamento deste evento. Com base no
> tamanho de cada algoritmo, estima-se o tamanho de memória necessária para armazenar todos
> os programas e os dados associados. Isso permitirá especificar a memória a ser utilizada e o
> espaço onde serão armazenados os programas. O algoritmo de tratamento de evento pode
> ser representado graficamente por um fluxograma. Recomenda-se usar símbolos gráficos consistentes 
> com a norma internacional ISO 1028-1973 e IS0 2972-1979.

## Referências (:warning: ATUALIZAR :warning:)
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
