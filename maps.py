"""
Mapas => conhecidos no Python como dicionários
"""

from numpy import rec


receitas = {'jan': 100, 'fev': 250, 'mar': 400}

# interar com ficionario
for chave in receitas:
    print(chave)

for chave in receitas:
    print(receitas[chave])

for chave in receitas:
    print(f"Em {chave} recebi R$ {receitas[chave]}")

# acesso a todas as chaves
receitas.keys

# desempacotamento de dicionarios

for chave, valor in receitas.items():
    print(chave, valor)

# soma, maximo, minimo e tamanho
sum(receitas.values())
max(receitas.values())
min(receitas.values())
len(receitas)
