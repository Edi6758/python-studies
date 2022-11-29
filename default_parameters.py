"""
funções com parâmetro padrão (default parameters)
função onde a passagem de parâmetro é opicional
"""

#parametro obrigatório...
def quadrado(numero):
    return numero ** 2

def exponencial(numero, potencia=2):
    return numero ** potencia

exponencial(3) #por padrão eleva ao quadrado
exponencial(3,3) #tu escolhe o valor da potência, substituindo o valor padrão
