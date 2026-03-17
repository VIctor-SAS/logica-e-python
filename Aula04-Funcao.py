#funcao - bloco de codigo criado para executar uma tarefa especifica

def saudacao():
    print('Ola')

"""
- Def cria a funcao
- saudacao e o nome dela
- () indica os parametros
- O bloco identado e o que ela faz

"""

# Criar nao eh so executar

""" 
So escrever nada acontece
eh necessario chamar a funcao

"""

# Exemplo chamar funcao

def saudacao():
    print('Ola')

saudacao()


# Funcao com parametro - informacao que a funcao recebe

def saudacao(nome):
    print(f'ola, {nome}!')

saudacao("Victor")


# Parametro x Argumento
# E a variavel na definicao da funcao

# def saudacao(nome): #-- Parametro nome

# saudacao('Victor') #-- Argumento eh o valor passado na chamada "Victor"


# funcao com mais de um parametro

def somar(a, b):
    print(a + b)

somar(3, 5)


# Return -- return serve para devolver um valor

def somar(a, b):
    return a + b

"""
Agora a funcao ano so mostra algo
Ela entrega um resultado
Voce pode guardar esse resultado

"""

resultado = somar(3, 5)
print(resultado)

#saida 8


"""
Diferenca entre Print e return

"""

# Print

def somar(a, b):
    print(a + b)

# Isso mostra o resultado, mas nao devolve nada a ser reutilizado.

# return

def somar(a, b):
    return a + b

"""
Isso devolve um valor, entao voce pode:
- Guardar em variavel.
- usar em outra conta.
- passar para outra funcao.
- comparar depois.

"""

# Exemplo pratico

# print

def dobro(numero):
    print(numero * 2)

resultado = dobro(5)
print(resultado)

"""
Saida:
10
none
"""

# Versao com return

def dobro(numero):
    return numero * 2

resultado = dobro(5)
print(resultado)

# Saida = 10

# funcao pode devolver texto tambem

def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
mensagem = verificar_maioridade(20)
print(mensagem)


"""
        Beneficios de usar funcao

    Reaproveitamento
- Voce escreve uma vez e usa varias.
    Organizacao
- Seu codigo fica divido em partes claras.
    Leitura melhor
- Fica mais facil entender o que cada parte faz.
    Base profissional
-Projetos reais usam funcao o tempo todo.

"""

# exemplos importantes.

# Ex01 - funcao que mostra seu nome

def mostrar_nome():
    print('Victor')
mostrar_nome()

# Ex02 - Funcao que recebe numero e mostra dobro

def mostrar_dobro(numero):
    print(numero * 2)
mostrar_dobro()

# Ex03 - Funcao que retorna o dobro

def calcular_dobro(numero):
    return numero * 2

resultado = calcular_dobro(10)
print(resultado)

# Ex04 - Funcao para somar

def somar(a, b):
    return a + b

print(somar(4, 6))


# Erros comuns

# Erro 01 -Criar funcao e noa chamar

def teste():
    print('oi')


# Erro 02 - Confundir print com return
# se for reaproveitar o valor, normalmente voce quer return


# Erro 03 - Passar quantidade errada de argumentos

def somar(a, b):
    return a + b

somar(5)

