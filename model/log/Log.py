from model.log.ClasseLog import ClasseLog
from colorama import Fore, Back, Style

class Log:
    def printLog(texto, classe = ClasseLog.DEFAULT):
        if(classe in ClasseLog._value2member_map_.values()):
            print(classe.value + texto)
        else:
            print(texto)
