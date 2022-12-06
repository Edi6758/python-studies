"""
    são funções sem nomes...
"""

def funcao(x):
    return 3 * x + 1

#Empressão lambda 
lambda x: 3 * x + 1

#como usar uma expressão lambda
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas...

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

amar = lambda: 'como não amar python'
uma = lambda x: 3 * x + 1
duas = lambda x,y: (x*y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z) 

#usando o lambda na prática
# Função quadratica 
# f(x) = a*x**2+b*c+c
def geracao_funcao_quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c