# `<Título em Português do Projeto>`
# `<Project Title in in English>`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> Incluir nome RA e foco de especialização de cada membro do grupo. Os projetos devem ser desenvolvidos em duplas.
> |Nome  | RA | Curso|
> |--|--|--|
>  | Bruno Moreira Pilarski | 195119  | Eng. Elétrica| Eng. de Computação |
>  | Felipe Martins Nogueira| 167263  | Eng. Elétrica| Eng. de Desenvolvimento de Produto|  


## Descrição do Projeto


O propósito deste projeto é empregar uma variedade de sensores capazes de diagnosticar as condições climáticas, tais como umidade, velocidade relativa do vento e temperatura, a fim de auxiliar no gerenciamento das condições internas de um espaço fechado. Esse conceito pode ser extrapolado para uma ampla gama de ambientes que buscam o controle da temperatura interna, fazendo uso das condições >externas favoráveis, como exemplificado pelo caso de um Contêiner Data Center.
Apesar de possuir a possibilidade de tais extrapolações, este projeto será conduzido tomando como base o controle interno de uma residência.

## Descrição Funcional
> A descrição funcional do projeto é a principal entrega do E1 e pode ser realizada neste próprio arquivo Markdown,
> com links para diagramas ou outros arquivos que estejam no próprio repositório.
>
> O sistema em questão deve ser capaz de diagnosticar, por meio de sensores, as mudanças de temperatura externa, a detecção de chuva, a temperatura relativa do vento. A partir desses dados, ou variáveis de controle, o dispositivo controlará o grau/nível de abertura das janelas e também a temperatura gerada pelo ar condicionado do local. Neste projeto, o dispositivo será utilizado para atender às demandas de uma residência. 


### Funcionalidades
Detecção de Chuva - O sistema é capaz de detectar a presença da chuva em diferentes intensidades, isto é, fraca, média e forte;
Determinação de velocidade relativa do vento;
Medição de temperatura;
Automação de janelas & Condicionadores de Ar - Fechamento e abertura das janelas e acionamento do ar condicionado a partir das variáveis de decisão mencionadas acima;


### Configurabilidade
A princípio, o sistema contará com três configurações possíveis: 
Modo manual | Modo automático | Híbrido ( habilitar função que permita ao usuário configurar as variáveis de decisão ).


### Eventos
> Quais eventos o sistema deve tratar?
> Se aplicável, classifique os eventos que são periódicos (procure especificar a periodicidade) e os que são não-periódicos
> (qual o tempo mínimo entre dois eventos sucessivos)?
>
> O dispositivo, a princípio, tem seu desenvolvimento orientado a climas tropicais. Em algumas regiões do Brasil, por exemplo, podemos identificar fenômenos climáticos endêmicos, próprio do local considerado. De forma geral, o sistema embarcado é capaz de lidar com os seguintes eventos:

Detecção de chuva: Nesta função, o sistema é capaz de detectar detectar a intensidade da chuva no momento e, partir desse input, definir o nível de abertura da janela, bem como a variação da temperatura interna da residência. 

Determinação da velocidade relativa do vento: o sensor afere o velocidade relativa do vento. A partir deste input, é possível identificar o grau de risco oferecido pela movimentação de ar, bem como alterar o nível de abertura da janela ( neste sentido, a função que detecta se um tornado,por exemplo, a partir das temperatura e intensidade do vento não entra no escopo deste projeto)

Medição de temperatura: aqui, o sistema é capaz de quantificar o nível de temperatura externa e, com isso, alterar a temperatura interna e modificar ao grau de abertura da janela. 

A partir dessas variáveis de entada, o sistema será capaz de gerenciar a temperatura interna de um local fechado. 

### Tratamento de Eventos
O tratamento de eventos pode ser descrito da seguinte maneira:

 |Evento  | Período de Avaliação |
 
 | Chuva  | Interrupção  | Fechar Janelas| 
 | Avaliar Temperatura Interna   | 5 minutos  | 
 | Avaliar Temperatura Externa  | 5 minutos  | 
 | Avaliar velocidade relativa do ar externo   | 5 minutos  | 
 | Avaliar Temperatura Interna   | 5 minutos  | 

## Descrição Estrutural do Sistema
> Junto com a descrição do comportamento do sistema, deve-se especificar, em nível de bloco ou sistema, a estrutura necessária 
> para captar os eventos do mundo externo, para alojar e processar o programa de tratamento de eventos, e para atuar sobre o mundo externo.
>
> Para essa descrição recomenda-se a criação de diagramas de blocos.
> Nesse diagrama, devem ser destacados os blocos funcionais que compõem o sistema, incluindo uma síntese das funcionalidades de cada bloco.
> Além disso, deve-se esclarecer também o relacionamento entre estes blocos, incluindo os principais sinais de comunicação entre
> os blocos de forma a assegurar a execução de todas as tarefas que o sistema deve realizar.
> 
> Você sabia? Ferramentas como o `draw.io` permitem integração com o Github.
> 

## Referências
Written with [StackEdit](https://stackedit.io/).
Fluxograma with [Lucid.App](https://lucid.app/)
http://www.catspowerdesign.fr/actualites/systeme-embarque

