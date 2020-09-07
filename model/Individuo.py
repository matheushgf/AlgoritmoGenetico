from model.log import *
import random

from model.StatusRelacionamento import StatusRelacionamento as statusRel

class Individuo:
    def __init__(self, populacao, geracao, pais = None):
        self.GENEROS = generos = ['M', 'H']
        
        self.id = hex(populacao.getContIndividuos()+1)
        self.pais = pais
        self.genero = random.choice(self.GENEROS)
        self.geracao = geracao
        self.setStatusRel(statusRel.SOLTEIRO)

    def getId(self):
        return self.id
    
    def setStatusRel(self, statusRelacionamento):
        if(statusRelacionamento in statusRel._value2member_map_.values()):
            self.statusRelacionamento = statusRelacionamento
        else:
            Log.printLog('WARNING TESTE', ClasseLog.WARNING)
            self.statusRelacionamento = None

    def getStatusRel(self):
        return self.statusRelacionamento
    
    def getPais(self):
        return self.pais

    def getGenero(self):
        return self.genero

    def getGeracao(self):
        return self.geracao
