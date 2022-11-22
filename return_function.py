numeros = [1,2,3]

numeros.pop()

#exemplo função

def quadrado_de_7():
    print(7*7)
    
ret = quadrado_de_7()

print(ret) #não vai retornar nada...

#com return
def quadrado_de_7():
    return 7*7 
    
ret = quadrado_de_7()

print(ret) #vai retornar 49.

def diz_oi():
    return "oi"

print(diz_oi()) # 'oi'


#vantagem e desvatagem do return...
#o return ta da mais flexibilidade de usar o dado...

#observações sobre o return
#finaliza a função...
#pode ter em uma função diferentes returnos usando condicional, retornando apenas 1 valor
#pode em 1 função retornar qualquer tipo de dado ou multiplos valores

from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'