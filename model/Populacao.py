from model.log import *
from model.Individuo import Individuo
from model.RelatorioPopulacao import RelatorioPopulacao
from model.StatusRelacionamento import StatusRelacionamento as statusRel
from fractions import Fraction
import random
import math

class Populacao:
    def criaPopulacaoInicial(self, individuosIniciais):
        while self.relatorio.getTotalPopulacao() < individuosIniciais:
            individuo = Individuo(self, 1)
            if(isinstance(individuo, Individuo)):
                self.addIndividuo(individuo, )
        
    def __init__(self, individuosIniciais, totalGeracoes):
        self.MINIMO_POPULACAO = 1
        self.MINIMO_GERACOES = 1
        self.TAXA_FERTILIDADE = 50
        self.TEMPO_VIDA = 3
        
        if(isinstance(individuosIniciais, int) and individuosIniciais >= self.MINIMO_POPULACAO and
            isinstance(totalGeracoes, int) and totalGeracoes >= self.MINIMO_GERACOES):
            self.geracaoAtual = 1
            self.contIndividuosExistiram = 0
            self.relatorio = RelatorioPopulacao(self)
            self.individuos = []
            self.totalGeracoes = totalGeracoes
            self.casais = []
            self.solteiros = []

            self.criaPopulacaoInicial(individuosIniciais)
        else:
            Log.printLog('WARNING TESTE', ClasseLog.WARNING)

    
    def getIndividuos(self):
        return self.individuos

    #Insere o indivíduo tanto na População quanto no contador do Relatório.
    def addIndividuo(self, individuo, recemCriado = False):
        self.individuos.append(individuo)
        self.contIndividuosExistiram += 1
        self.relatorio.contabilizaIndividuo(individuo, recemCriado)

    def removeIndividuo(self, individuo):
        #Caso seja casado, destroi o casal e retorna o outro integrante aos solteiros
        eraCasado = False
        if(individuo.getStatusRel() == statusRel.CASADO):
            casal = [c for c in self.getCasais() if individuo in c['integrantes']][0]
            conjuge = [i for i in casal['integrantes'] if i != individuo][0]
            eraCasado = True
            conjuge.setStatusRel(statusRel.SOLTEIRO)
            self.solteiros.append(conjuge)
            self.separaCasal(casal)
        self.relatorio.removeIndividuo(individuo, eraCasado)
        self.individuos.remove(individuo)

    def getContIndividuos(self):
        return self.relatorio.getTotalPopulacao()

    def getContIndividuosExistiram(self):
        return self.contIndividuosExistiram

    def getGeracaoAtual(self):
        return self.geracaoAtual

    def getTotalGeracoes(self):
        return self.totalGeracoes

    def getCasais(self):
        return self.casais

    def separaCasal(self, casal):
        self.casais.remove(casal)

    #Passa uma geração
    def iteraGeracoes(self):
        while((self.getGeracaoAtual() <= self.getTotalGeracoes()) and len(self.individuos) > 0):
            self.formaCasais(self.filtraSolteiros(self.getIndividuos()))
            self.checaTempoVida()
            self.relatorio.fimCicloGeracao(self.getGeracaoAtual(), len(self.getSolteiros()))
            self.relatorio.printRelatorio()
            self.geracaoAtual += 1
            self.relatorio.resetaRecemCriados()
            self.iteraHerdeiros()
        if(len(self.individuos) == 0): Log.printLog('\n**********População Extinta**********', ClasseLog.FAIL)

    def iteraHerdeiros(self):
        ##Cálculo de número de casais que terão descendentes
        casais = self.getCasais()
        numeroCasais = math.floor((self.TAXA_FERTILIDADE/100)*len(casais))
        casais = random.sample(casais, numeroCasais)
        for casal in casais:
            #print('Casal ', (casal['integrantes'][0].getId(), casal['integrantes'][1].getId()), ' resolveu ter filho')
            individuo = Individuo(self, self.getGeracaoAtual(), casal['integrantes'])
            self.addIndividuo(individuo, True)
            casal['filhos'] += 1
            
    def getContHomens(self):
        return self.relatorio.getContHomens()

    def getContMulheres(self):
        return self.relatorio.getContMulheres()

    def filtraSolteiros(self, amostra):
        return [i for i in amostra if i.getStatusRel() == statusRel.SOLTEIRO]

    def getSolteiros(self):
        return self.solteiros

    def setSolteiros(self, solteiros):
        self.solteiros = solteiros
        
    def novoCasal(self, integrantes):
        self.casais.append({'integrantes': integrantes, 'filhos': 0})
        self.relatorio.novoCasal()
        for integrante in integrantes:
            integrante.setStatusRel(statusRel.CASADO)

    #Forma casais com a amostra do parâmetro
    def formaCasais(self, amostra):
        while True:
            fila = tuple()
            for i in amostra:
                if((len(fila) == 1 and i.getGenero() != fila[0].getGenero())
                       or len(fila) == 0):
                    fila += (i,)

                if(len(fila) == 2):
                    self.novoCasal(fila)
                    for i in fila: i.setStatusRel(statusRel.CASADO)
                    fila = tuple()
    
            solteiros = self.filtraSolteiros(amostra)
            #Checa se os solteiros contem generos diferentes. Se sim, os coloca
            #Como população temporária (amostra). Se não, finaliza a função
            h = [item for item in solteiros if item.getGenero() == 'M']
            m = [item for item in solteiros if item.getGenero() == 'H']
            
            if(len([item for item in solteiros if item.getGenero() == 'M']) > 0
               and len([item for item in solteiros if item.getGenero() == 'H']) > 0):
                amostra = solteiros
            else:
                self.setSolteiros(solteiros)
                self.relatorio.setSolteiros(len(solteiros))
                break
        
    def checaTempoVida(self):
        for individuo in [i for i in self.getIndividuos()
                          if(self.getGeracaoAtual() - i.getGeracao() >= self.TEMPO_VIDA)]:
            self.removeIndividuo(individuo)
