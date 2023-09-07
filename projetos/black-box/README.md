# `Caixa Preta`
# `Black Box`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Curso|
|--|--|--|
| Caio Ruiz Coldebella  | 232621  | Eng. de Computação|
| Gustavo de Souza dos Reis  | 217425  | Eng. de Computação|

## Descrição do Projeto

> Descrição do objetivo principal do projeto, incluindo contexto gerador, motivação.
> Escreva essa seção imaginando que está tentando convencer alguém a investir financeiramente no seu projeto.
> Qual problema vocês pretendem solucionar?
> Quem são os potenciais usuários?
> É possível estabelecer um valor econômico associado?

O Black Box é um sistema de registro e transmissão de dados de vôo de um foguete, ele foi pensado para
atender uma demanda da equipe Antares Unicamp, aonde se viu a ncessidade de análise de informações do lançamento.

Dessa forma, mesmo que haja um acidente que comprometa o vôo, o sistema deve ser seguro e resistente o suficiente para
resistir ao impacto da queda e permitir a leitura de informações sobre o lançamento ao ser encontrado em terra, além disso
é necessário que seja de baixo custo.

## Descrição Funcional
> A descrição funcional do projeto é a principal entrega do E1 e pode ser realizada neste próprio arquivo Markdown,
> com links para diagramas ou outros arquivos que estejam no próprio repositório.

O sistema será projetado utilizando uma plataforma de prototipagem NodeMCU-32S baseada no microcontrolador SP-WROOM-32, juntamente com um sensor de altitude (altímetro),
que será responsável por fornecer com precisão os dados de altitude. 

A vantagem de utilizarmos o NodeMCU-32S é que este possui um módulo wi-fi para podermos
receber com praticidade os dados de log do vôo, além disso ele possui outros pontos positivos como bluetooth, um microprocessador de baixa potência,
memória flash de 32MB, antena embutida, conversor USB serial integrado e porta micro USB para alimentação e programação, além de diversas interfaces entre elas a I2C 

### Funcionalidades
> Detalhe todas as tarefas que o sistema será capaz de executar
As funcionalidades planejadas para o sistema serão:

- Apogeu (altitude máxima de vôo)
- Tempo de Apogeu
- Variação da altitude ao longo de itervalos de tempo (dado não essencial)

### Configurabilidade
> Detalhe, se houver, todas as possíveis configurações do circuito e todos os pontos de alteração da configuração.

### Eventos
> Quais eventos o sistema deve tratar?
> Se aplicável, classifique os eventos que são periódicos (procure especificar a periodicidade) e os que são não-periódicos
> (qual o tempo mínimo entre dois eventos sucessivos)?

- Registro de informação do altímetro (periódico)
- Comunicação via wi-fi (não periódico)

### Tratamento de Eventos
> Qual comportamento o sistema deve ter para tratar corretamente cada evento?

Os eventos são tratados a partir da leitura e escrita de dados na memória flash

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
![Diagrama Estrutural](./Diagrama_black_box.drawio.png)
## Referências
> Seção obrigatória. Inclua aqui referências utilizadas no projeto.

- [NodeMCU32S Blog MasterWalker Shop](https://blogmasterwalkershop.com.br/embarcados/esp32/conhecendo-o-nodemcu-32s-esp32)
