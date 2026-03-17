"""
01. O que e uma lista
Estrutura que guarda varios valores em uma unica variavel

"""
numero = [10, 20, 30, 40]

# Variavel numero guarda 4 valores

"""
02 . Lista de textos

"""

nomes = ["Victor", "Ana", "Carlos"]


"""
03. Indice da lista
cada elemento da lista tem uma posicao
    Regra importante
Em python, a contagem comeca em 0.

"""

nomes = ["Victor", "Ana", "Carlos"]

"""
nomes[0] -> "Victor"
nomes[1] -> "Ana"
nomes[2] -> "Carlos"

"""


# 04. Acessando elementos

nomes = ["Victor", "Ana", "Carlos"]

print(nomes[0])
print(nomes[1])
print(nomes[2])


# 05. Modificando um elemento

nomes = ["Victor", "Ana", "Carlos"]
nomes[1] = "Beatriz"

print(nomes)

# 06 - Descobrindo o tamanho da lista
# Use len():

nomes = ["Victor", "Ana", "Carlos"]
print(len(nomes))


# 07 - Adicionando um elemento
# Use append():

nomes = ["victor", "Ana"]
nomes.append("Carlos")

print(nomes)


# 08 - Removendo elemento
# Use remove():

nomes = ["Victor", "Ana", "Carlos"]
nomes.remove("Ana")

print(nomes)


# 09 - Percorrendo lista com For
# Esse e um dos pontos mais importantes da aula.

nomes = ["Victor", "Ana", "Carlos"]

for nome in nomes:
    print(nomes)

"""
Aqui:
 - nomes e a lista
 - nome e a variavel que vai receber cada item da lista
"""

# 10 - lista com numeros e soma

numeros = [10, 20, 30, 40]
soma = 0

for numero in numeros:
    soma += numero

print(soma)

# 11 - Encontrando o maior valor

numeros = [8, 10, 20, 50]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(maior)

# 12 - Encontrando o menor valor

numeros = [8, 10, 20, 50]
menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print(menor)

# 13 - Lista vazia - tambem pode comecar com a lista vazia

numeros = []

# E ir adicionando

numeros.append(10)
numeros.append(20)
numeros.append(30)

# 14 - Preenchendo lista com [input]

numeros = []

for i in range(3):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

print(numeros)


# Aqui o usuario digita 3 numeros, e eles sao guardados na lista.

# 15 - Erros comuns.

# Erro 01 - tentar acessar a posicao que nao existe.

nomes = ["Victor", "Ana"]
print(nomes[1])
"""
Isso da erro, porque so existem:
 - 0
 - 1
"""

# Erro 02 - esquecer que comeca em 0.
# isso e muit comum no comeco


# Erro 03 - Confundir item com indice.

# Percorrendo item:

for nome in nomes:
    print(nome)

# Percorrendo indice:

for i in range(len(nomes)):
    print(nomes[i])

# Os dois funcionam , mas tem usos diferentes.


# 16 - Exemplos importantes:

# Exemplo 01 - mostrar todos os nomes.

nomes = ["Victor","Ana","Carlos"]

for nome in nomes:
    print(nome)

# Exemplo 02 - somar numeros.

numeros = [1, 2, 3, 4, 5, 6]
soma = 0

for numero in numeros:
    soma += numero

print(soma)


# Exemplo 03 - maior numero

numeros = [1, 2, 3, 4, 5, 6]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    print(maior)
print(maior)