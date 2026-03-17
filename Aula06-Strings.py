# 01 - String.

nome = "Victor"
senha = "python123"
cidade = "Campo grande"
frase = "Estou estudando programacao"

# 02 - cada caracter tem uma posicao.
# assim como lista, string tem indice.

# Exemplo

nome = "Victor"

"""
nome[0] -> V
nome[1] -> i
nome[2] -> c

"""

# 03 - Acessando caracteres.

nome = "Victor"

print(nome[0])
print(nome[1])
print(nome[2])

# 04 - Ultimo caractere.

nome = "Victor"

print(nome[-1]) # possivel usar indice negativo para colocar sempre o ultimo indice.



# 05 - Tamanho do texto com len().

nome = "Victor"
print(len(nome))

# saida = 6.


# 06 - Maiusculo e Minusculo.

# Maiusculo.
nome = "Victor"
print(nome.upper())

# Minusculo.
nome = "Victor"
print(nome.lower())

# 07 - Remover espacos com strip().

nome = "    Victor   "
print(nome.strip())
# Isso remove espacos do comeco e do fim.

# 08 - Comparar textos

senha = input("Digite a senha: ")

if senha == "python123":
    print('Acesso permitido')
else:
    print("Acesso negado")


# 09 - Comparar ignorando maiuscula/minuscula.
"""
Exemplo
 -"Victor"
 -"victor"
 -"VICTOR"

Voce pode normalizar antes.
"""

nomes = input("Digite seu nome: ").strip().lower()

if nome == "victor":
    print("Nomes reconhecido")


# 10 - Verificar se um texto esta dentro de outro.
# use in.

frase = "Estou estudando Python"

if "Python" in frase:
    print("Encontrado")


# 11 - Percorrer uma string com for.

nome = "Victor"

for letra in nome:
    print(letra)

# Imprime uma letra por linha.

# 12 - Contar vogais - exemplo de logica com string.

texto = input("Digite uma palavra: ").lower()
contador = 0

for letra in texto:
    if letra in "aeiou":
        contador += 1
print(f"Quantidade de vogais: {contador}")

# 13 - Erros comuns.

"""
 Erro 01 - Esquecer que string tambem comeca no indice 0.

 Erro 02 - Comparar texto sem tratas espacos.
 exemplo:
    o usuario digita "  victor " e voce compara com "Victor".
    sem strip(), pode falhar.

    
 Erro 03 - comparar sem padronizar maiuscula/minuscula.
    Exemplo:
    "Victor" E diferente de "victor".
"""


# 14 - Metodos mais uteis por agora.
"""
upper()
Transforma em maiusculo.

lower()
Transforma em minusculo.

strip()
Remove espacos de comeco e de fim.

len()
Tamanho do texto.

"""

# 15 - Exemplos importantes.

# Exemplo 01 - Mostrar primeira letra.

nome = input("Digite seu nome: ")
print(nome[0])


# Exemplo 02 - Mostrar quantidade de letras.

nome = input("Digite seu nome: ")
print(len(nome))

# Exemplo 03 - Normalizar nome.

nome = input("Digite seu nome: ").strip().lower()
print(nome)

# Exemplo 04 - verificar palavra dentro da frase.

frase = input('Digite uma frase: ')

if "python" in frase.lower():
    print('A frase contem a palavra python')
else:
    print('A frase nao contem a palavra python')








