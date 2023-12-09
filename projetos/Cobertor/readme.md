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

Com o objetivo de promover uma significativa melhoria na qualidade de vida e na humanização do tratamento oferecido aos pacientes em ambientes hospitalares, desenvolvemos uma inovadora manta aquecedora para o controle preciso da temperatura.

Dentre os diversos procedimentos nos quais a manutenção contínua da temperatura se revela crucial, destacam-se: a necessidade de aquecimento prévio durante a transfusão de concentrado de hemácias, a fim de evitar coagulação; o suporte à analgesia da pele suprapúbica durante a inserção de um DIU; o aquecimento direto para recém-nascidos nos primeiros minutos de vida; e o condicionamento térmico de uma bolsa de ocitocina antes de sua infusão no pós-parto (período de grenberg). Adicionalmente, a consideração do conforto térmico do paciente é fundamental, uma vez que o frio presente em clínicas e hospitais, embora necessário, pode ser desagradável para muitos.

O produto em questão é composto por dois elementos essenciais: um controlador de aquecimento e uma malha resistiva, disponível em diferentes tamanhos. Destaca-se a versatilidade do controlador, que pode ser utilizado em malhas variando desde 20x20 cm até 2x1 m, proporcionando uma distribuição constante e eficaz do calor. O dispositivo opera com uma configuração pré-definida de 37,5 °C, mantendo o equilíbrio térmico, e está equipado com um termômetro que monitora a temperatura do paciente, quantificando a quantidade necessária de calor a ser transmitida.

Ademais, o produto oferece modos rápido e lento de aquecimento, proporcionando flexibilidade no tratamento. Além disso, apresenta a opção de alimentação por tomada elétrica ou bateria, garantindo praticidade e mobilidade em diferentes contextos hospitalares. Essas características tornam nossa manta aquecedora não apenas uma solução eficaz para os desafios térmicos em procedimentos médicos, mas também um instrumento versátil e adaptável às diversas necessidades clínicas.

## Descrição Funcional

O controle de temperatura é realizado por meio de um microcontrolador, permitindo ao operador configurar e monitorar a temperatura por meio de sensores especializados. Este inovador dispositivo apresenta uma série de características essenciais para garantir um tratamento térmico eficaz e seguro:

1. **Configuração Flexível de Temperatura:**
   - O equipamento oferece a conveniência de um pré-set inicial de temperatura em 37,5°C, facilitando a operação, mas permitindo ajustes conforme necessário.

2. **Modos de Aquecimento Rápido e Lento:**
   - Conta com dois modos de aquecimento distintos, um rápido e outro lento, proporcionando flexibilidade e adaptabilidade aos diferentes requisitos clínicos.

3. **Operação Silenciosa:**
   - Garante um ambiente tranquilo no ambiente hospitalar, evitando qualquer interferência sonora, assegurando conforto tanto para pacientes quanto para profissionais de saúde.

4. **Indicador de Temperatura do Paciente:**
   - Apresenta um indicador claro da temperatura do paciente, permitindo uma monitorização constante e eficaz do estado térmico.

5. **Sinalizador de Alerta:**
   - Incorpora um sinalizador que alerta a equipe no caso de o paciente não conseguir manter a temperatura adequada sem o dispositivo, garantindo intervenção rápida.

6. **Monitoramento Inteligente pós-Homeostase:**
   - Após atingir a homeostase, o dispositivo continua monitorando o paciente. Em caso de uma queda de temperatura fora da faixa adequada, reinicia automaticamente o aquecimento e notifica a equipe.

7. **Segurança contra Queimaduras:**
   - Trabalha na região de homeostase, mantendo uma temperatura uniforme que evita riscos de queimaduras aos pacientes.

8. **Mínimo Risco de Contaminação:**
   - No caso de contato direto com a pele, o dispositivo é projetado para oferecer o menor risco possível de contaminação, cumprindo rigorosos padrões de segurança.

9. **Autodesligamento e Sinalização de Problemas:**
   - Em situações adversas, o equipamento é capaz de se autodesligar e sinalizar o problema por meio de uma Interface Homem-Máquina (IHM), proporcionando segurança adicional.

10. **Métodos Não Invasivos e Toque Confortável:**
    - O dispositivo utiliza métodos não invasivos, garantindo conforto ao paciente, inclusive ao toque, sem comprometer a segurança ou eficácia do tratamento térmico.


### Funcionalidades

- O sistema apresenta capacidade para monitorar três diferentes temperaturas: a corporal do usuário, a ambiente e a interna do cobertor;

- Os usuários podem facilmente selecionar a temperatura desejada por meio de uma intuitiva interface com o operador;

- Monitoramento completo de todas as temperaturas é possível através da interface com o operador;

- O sistema oferece tanto opções de aquecimento lento quanto rápido;

- Inclusão de um timer para ajustar períodos específicos de aquecimento;

- Proteção contra superaquecimento integrada;

- Sinalizadores para situações de emergência, assegurando rápida intervenção;

- Indicador de nível de bateria para acompanhamento do status energético.


### Configurabilidade

O sistema permite a configuração da temperatura desejada entre o cobertor e o usuário, sendo adaptável a diferentes malhas de tamanhos distintos;

Compatibilidade com a rede elétrica convencional (AC) e a opção de operação por baterias.

### Eventos

O sistema é projetado para ler as temperaturas do ambiente e ajustar a corrente fornecida às resistências, manipulando assim a temperatura gerada pela malha térmica. O ciclo de operação do sistema segue a seguinte lógica:

1. O operador deve verificar qual forma de alimentação será utilizada, AC ou bateria.

2. Ligar a chave geral de operação do equipamento para ativá-lo.

3. Após a ativação, o microcontrolador detectará se a manta térmica está conectada a ele.

         - 3-A. Se a condição anterior for atendida, o sistema avançará para a próxima etapa; caso contrário, seguirá para o item 3-B.
        
         - 3-B. O controlador indicará a existência de um problema com a malha, permanecendo travado nessa condição até ser liberado pelo reset (liga e desliga geral do equipamento).

4. O controlador verificará se os sensores de temperatura estão conectados e prontos para operar; em caso contrário, ocorrerá a mesma situação descrita no item 3-B, indicando qual sensor apresenta problemas.

5. Com todas as condições atendidas, a Interface Homem-Máquina (IHM) é liberada para configuração.
    
       - 5-A. O controlador permite o ajuste da temperatura de aquecimento, iniciando por padrão em 37,5°C.
      
       - 5-B. Após o ajuste da temperatura, o operador pode escolher entre os modos de aquecimento rápido e lento.
      
       - 5-C. Por fim, o operador ajusta o tempo de operação.

6. Após a configuração, o operador inicia o ciclo de aquecimento pressionando o botão correspondente.

7. Durante o ciclo de aquecimento, o sistema atua com uma rotina inteligente de monitoramento do paciente e da temperatura. No entanto, algumas condições podem interromper o ciclo:

       - 7-A. Superaquecimento do paciente;
       
       - 7-B. Sobrecorrente no sistema;
       
       - 7-C. Detecção de fuga de corrente;
       
       - 7-D. Baixo ganho de temperatura.

8. Após a conclusão do ciclo de aquecimento, o controlador sinaliza que o processo foi finalizado, exibindo parâmetros como tempo médio de aquecimento.

9. O sistema permite a realização de um novo ciclo.


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

### Especificação de Algoritmos 

Estão presentes no processo descritos no  [Sheet](https://docs.google.com/spreadsheets/d/1-1rj091qlxhiRs93vTr5_trmvLaekvoHrqH35_JUYkg/edit?usp=sharing), contudo serão passados algoritimos.

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


