"""
Tuplas são bem parecidas com listas
elas possuem 2 diferenças básicas
1 - As tuplas são representadas por ()
2 - As tuplas são imutáveis, toda alteração em uma tupla, gera uma nova tupla...    
"""

# CUIDADO 1: as tuplas são representadas por (), no entanto...
tupla1 = (1, 2, 3, 4, 5, 6)
type(tupla1)  # <class 'tuple'>

tupla2 = 1, 2, 3, 4, 5, 6
type(tupla2)  # <class 'tuple'>

# CUIDADO 2: tentar criar tupla com só um elemento
tupla3 = (3)  # isso não é uma tupla
type(tupla3)  # <class 'int'>

tupla4 = (4,)  # isso é uma tupla
type(tupla4)  # <class 'tuple'>

tupla5 = 5,  # isso é uma tupla
type(tupla4)  # <class 'tuple'>

# CONCLUSÃO: tuplas sãop definidas pela vŕgula e não pelo parênteses

# Podemos gerar uma tupla dinamicamente com range(início,fim,passo)
tupla = tuple(range(11,))

# desempacotamento de tupla
tupla = ('geek', 'university')

escola, ensino = tupla  # escola e ensino recebe os valores que estão dentro de tupla

# da pra fazer operações com tuplas tb sendo elas inteiras ou reais

tupla(1, 2, 3, 4, 5)

sum(tupla)  # soma
max(tupla)  # valor máximo
min(tupla)  # valor mínimo
len(tupla)  # tamanho

# concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla1 = tupla1+tupla2  # tuplas são imutáveis, mas vc pode sobreescrever seus valores

# verificar se determinado valor ta na tupla
3 in tuple


# interando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

# contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e')

tupla.count('c ')

# onde usar tuplas
# sempre quando n for necessário mudar os dados de uma coleção
# meses
# dias da semana

# tuplas são mais rápidas do que listas...
# tuplas aplicam o conceitam de imutabilidade
