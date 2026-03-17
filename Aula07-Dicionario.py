# 01 - O que um dicionario.

# Dicionario e uma estrutura que guarda dados em formato:

chave: valor

# Exemplo.

pessoa = {
    "nome": "Victor",
    "idade": 20,
    "cidade": "Campo Grande"
}

"""
nome e a chave
Victor e o valor
idade e a chave
20 e o valor
"""

# 02 - Diferenca de lista e dicionario.

# Lista.

nomes = ["Victor", "Ana", "Carlos"]
print(nomes[0])

# Dicionario.

pessoa = {"nome": "Victor", "Idade": 20}
print(pessoa["nome"])

# 03 - Criando um dicionario.

aluno = {
    "nome": "Victor",
    "idade": 22,
    "curso": "Ciencia da computacao"
}

# 04 - Acessando valores.

print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])

# 05 - Alterando um valor.

aluno["idade"] = 23
print(aluno)

# 06 - Adicionando novo par chave/valor.

aluno['cidade'] = "Campo Grande"
print(aluno)
# Agora o dicionario passou a ter uma nova informacao.

# 07 - Removendo um item.

del aluno['curso']
print(aluno)


# 08 - Percorrendo um dicionario.
# Percorrendo as chaves.

pessoa = {"nome": "Victor", "Idade": 22}

for chave in pessoa:
    print(chave) # saida - nome / idade

# Percorrendo valores pelas chaves.

for chave in pessoa:
    print(chave, pessoa[chave]) # saida = nome Victor, idade 22


# 09 - metodo items()

for chave, valor in pessoa.items():
    print(chave, valor)

"""
isso percorre:
 - chave
 - valor
 ao mesmo tempo.
"""

# 10 0 metodo keys() e values().

# So chaves.

for chave in pessoa.keys():
    print(chave)

# So valores

for valor in pessoa.values():
    print(valor)

# 11 - Exemplo pratico - usuario

usuario = {
    "nome": "Victor",
    "email": "victor@gmail.com",
    "idade": 22,
    "Ativo": True
}

print(usuario["nome"])
print(usuario["email"])
print(usuario["idade"])
print(usuario["ativo"])

# 12 - Exemplo pratico - produto

produto = {
    "nome": "Teclado",
    "preco": 150.0,
    "estoque": 10
}

print(f"Produto: {produto['nome']}")
print(f"Preco: {produto['preco']}")
print(f"Estoque: {produto['estoque']}")

# 13 - Erros comuns

# Erro 01 - acessar cahve que nao existe.

pessoa = {"nome": "Victor"}
print(pessoa["idade"])

# Isso da erro


# Erro 02 - confundir lista com dicionario.

# lista usa indice:

lista[0]

# Dicionario usa chave:

dicionario["nome"]

# Erro 03 - esquecer aspas na chave string.

# Certo

pessoa["nome"]

# Errado

pessoa[nome]

# se nome nao for uma variavel definida, isso da erro.

# 14 - Exemplo com input.

pessoa = {}

pessoa["nome"] = input("Digite o nome: ")
pessoa["idade"] = int(input("Digite a idade: "))
pessoa["cidade"] = input("Digite a cidade: ")

print(pessoa)


# 15 - Exemplo com impressao organizada.

pessoa = {
    "nome": "Victor",
    "idade": 22,
    "cidade": "Campo Grande"
}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

    