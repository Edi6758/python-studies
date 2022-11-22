#função sem entrada, sempre faz a mesma coisa

def quadrado_de_7():
    return 7 * 7


#função com entrada, pode variar a saída
def quadrado(numero):
    return numero ** 2

def cantar_parabens(aniverssariante):
    return f"parabens pra vc nessa data querida...{aniverssariante}"

#funções podem ter N parâmetros
def soma(a,b):
    return a+b

#parametros sao variaveis declaradas na definição de uma função
#argumentos são dados passados durante a execução da função

def multiplicar(a,b): #parametros
    return a*b

multiplicar(3,5) #argumento

#argumentos nomeados
def diminuir(a="1", b="2"):
    return a-b