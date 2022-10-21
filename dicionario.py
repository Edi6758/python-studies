"""
dicionários
obs: Em algumas linguagens os dicionários são mapas

eles são representados por {}

tanto as chaves quanto os valores podem ser de qualquer tipo
"""

# forma 01
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'paraguai'}

# forma 02
paises = dict(br='Brasil', eua='Estados unidos', py='paraguai')

# acessando elementos

# forma 01 - Acessando via chaves
paises['br']  # Brasil
paises['ru']  # Key error

# forma -2 - Acessando via get
paises.get('br')  # Brasil
paises.get('ru')  # None

# o porque de usar get
russia = paises.get('ru')

if (russia):
    print("Encontrei o país")
else:
    print("Não encontrei o país")
    # ele vai retornar o else pq o None sempre é falso

# deixando essa validação mais simples
pais = paises.get('ru', 'Não encontrado')
# aqui ele poem um valor pré definidi ocaso o país não seja encontrado

# podemos pesquisar valores através das chaves

'br' in paises
'ru' in paises

# criando um dicionário usando tupla como chave

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}

# adiconar elementos
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# forma 01
receita['abr'] = 350

# forma 02
novo_dado = {'mai': 500}
receita.update(novo_dado)

# forma 03
receita.update({'mai': 500})

# atulizando dados
receita['abr'] = 600
# basicmanete a atualização de dados acotnece uando tu tenta mudar o valor de uma chave já existente

# como remover dados
receita = {'jan': 100, 'fev': 120, 'mar': 300}
receita.pop('jan ')

# zerar dados
receita.clear()

# copiando um dicionário para outro
novo = receita.copy()
