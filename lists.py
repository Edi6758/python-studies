"""
listas em python são como vetores/matrizes

outro detalhe é que eles são dinâmicos, 
não possuem tamanho físico, ou seja podemos criar a lista e ir adicionando elementos
com 

"""

type([])
# <class 'list'>

lista1 = [1, 99, 4, 27, 4, 434, 56, 3]
lista2 = ['g,', 'e', 'v', 'r', 's', 'u', 'i']
lista4 = list(range(11))  # lista de 0 a 10
lista5 = list('Geek University')  # ['G', 'e', 'e' ... ]

# checar se determinado valor existe na lista
num = 18
if num in lista4:
    print("encontrei o número")
else:
    print("não encontrei o número ")

# mesmo teste só que com string
char = 'e'
if char in lista5:
    print("encontrei a letra")
else:
    print("não encontrei a letra")

# ordenação de lista
lista1.sort()
print(lista1)

# ordenação de caracteres
lista5.sort()

# podemos contar o número de ocorrência de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# add valor ÚNICO na lista
lista1.append(42)  # só pode adicionar um elemento por vez
# lista1.append(23, 45, 67) erro
lista1.append([8, 3, 1])  # add um objeto do tipo lista

# add valor interável, varios valores
lista1.extend('geek')

# inserir novo elemento informando a posição do índice
# isso não substitui o valor inicial, apenas desloca para a direita....
lista1.insert(2, 'Novo valor')

# juntar listas
lista6 = lista1 + lista2
lista1.extend(lista2)

# inverter lista
lista1.reverse()
lista2.reverse()

lista1[::-1]
lista2[::-2]

# copiar lsita
lista6 = lista2.copy()

# contar elementos na lista
len(lista1)

# remover o ultimo elemento da lista
lista5.pop()

# remover o elemento pelo indice
lista5.pop(4)

# limpar uma lista
lista5.clear()

# converter string pra lista
curso = 'Programação em python'
curso = curso.split()
curso = curso.split(',')

lista7 = ['programação', 'em', 'python']

# converter lista pra strinf
# pega a lista 7, coloca espaço entre cada elemento e cria uma string
curso = ''.join(lista7)

# iteração sobre lista com for
for elemento in lista1:
    print(elemento)

carrinho = []
produto = ''

# testando...
while produto != 'sair':
    print("Add um produto na lista ou digite sair para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# as listas são ciclicas, você pode acessar de forma inversa

#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
# acesso normal
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# acesso inverso
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
print(cores[-5])  # erro

# gerar indice em um for
for indice, cor in enumerate(cores):  # criando chave e valor com o enumarate
    print(indice, cor)

# lista aceitam repetições
lista = []
lista.append(42)
lista.append(42)

# achar o indice de um elemento na lista, retorna erro se n achar nada e se tiver mais que 1 ele retorna o primeiro encontrado
numeros = [6, 7, 8, 5, 4, 6, 7, 8, ]
numeros.index(9)

# fazer busca determinando por qual indice você quer começar a buscar
numeros.index(5, 1)  # buscando o 5 a partir da 1
numeros.index(5, 2)  # buscando o 5 a partir da 2

# é possível fazer busca de dentro de um range(), início e fim
numeros.index(8, 3, 6)

# trabalhando com lista no parâmetro passo
lista = [1, 2, 3, 4]
lista[1::2]  # começa em 1, vai até o final de 2 em 2
lista[::2]  # começa em 0, vai até o final de 2 em 2
lista[:2]  # começa em 0, e vai até o indice 2-1
lista[:4]  # começa em 0, e vai até o indice 4-1
lista[1:3]  # começa em 1, e vai até o indice 3-1

# transformar lista em typla
lista = [1, 2, 3, 4]
type(lista)  # list

tupla = tuple(list)
type(tupla)  # list

# desempacotar lista
lista = [1, 2, 3]

num1, num2, num3 = lista

# copiando uma lista para outra (shallow copy, deep copy)

lista = [1, 2, 3]

# deep copy
novaLIsta = lista.copy()  # toda modificação nessa lista n afeta a anterior, se fosse apenas uma atribuição, a modificação de 1 afetaria a outra, isso se chama deep copy

lista = [1, 2, 3]
# nessa caso toda alteração em novaLista afeta a lista normal...
novaLIsta = lista
