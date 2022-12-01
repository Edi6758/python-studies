"""
entendendo o *args

- o *args é um parâmetro, como outro qqr. isso significa que você poderá chamar de qrr coisa, desde que comece com *

- oq é o *args?
o parâmetro args pega os valores extras informados como entrada e coloca em uma tupla
"""

def soma_todos_valores(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

#como é uma tupla, pode ser feito assim
def soma_todos_valores(*args):
    return sum(args)
    
    

soma_todos_valores(1,2) #retorna uma tupla
soma_todos_valores(1,2,3) #retorna uma tupla
soma_todos_valores(1,2,3,4) #retorna uma tupla

#uma função não precisa ter apenas o args
def funcao_qualquer(*args, nome, email):
    pass