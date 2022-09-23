"""
Ranges
- conhecer o for é necessário para usar o range.
- precisamos conhecer o ranger para aprimorar o for
- range forma sequencias númericas de forma especificada

formas de usar o range
- range(valor_de_parada)
- OBS: valor de parada não inclusive (inicio padrao 0, e passo de 1 em 1)
(se vcc colocar 10 vai até 9, é sempre -1)
"""

# forma 1 - mais simples
for num in range(11):
    print(num)

# forma 2 - valor de inicio, valor de parada
for num in range(1, 11):
    print(num)


# forma 3 - valor de inicio, valor de parada, passo
for num in range(0, 10, 2):
    print(num)

# forma 4 - contagem regressiva
for num in range(10, 0, -1):
    print(num)
