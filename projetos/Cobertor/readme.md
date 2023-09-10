# `Cobertor de Hospital`
# `Hospital Blanket`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 |Guilherme Lehmann Concentino  | 173805  | Eng. Elétrica |
 |Pedro Henrique Moraes Dos Santos  | 243528 | Eng. Elétrica |

## Descrição do Projeto

Visando uma melhor qualidade de vida e humanização no tratamento dos pacientes de ambientes hospitalares, desenvolvemos uma manta aquecedora para controle de temperatura.
O ambiente frio de clínicas e hospitais é necessário, porém desagradável para muitos.

> Escreva essa seção imaginando que está tentando convencer alguém a investir financeiramente no seu projeto.
> Qual problema vocês pretendem solucionar?
> Quem são os potenciais usuários?
> É possível estabelecer um valor econômico associado?


## Descrição Funcional

A manta térmica é uma malha de resistências ligadas diretamente na tomada. O controle de temperatura é feito a partir de um microcontrolador, e a temperatura será configurada pelo operador e controlada por sensores de temperatura.

> A descrição funcional do projeto é a principal entrega do E1 e pode ser realizada neste próprio arquivo Markdown,
> com links para diagramas ou outros arquivos que estejam no próprio repositório.

### Funcionalidades

* O sistema será capaz de identificar a temperatura corporal do usuário, a temperatura ambiente e a temperatura interna do cobertor.
* Será possível selecionar a temperatura desejada atarvés de uma interface com o operador.
* Será possível monitorar todas as temperaturas pela interface com o operador.


> Detalhe todas as tarefas que o sistema será capaz de executar

### Configurabilidade

Será configurada a temperatura que é desejada entre cobertor e usuário.

> Detalhe, se houver, todas as possíveis configurações do circuito e todos os pontos de alteração da configuração.

### Eventos

O sistema deve ler as temperaturas do sistema e ajustar a corrente fornecida às resistências para manipular a temperatura gerada pela malha térmica.

> Quais eventos o sistema deve tratar?
> Se aplicável, classifique os eventos que são periódicos (procure especificar a periodicidade) e os que são não-periódicos
> (qual o tempo mínimo entre dois eventos sucessivos)?

### Tratamento de Eventos
> Qual comportamento o sistema deve ter para tratar corretamente cada evento?

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
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.
