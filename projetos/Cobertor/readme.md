# `Manta e sistema de controle de aquecimento para procedimentos hospitalares.`
# `Heating system for hospital procedures`

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA075 - Introdução ao Projeto de Sistemas Embarcados*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

 |Nome  | RA | Curso|
 |--|--|--|
 |Guilherme Lehmann Concentino  | 173805  | Eng. Elétrica |
 |Pedro Henrique Moraes Dos Santos  | 243528 | Eng. Elétrica |

## Descrição do Projeto

Visando uma melhor qualidade de vida e humanização no tratamento dos pacientes de ambientes hospitalares, desenvolvemos uma manta aquecedora para controle de temperatura.

Entre alguns procedimentos onde controle de temperatura continuo é importante, temos: procedimentos como transfusão de concentrado de hemácias requerem o aquecimento antes de serem aplicadas nos pacientes para evitar a coagulação; para apoio na analgesia da pele suprapúbica quando de insere um DIU; aquecimento por contado para recém-nascidos nos primeiros minutos de vida, além do condicionamento térmico de uma bolsa de ocitocina antes de infundi-la no pôs parto (período de grenberg), mas também visando o conforto térmico do paciente dado que frio de clínicas e hospitais é necessário, porém desagradável para muitos.

O produto possui dois componentes: um controlar para aquecimento e a malha resistiva que pode ter diferentes tamanhos, sendo que um controlado pode ser usado para malhas de diferentes medidas desde peça de 20x20 cm até peças de 2x1 m transmitindo o calor de forma constante. Ele trabalha com pré-set de 37,5 °C no equilíbrio, além de contar com termômetro que acompanhar a temperatura do paciente e quantifica o quanto de calor deverá ser transmitido. Além disso, ele conta com modos rápido e lente de aquecimento. E também, conta com alimentação por tomada e baterias.

## Descrição Funcional

 O controle de temperatura é feito a partir de um microcontrolador, e a temperatura será configurada pelo operador e controlada por sensores de temperatura. Também deverá:

*É interessante conter um pré-set de temperatura em 37,5°C, mas que seja possível alterar;
*É importante que tenha dois modos de aquecimento, um rápido e outro lento;
*Que não faça barulho;
*Que tenha um indicador de temperatura do paciente, além de ter um sinalizador onde demonstre se paciente não está conseguindo manter o calor sem o equipamento;
*Que seja inteligente e monitore o paciente após ter atingido a homeostase, mas também que em caso de queda de temperatura fora da faixa adequada, volte a aquecer e avise a equipe;
*O dispositivo não deve oferecer risco de queimaduras aos pacientes, devendo trabalhar na região de homeostase, com temperatura uniforme;
*Caso dispositivo tenha contato direto com a pele, deverá oferecer o menor risco de contaminação;
*Em caso de problema a equipamento precisa se autodesligar e sinalizar o problema por uma IHM;
*Não usar métodos invasivos;
*Confortável ao toque. em caso de contato.

### Funcionalidades

* O sistema será capaz de identificar a temperatura corporal do usuário, a temperatura ambiente e a temperatura interna do cobertor;
* Será possível selecionar a temperatura desejada atarvés de uma interface com o operador;
* Será possível monitorar todas as temperaturas pela interface com o operador;
* Deve contar com sistema de aquecimento lento e rápido;
* Um timer para ajuste de períodos de aquecimento;
* Proteção sobre aquecimento;
* Sinalizadores para situações emergências;
* Deverá ter um indicador de nível de bateria.

### Configurabilidade

Será configurada a temperatura que é desejada entre cobertor e usuário. Pode se adaptar a diferentes malhas de tamanhos distuntos; pode trabalhar com a  rede AC convencional  e com baterias.

### Eventos

O sistema deve ler as temperaturas do sistema e ajustar a corrente fornecida às resistências para manipular a temperatura gerada pela malha térmica.O ciclo de operação do sistema seguirá a seguinte lógica:

1. Operador deverá verificar qual a forma de alimentação será usada, AC ou bateria.
2. Ligar a chave geral de operação do equipamento para ligá-lo.
3. Após isso, o microcontrolador deverá detectar se a manta térmica está conectada a ele.
   
       3-A. Caso a condição anterior seja cumprida, a próxima etapa, caso não seguirá o item 3-B.
  
       3-B. O controlador deverá indicar que existe um problema com a malha, ficando travado nesta condição, sendo liberado com o reset (liga e desliga geral do equipamento).
  
4. O controlador verificará se os sensores de temperatura estão conectavados e prontos para operar, caso contrário ocorrerá a mesma situação do item 3-B indicando qual sensor apresenta problemas.
5. Dado que todas as condições foram atendidas a IHM liberada para configuração.
       5-A. O controlador deverá permitir o ajuste de temperatura de aquecimento, sendo que por padrão ele deve iniciar com a temperatura de 37,5 C.
       5-B. Após realizar o ajuste de temperatura, deverá ser escolher o modo de aquecimento rápido e lento.
       5-C Por fim, ajustar o tempo de operação.

6. Feito isso, o operador deve apertar o botão para iniciar o ciclo de aquecimento.

7. Durante o ciclo de aquecimento o sistema atuará com uma rotina de inteligente de monitoramento do paciente e temperatura. Contudo, a algumas condições poderão gera a interrupção do ciclo, entre elas:

       7-A.Sobre aquecimento do paciente;
   
       7-B. Sobre corrente no sistema;
   
       7-C. Dectação de fuga de corrente;
   
       7-D. Baixo ganho de temperatura;

8. Após o ciclo de aquecimento, o controlador deverá sinalizar que o ciclo foi finalizado, mostrando parâmetros de tempo médio de aquecimento.
9.  Permitirá que seja feito um novo ciclo.


## Descrição Estrutural do Sistema

A partir da descrição funcional foi montado a primeira versão do fluxo de processo dos projetos indicando correlação e passagem de informações, além de mapear os processos.

![Projeto manta drawio](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/65ec84dc-b258-4028-aa54-cd52aa2d2bd3)

## Especificações

### Especificação Estrutural

 A elicitação dos requistos está sendo feito [via Sheet](https://docs.google.com/spreadsheets/d/1-1rj091qlxhiRs93vTr5_trmvLaekvoHrqH35_JUYkg/edit?usp=sharing). A primeira aba do documento  "Requisito Sistêmico" contém uma lista de processos sistêmicos (hardware e software) que foram extraído a partir da descrição do projeto e que compõem o fluxo gerado na Descrição Estrutural do Sistema, cada item da lista é referente a um processo mapeado e suas ramificações recebeu um *RS-SAXX* para ser identificado. Segue a imagem.
 
  ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/b796bf82-d057-45c4-8fe2-b529ad15c862)

Na segunda aba do arquivo “Requisito Funcional”, cada processo gerou um conjunto de requisitos funcionais, RF-SAXX, para esclarecer e identificar o que cada função e componente do processo deve fazer. Além de já conter a indicação de componente de possam atender a demanda. Conforme a imagem abaixo.
<div align="center">
 
  ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/cc66dbc1-754a-4a36-815e-c2141c1f1384)

  ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/ced7a3a6-e7b0-4d8c-9839-f94df5a13b11)

  ![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/a79f914c-16ad-42eb-bcfd-2c5da8404e1b)

</div>

**Processo M1**

     **Título:** Detecção de alta impedância
     
     **Parâmetros de entrada:** Sinal digital convertido pelo MCP3301, conectado ao pino B0 do PIC.
     
     **Parâmetros de saída:** Sinalização intermitente no LED, conectado ao pino A1 do PIC.
     
     **Função:** Indicar se a malha resistiva está conectada corretamente ou com problemas.
     
     **Processo dependente direto:** Processo S1 e S2.


**Processo M2 e M3**

    **Título:** Interrompe o funcionamento do circuito em caso de fuga de corrente maior que 0.1 mA
    
    **Entrada:** Sinal digital convertido pelo MCP3301, pino B0
    
    **Saída:** Conectado ao pino A0 do PIC;
    
    **Função:** Realiza a função diferencial residual nas entradas da malha.
    
    **Processo dependente direto:** Processo S1
    

**Processo M4 e P1:**

    **Título:** Leitura da temperatura da malha
    
    **Entrada:** Parâmetros obtidos a partir da interface serial com o sensor MLX90614, conectado aos pinos A2 e A3 do PIC, respectivamente.
    
    **Saída:** Os parâmetros são usados no processo S4.
    
    **Função:** Faz a leitura do parâmetro para temperatura.
    
    **Processo dependente direto:** Processo S3


**Processo M5**

    **Título:** Condicionamentos do sinal de acionamento.
    
    **Entrada:** Conectado ao pino A0 do PIC.
    
    **Saída:** Conectado à malha.
    
    **Função:** Amplifica o sinal PWM para a malha.
    
    **Processo dependente direto:** Não há

 
**Processo F2**

    **Título:** Seletor de alimentação.
    
    **Entrada:** Bateria e tomada
    
    **Saída:** F2 e F1
    
    **Função:** Seleciona se será usada bateria ou rede elétrica.


**Processo F1**

    **Título:** Carregador de bateria
    
    **Entrada:** Tensão da rede.
    
    **Saída:**
    
    **Função:** Garantir que a bateria esteja carregada.
    

**Processo F3**

    **Título:** Reguladores de tensão
    
    **Entrada:** Tensão da rede
    
    **Saída:** Tensão de 12V e 5V,
    
    **Função:** Alimentação dos componentes.

### Especificação de Algoritmos 



Estão presentes no processo descritos no  [Sheet](https://docs.google.com/spreadsheets/d/1-1rj091qlxhiRs93vTr5_trmvLaekvoHrqH35_JUYkg/edit?usp=sharing), contudo serão passados algoritimos.

**Processo S1**

    **Título:** Problemas na malha
    
    **Entrada:** Processo M1, M2 e M3, usando conectado ao pino B0 do PIC
    
    **Saída:** Interrupção do microcontrolador, via software; interrupção do sinal PWM; e sinalização intermitente no LED, conectado ao pino A1 do PIC.
    
    **Função:** Interrompe o funcionamento do circuito em caso de fuga de corrente maior que 0.1 mA.
    
    **Processo dependente direto:** Processo S2 e S3.


**Processo S2**

    **Título:** Preset equipamento - IHM
    
    **Entrada:** Potenciômetro, conectado ao pino A5 do PIC, com a função de alterar a escala de temperatura. Chave tátil, conectada ao pino A4 do PIC, usada para mudar as opções no menu de configuração (descrito no menu no MANUAL DE OPERAÇÃO).
    
    **Saída:** Parâmetro de temperatura desejada para o S3 e tempo.
    
    **Função:** Descrito no MANUAL DE OPERAÇÃO.
    
    **Processo dependente direto:** Processo S3.

**Processo S3**

    **Título:** Controle de temperatura
    
    **Entrada:** Os parâmetros de temperatura desejada e tempo são  passados pelo processo S2.
    
    **Saída:** Sinal PWM, pino A0.
    
    **Função:** Gerar um sinal PWM de acordo com a necessidade de aquecimento.
    
    **Processo dependente direto:** Processo M5.



<div align="center">

![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/fbd69272-6719-4824-96ff-1ff71acf5b40)

![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/c7a46948-c610-4094-b46b-66e94ce35ac2)

![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/339a0c3a-a23a-4dd8-afaf-5f7a55926f50)

![image](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/62679350/ba0bc06a-104e-49ae-9031-2db9f3f6f0e8)

</div>

## Projeto

### Esquemático do sistema

![Schematic_Manta_2023-12-03](https://github.com/piaiman/phms.2023.s2-feec-ea075/assets/144074445/eaad8ceb-9140-46fb-bbba-3637c0e00c55)

### Descrição

* Alimentação é de entrada de tensão AC com retificador e abaixador de tensão. A bateria é para suprir possíveis faltas de energia.
* O controle do sistema é feito por sensores de temperatura e podem ser monitorados por indicadores visuais, LEDs e Display.
* Há o sistema de segurança que atua em casos de sobre corrente.

## Referências

[ABNT NBR IEC 60601-1-2010: Equipamento eletromédico Parte 1: Requisitos gerais para segurança básica e desempenho essencial](https://www.zambini.org.br/pdfs/ABNT%20NBR%20IEC%2060601-1-2010%20Emenda%201-2016%20-%20Equipamento%20eletrom%C3%A9dico%20-%20Parte%201-%20Requisitos%20gerais%20para%20seguran%C3%A7a%20b%C3%A1sica%20e%20desempenho%20essencial.pdf)


