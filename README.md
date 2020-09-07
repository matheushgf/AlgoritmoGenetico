# **Algoritmo Genético**
Este repositório contém testes de códigos em ***Python 3.8*** contendo simulação simples de Algoritmos Genéticos, a fim de simular a Evolução de forma algorítmica.

### **Atual funcionamento do código**
O código atualmente simula inicialmente uma criação de uma população de X indivíduos (sem contar sua origem) com interação automática entre os mesmos durante Y gerações ou até que todos os indivíduos se acabem. A cada geração, os indivíduos SOLTEIROS se juntam a outros do sexo oposto e mudam seu status para CASADO. Ao mesmo tempo, a cada geração, os casais tem filhos, que se juntam à população, podendo apenas procriar a partir da geração seguinte à que foi criado, e os indivíduos com o tempo de vida maior do permitido são removidos. A População tem uma taxa fertilidade, que aqui apenas simula um controle populacional para melhor controle dos processos.
A casa geração, é gerado um pequeno relatório para visualização de alguns dados, como número de indivíduos gerados, número de casais e média de filhos por casal, mas para rodar de forma mais leve sem o print, basta setar 'exibir' na classe RelatorioPopulacao para False.

### **Estrutura do repositório**
O repositório contem arquivos com a extensão **_.py_**:
* **main**: Este é o código a ser rodado para iniciar a simulação;
* **models/**: É a pasta de Classes do sistema;

### **Como executar e testar**
Os arquivo __main__ contidos no projeto são executáveis apenas possuindo o Python 3.8. Para exibição com cores (utilizado da biblioteca __colorama__), basta rodar __main__ através do terminal, da seguinte forma:
```
    cd <caminho_da_pasta>
    python main.py
```
Caso deseje testar e modificar, basta abrir o código com uma IDE e sair usando. Até o momento, nenhuma biblioteca externa foi usada para desenvolvimento do código.

### **Futuras alterações**
* Variáveis genéticas simples para visualizar hereditariedade;
* Cromossomos e aleatoriedade de mutação;
* Competição por recursos;
* Adição de competição para simular a _Seleção Natural_ de forma reduzida a poucas variáveis;
* Utilização de plataforma de _I.A._ para permitir maior complexidade; 
* Arquivo de configuração de variáveis dinâmicas;
* Diferenciação de espécies de acordo com o grau de diferença com sua população;
* Variáveis de simulação de situações, como falta de comida;
* Teste múltiplo de Populações usando variáveis diferentes;