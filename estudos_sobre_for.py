"""
loop for
loop -> estrutura de repetição.
For -> Uma dessas estruturas

no geral na maiorias das linguagens a sintaxe é assim:
for(int i = 0; i < 10; i++){
    //faz algo no loop...
}

já no python
for item in interável:
    //faz algo no loop...
    
valores interavéis no python são valores que você consegue manipular
- string
    nome = edi,
lista
    lista = [1,3,5,7],
"""

nome = "edivaldo jr"
lista = [1, 3, 5, 7]
numeros = range(1, 10)

# exemplo de for 1
for letra in nome:
    print(letra)
    # para cada letra dentro do interável nome, imprima as letras

# exemplo de for 2
for numero in lista:
    print(numero)
    # para cada numero na lista imprima um número

# range
"""
range(valor_inicial, valor_final)
OBS: O valor final não é incluso
basicamente ele pega o valor final do range e adicionar um -1
"""
for numero in range(1, 10):
    print(numero)

# enumerate
"""
Enumerate:
((0, 'e'),(1, 'd'),(2, 'i'),(3, 'v'),(v, 'a')...)
o Enumerate gera um objeto que cria uma tupla com a posição de cada letra da lista
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

# exemplo de for 3
for indice, letra in enumerate(nome):
    print(letra) #faz a msm coisa do for de cima...

# exemplo for 4
"""
quando não precisamos de um valor a gente pode descartar ele usando underline '_' 
"""
for _, letra in enumerate(nome):
    print(letra)

# exemplo 5
#para cada valor dentro do interavel enumerate...
for valor in enumerate(nome):
    print(valor)
    
# exemplo 6
qtd = int(input('Quantas vezes esse loop deve rodar?'))
for n in range(1, qtd):
    print(f'Imprimindo {qtd}')
#lembrando que o valor digitdo dentro range é sempre -1

# exemplo 7
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')

# exemplo 8 
"""
por padrão o python colocar um \n após uma impressão no print dentro de um loop, para corrigir esse problemas o ideal é definir que o final do loop vai ser vazio
"""
for letra in nome:
    print(letra, end='')

#EXEMPLO 9    
#emoji com python
"""
entrar no site timwhitlock.info e procurar o emoji desejado
ex: U+1F60D
após isso você precisa modificar removendo o + e colocando 3 zeros
exe: U0001F60D
"""

for num in range(1,11):
    print('\U0001F60D' * num)