contador = 1

while contador <= 5:
    print(contador)
    contador += 1

# - enquanto contador <= 5
# - imprima
# - aumente 1

senha = ""

while senha != "python123":
    senha = input("Digite a senha: ")

print("Acesso permitido")


for i in range(5):
    print(i)

print("------------------------")
for i in range(1, 6):
    print(i)

print("------------------------")

# x = aonde comeca, y = 1 acima do limite, z = frequencia
for i in range(0, 10, 2):
    print(i)

print("------------------------")

soma = 0

for i in range(1, 6):
    soma += i
print(f"Soma total: {soma}")


# Contador

# contador = 1

while contador <= 3:
    print(contador)
    contador += 1

# Aqui o contador vai: - variavel usada para contar.
# - 1
# - 2
# - 3

# Acumulador

soma = 0

for i in range(1, 6):
    soma += i
    print(soma)
print(soma)

