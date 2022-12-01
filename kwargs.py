"""
**kwargs
kwargs é um parâmetro que exige que utilizemos parâmetros nomeados transformando esses parâmetors em um dicionário

- os parâmetros *args e **kwargs não são obrigatórios
"""

def cores_favoritas(**kwargs):
    print(kwargs)
    
cores_favoritas(edi="verde", rafa="azul", jose="verde")

def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'vc recebeu um cumprimento pythônico...'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não reconheço você...'