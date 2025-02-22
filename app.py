import random 

# Letras, números e caracteres a serem usados no projeto para gerar as senhas aleatórias. 
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_=+<>?/{}[]"

tamanho = 20

# Unificando todos caractes em uma só variavel. 
def gerar_senha(tamanho):
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    return ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

senha = gerar_senha(tamanho)
print('Sua senha é:', senha)
