# **Algoritmo Genético**
Este repositório contém testes de códigos em ***Python 3.8*** contendo simulação simples de Algoritmos Genéticos, a fim de simular a Evolução de forma algorítmica.

### **Atual funcionamento do código**
O código atualmente simula inicialmente uma criação de uma população de X indivíduos (sem contar sua origem) com interação automática entre os mesmos durante Y gerações, ambos parâmetros obrigatoriamente maiores que 0. A cada geração, os indivíduos SOLTEIROS se juntam a outros do sexo oposto e mudam seu status para CASADO. Ao mesmo tempo, a cada geração, os casais tem filhos, que se juntam à população, podendo apenas procriar a partir da geração seguinte à que foi criado. Ao gerar um filho, o casal diminui em 50% sua fertilidade, que aqui apenas simula um controle populacional para melhor controle dos processos.
Não foi levado em conta, até o momento, o tempo de maturação dos indivíduos, e nem outros fatores externos.
Ao final da execução dos arquivos, é gerado um pequeno relatório para visualização de alguns dados, como número de indivíduos gerados, número de casais e média de filhos por casal.

### **Estrutura do repositório**
O repositório contem três arquivos com a extensão **_.py_**:
* **main_atualizado.py**: Este é o mais recente e com a versão mais recente;
* **main_antigo.py**: É a versão anterior à atualizada, mantida para testes de velocidade e precisão da evolução do código;
* **relatorio**: Utilização do módulo _timeit_ do Python 3 para teste de performance das duas últimas versões do código, para comparação e visualização da melhoria de velocidade.

### **Como executar e testar**
Os três arquivos contidos no projeto são executáveis apenas possuindo o Python 3.8. Nas versões __main__, o programa pede as variáveis no início, enquanto no relatório apenas a execução é contada, utilizando os mesmos parâmetros nas duas funções.
Caso deseje testar e modificar, basta abrir o código com uma IDE e sair usando. Até o momento, nenhuma biblioteca externa foi usada para desenvolvimento do código.

### **Futuras alterações**
* Melhoria da probabilidade de gênero ao nascer, que atualmente é aleatória;
* Aumento de variáveis nas interações entre indivíduos, como idade e morte;
* Variáveis genéticas simples para visualizar hereditariedade e suportar competição por recursos;
* Adição de competição para simular a _Seleção Natural_ de forma reduzida a poucas variáveis;
* Utilização de plataforma de _I.A._ para permitir maior complexidade. 