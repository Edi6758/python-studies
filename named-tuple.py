"""
tupla nomeada
tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros
"""

# importando
from collections import namedtuple

# forma 01

# 3 variáveis para 1 cachorro
cachorro = namedtuple('cachorro', ['idade raca nome'])
ray = cachorro(idade=2, raca="vira lata", nome="ray")

print(ray)
