"""
while expressão booleana:
    //execução do loop
    
o bloco do while sera repetido enquanto a expressão booleana for verdadeira.

expressão boolenaa é toda expressão onde o resultado é verdadeiro ou falso
por ex:
num = 5
num < 5
true
"""

# Ecemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

# Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input("Já acabou jéssica?")
