"""
criação de lists com dados processados a partir de outro interável (coleção de dados)

"""

numeros = [1,2,3,4,5,6]

res = [numero * 10 for numero in numeros]

print(res) 

# exemplo de utilização

nome = "edivaldinho"
print([letra.upper() for letra in nome])

# adição de estruturas condicionais lógicas n list_comprehension...


numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares) #vai receber os números pares de numeros

# multiplicando números

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]