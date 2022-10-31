"""
conjuntos ou sets não possuim valores duplicados
conjuntos não possuem valores ordenados
conjuntos não são indexados

conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos para a ordenação deles

os conjuntos são referenciados em python com {}

diferença entre conjuntos(set) e mapas(dicionario)
- um conjunto tem chave e valor
- um dicionario tem apenas valor

da pra usar os métods vistos anteriormente em sets também
"""

# definindo um conjunto
s = set({1, 2, 3, 4, 5, 6, 7})

# no exemplo abaixo os valores repetidos são excluidos
s2 = set({1, 2, 3, 4, 5, 6, 7})

# verificar se o elemento existe
if 14 in s:
    print("tem")
else:
    print("não tem")

# listas aceitam valores duplicados
# tuplas aceitam valores duplicados
# dicionarios não aceitam chaves suplicados
# conjuntos n aceitam valores duplicados

# assim como todo outro conjunto em python, podemos colocar tipos de dados misturados em sets

# usos interessantes com sets

# imagine um cadastro em uma feira ou museu
# os visitante informa manualmente a cidade de onde vieram
# cada cidade é adicionado em uma lista python. ja que uma lista pode adicionar novos elementos e ter repetição

cidades = ['belo horizonte', 'são paulo',
           'floripa', 'são paulo', 'belo horizonte']

# pra pegar as cidade sem rpeetição é so por em um set
set(cidades)

# duplicidade não gera erro, ele simplemente ignora
s.add(3)
s.add(3)

# remoção de valores
s.remove(3)

# copiando conjunto
s3 = set({1, 2, 3, 4, 5, 6, 7})
novo = s3.copy()

# métodos matemáticos de conjuntos

# imagine que existe um conjunto de estudantes de python e um conjunto de estudantes de java

estudantes_python = {'marcos', 'patricia',
                     'elsen', 'pedro', 'julia', 'gabriel'}
estudantes_java = {'daniel', 'patricia',
                   'rafael', 'samuel', 'julia', 'gabriela'}

# existem estudantes que fazem os 2 cursos

# precisamos gerar um conjuntos com os nomes de estudantes únicos

# forma 1 - union
unicos1 = estudantes_java.union(estudantes_python)
# vai imprimir todos os estudantes sem repetir

# forma 2 - usando o caracter pipe |
unicos2 = estudantes_java | estudantes_python

# gerar uma lista de estudantes que estão nos 2 cursos

# forma 1 - intersection
ambos1 = estudantes_java.intersection(estudantes_python)

# forma 2 - &
ambos2 = estudantes_java & estudantes_python

# estudantes de apenas um curso
# so java
so_java = estudantes_java.difference(estudantes_python)

# so python
so_python = estudantes_python.difference(estudantes_java)
