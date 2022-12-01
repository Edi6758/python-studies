"""
criação de lists com dados processados a partir de outro interável (coleção de dados)

"""

numeros = [1,2,3,4,5,6]

res = [numeros * 10 for numero in numeros]

print(res) 