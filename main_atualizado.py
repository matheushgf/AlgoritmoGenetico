import random
from enum import Enum
from fractions import Fraction
import os

generos = ['M', 'F']
populacao = {}
analise = {'total': 0, 'Masc': 0, 'Fem': 0}
casais = []
ter_filhos = ['S', 'N'] #Usada pra cálculo de fertilidade

class Status(Enum):
    SOLTEIRO = 1
    CASADO = 2

def get_individuo(id):
    if(id in populacao.keys()):
        return populacao[id]
    else:
        return None
    
def cria_individuo(pais = None):
    novo_individuo = {}
    novo_individuo_id = hex(analise['total']+1)
    novo_individuo['genero'] = random.choice(generos)
    novo_individuo['status'] = Status.SOLTEIRO
    if(pais is not None):
        novo_individuo['pais'] = pais
        
    populacao[novo_individuo_id] = novo_individuo
    return (novo_individuo_id, novo_individuo)

def forma_casais(pop):
    while True:
        standby = tuple()
        for i in pop.items():
            if i[1]['status'] == Status.SOLTEIRO:
                if((
                        len(standby) == 1
                        and i[1]['genero'] != pop[standby[0]]['genero']
                    ) or len(standby) == 0):
                    standby += (i[0],)

            if(len(standby) == 2): 
                casais.append({'integrantes': standby, 'filhos': 0, 'fertilidade': 100})
                for integrante in standby:
                    individuo = get_individuo(integrante)
                    if(individuo is not None):
                        individuo['status'] = Status.CASADO
                standby = tuple()
        sobras = {j:v for j,v in pop.items() if v['status']==Status.SOLTEIRO}
        #Checa se as sobras contem generos diferentes. Se sim, coloca as sobras
        #Como população temporária (pop). Se não, finaliza a função
        if(len([item[0] for item in sobras.items() if item[1]['genero'] == 'M']) > 0
           and len([item[0] for item in sobras.items() if item[1]['genero'] == 'F']) > 0):
            pop = sobras
        else:
            return {'casais': casais, 'sobras': sobras}

criados_geracao = 0
filhos_criados = 0

individuos = 0
while individuos <= 0:
    individuos = int(input('Insira o n de individuos iniciais aleatórios (MAIOR QUE ZERO): '))
    if(individuos >= 0):
        for i in range(0, individuos):
            individuo = cria_individuo()
            analise['total']+=1
            criados_geracao+=1
            if(individuo[1]['genero'] == 'M'):
                analise['Masc']+=1
            elif(individuo[1]['genero'] == 'F'):
                analise['Fem']+=1

geracoes_total = 0
while geracoes_total <= 0:
        geracoes_total = int(input('Insira o n de gerações (MAIOR QUE ZERO): '))

for geracoes in range(0, geracoes_total):       
        print('==========Geração nº ', geracoes+1, '==========')
        casais_geracao = forma_casais(populacao)
        print('População desta geração: ', criados_geracao)
        print('Filhos nascidos nesta geração: ', filhos_criados)
        print('População total: ', analise['total'])
        print('Total Masc: ', analise['Masc'])
        print('Total Fem: ', analise['Fem'])
        #print('População: ', str(populacao))
        #print('Casais: ', casais_geracao['casais'])
        print('**Nº de casais: ', len(casais_geracao['casais']))
        #print('Sobras: ', casais_geracao['sobras'])
        print('**Nº de sobras: ', len(casais_geracao['sobras']))
        print('========================================')

        #Para cada casal, criar seu filho. Perceba que os casais são formados antes dos filhos,
        #para que os filhos criados não criem filhos imediatamente, o que causaria um loop
        #infinito.
        #Caso o casal tenha mais que dois filhos, reduz a chance de ter mais um em 50% da chance
        criados_geracao = 0
        filhos_criados = 0
        for casal in casais:
            rat = casal['fertilidade']/100
            prob = Fraction(rat).limit_denominator()
            escolha_filhos = random.choices(ter_filhos, weights=[prob.numerator, prob.denominator-prob.numerator], k=1)
            if escolha_filhos[0] == 'S':
                individuo = cria_individuo(casal['integrantes'])
                analise['total']+=1
                criados_geracao+=1
                filhos_criados+=1
                casal['filhos']+=1
                casal['fertilidade'] = casal['fertilidade']/2
                if(individuo[1]['genero'] == 'M'):
                    analise['Masc']+=1
                elif(individuo[1]['genero'] == 'F'):
                    analise['Fem']+=1

seq = [casal['filhos'] for casal in casais]
maior = max(seq)
menor = min(seq)
media = sum(seq)/len(seq) 
print('==========ANÁLISE FINAL==========')
print('Menor incidência de filhos: ', menor)
print('Maior incidência de filhos: ', maior)
print('Média de filhos de todos os casais: ', media)

os.system('PAUSE')
