"""
serve para finalizar uma condição lógica
usamos pra air de loop de forma projetada
"""

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")

while True:
    comando = input("DIgite 'sair' para sair")
    if comando == 'sair':
        break
