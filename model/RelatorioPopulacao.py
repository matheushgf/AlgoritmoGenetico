from model.log import *

class RelatorioPopulacao:
    def __init__(self, populacaoPai):
        self.populacaoPai = populacaoPai
        self.totalPopulacao = 0
        self.totalHomens = 0
        self.totalMulheres = 0
        self.casais = 0
        self.solteiros = 0
        self.historicoGeracoes = {}
        self.recemCriados = 0
        self.configuracaoPrintRelatorio = {
            'exibir': True,
            'mostraHeaders': True,
            'mostraTotal': True,
            'mostraTotalHomens': True,
            'mostraTotalMulheres': True,
            'mostraNumeroCasais': True,
            'mostraNumeroSolteiros': True
        }
        
    def incrementaTotalPopulacao(self):
        self.totalPopulacao += 1

    def getTotalPopulacao(self):
        return self.totalPopulacao

    def contabilizaIndividuo(self, individuo, recemCriado):
        #Analisa e incrementa
        self.totalPopulacao += 1
        genero = individuo.getGenero()
        if(genero == 'M'):
            self.totalMulheres += 1
        elif(genero == 'H'):
            self.totalHomens += 1
        if(recemCriado): self.incrementaRecemCriados()

    def removeIndividuo(self, individuo, eraCasado):
        self.totalPopulacao -= 1
        genero = individuo.getGenero()
        if(genero == 'M'):
            self.totalMulheres -= 1
        elif(genero == 'H'):
            self.totalHomens -= 1
        if(eraCasado):
            self.casais -= 1
            self.solteiros += 1
        else: self.solteiros -= 1
        
    def getContHomens(self):
        return self.totalHomens

    def getContMulheres(self):
        return self.totalMulheres

    def printRelatorio(self):
        config = self.configuracaoPrintRelatorio
        if(config['exibir']):
            if(config['mostraHeaders']):
                g = self.populacaoPai.getGeracaoAtual()
                Log.printLog(f'==========GERAÇÃO {g}==========', ClasseLog.WARNING)
            Log.printLog(f'Descententes novos: {self.getRecemCriados()}', ClasseLog.DEFAULT)
            if(config['mostraTotal']):
                Log.printLog(f'População Total: {self.totalPopulacao}', ClasseLog.DEFAULT)
            if(config['mostraTotalHomens']):
                Log.printLog(f'População Homens: {self.totalHomens}', ClasseLog.DEFAULT)
            if(config['mostraTotalMulheres']):
                Log.printLog(f'População Mulheres: {self.totalMulheres}', ClasseLog.DEFAULT)
            if(config['mostraNumeroCasais']):
                Log.printLog(f'Casais: {self.casais}', ClasseLog.DEFAULT)
            if(config['mostraNumeroSolteiros']):
                Log.printLog(f'Solteiros: {self.solteiros}', ClasseLog.DEFAULT)

    def novoCasal(self):
        self.casais += 1
        
    def setSolteiros(self, solteiros):
        self.solteiros = solteiros

    def fimCicloGeracao(self, geracao, criados):
        self.historicoGeracoes[str(geracao)] = criados
    
    def getHistoricoGeracao(self, geracao):
        return self.historicoGeracoes[str(geracao)]

    def getPopulacaoPai(self):
        return self.populacaoPai

    def incrementaRecemCriados(self):
        self.recemCriados += 1

    def resetaRecemCriados(self):
        self.recemCriados = 0

    def getRecemCriados(self):
        return self.recemCriados
