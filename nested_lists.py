"""
Listas aninhadas

- no python não existe array, existe lista
"""

listas = [[1,2,3],[4,5,6],[7,8,9]] #lista de listas...
listas[0][1] #2 - linha e coluna...

#iterando com loop em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num) #1,2,3,4,5,6,7,8,9
        
#list comprehension...
[[print(valor) for valor in lista] for lista in listas]