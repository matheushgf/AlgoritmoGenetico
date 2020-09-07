import random
from fractions import Fraction
import os
from colorama import init
init(True)
from model.Populacao import Populacao

populacao = None
        
while not isinstance(populacao, Populacao):
    individuosIniciais = int(input('Insira o n de individuos iniciais aleatórios (MAIOR QUE ZERO): '))
    totalGeracoes = int(input('Insira o n de gerações (MAIOR QUE ZERO): '))
    populacao = Populacao(individuosIniciais, totalGeracoes)

populacao.iteraGeracoes()    
##seq = [casal['filhos'] for casal in casais]
##maior = max(seq)
##menor = min(seq)
##media = sum(seq)/len(seq) 
##print('==========ANÁLISE FINAL==========')
##print('Menor incidência de filhos: ', menor)
##print('Maior incidência de filhos: ', maior)
##print('Média de filhos de todos os casais: ', media)
