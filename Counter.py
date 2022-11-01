"""
high-performace

recebe um interavel como parâmetro e cria um objeto do tipo collections Counter que é parecido com um dicionário

"""

# estamos usando uma lista, mas pode ser qualquer interável (lista, tupla, etc )
lista = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

# aqui ele vai por o valor como chave e a quantidade de ocorrencia como valor
res = Counter(lista)
