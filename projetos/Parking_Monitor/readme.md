# `Sistema de Monitoramento de Estacionamento`
# `Parking Monitor System`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

> |Nome  | RA | Curso|
> |--|--|--|
> | Felipe Benedet  | 234180  | Eng. Elétrica|
> | Nome2  | 123456  | Eng. Elétrica|


## Descrição do Projeto
Este projeto se trata de um sistema de monitoramento de estacionamento. O objetivo principal é verificar a disponibilidade de vagas em tempo real, sinalizando quais estão ocupadas ou livres. Além disso, o sistema exibirá uma lista das vagas disponíveis em um painel visível para os usuários e registrará dados sobre o fluxo de veículos. O sistema também será capaz de enviar os dados via internet para outro software especializado fazer o processamento dos dados e gerar reports detalhados sobre o fluxo de veículos.


## Descrição Funcional

### Funcionalidades
Para o monitoramento adequado de estacionamentos o sistema deve ter algumas funcionalidades básicas que envolvem ser capaz de:
- Para monitoramento das vagas:
    - Detectar a presença de qualquer veículo estacionado nas vagas;
    - Indicar se as vagas estão disponíveis/ocupadas;
        - A mudança de status da vaga só deve ser considerada após um certo período que a mudança for detectada;
- Para exibição do controle de vagas:
    - Contabilizar todas as vagas disponíveis;
    - Ter registro do total de vagas;
    - Mostrar em um painel a quantidade de vagas disponíveis;
        - É importante que essa informação seja atualizada em tempo real;
- Para coleta de dados para análise de fluxo:
    - Coletar a relação de vagas periodicamente;
    - Enviar os dados via internet para o software analisador.


### Configurabilidade
O sistema projetado deve apresentar um comportamento semelhante em cada contexto em que for aplicado e, para apresentar um bom funcionamento em todos eles, deve ser possível:
- Indicar a quantidade total de vagas que estarão disponíveis no estacionamento;
- Indicar o threshold de tempo para considerar a mudança de estado da vaga;
- Indicar o intervalo de tempo em que serão coletados os logs para análise de fluxo.


### Eventos



### Tratamento de Eventos

## Descrição Estrutural do Sistema
![parking-sys](https://github.com/felipe-benedet/ea075-2023.2/assets/144614560/08de9dc7-7366-438a-9cf2-0d44e0eeb147)

## Referências
