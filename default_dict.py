"""
módulo collections - default dict

basicamente não da o key erro quando vc tenta acessar um dicionario com uma chave que não existe

é mais performatico

tu pode atribuir um valor padrão caso a chave n exista

você sempre salva a chave que o usuario buscou errado com um valor default

"""
from collections import defaultdict


dicionario = defaultdict(lambda: 0)
dicionario = {'cursos': 'programação em python'}
# normalmente gera um key error mas nesse exemplo aqui não...
print(dicionario['outros'])
