"""
dicionario = {'a': 1}
{chave:valor for valor in interavel}
"""

#exemplos...

numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

#outro exemplo
numeros = [1,2,3,4,5,6,7,8,9,10]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros }

