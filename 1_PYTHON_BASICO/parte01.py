
#Docstrings
"""
"""

# Aula print

print("A", "B", "C", sep="-");
print(12, 34, 1011, sep="-", end="#\n")

# Aula sobre tipo string str

texto1 = "Olá"
texto2 = "Mundo"

print(texto1, texto2, sep=", ")

# Escape \" Nos permite utilizamos caracteres de fechamente e abertura 
print("Murilo \"Santos")
print('Murilo "Santos"')


# Aula sobre tipos númericos int e float
numero1 = 10

print(10 + 10) # int
print(10.2 + 15.5) # float
print(type(numero1))

## Aula sobre tipo boleano bool

print(10 > 15)
print(bool(0))
print(10 == 10)

# Aula sobre Conversão de tipos
numeroInt = 10
numeroFloat = float(numeroInt)
numeroParaStr = str(numeroInt)

# Aula sobre Variáveis
nome_completo = "Murilo dos Santos Barbosa"
print(nome_completo)

# desafio 

nome = "Murilo"
sobrenome = "Dos Santos Barbosa"
idade = 18
ano_nascimento = 2006
maior_de_idade = idade >= 18
altura_metros = 1.76

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de Idade?", maior_de_idade)
print("Altura em metros:", altura_metros)


# Aula operadores aritméticos 
adicao = 10 + 10
print("Adição:", adicao)

subtracao = 10 - 5
print("Subtação:", subtracao)

multiplicacao = 10 * 3
print("Multiplicação:", multiplicacao)

divisao = 10 / 2.2
print("Divisão:", divisao)

divisao_inteira = 10 // 2.2
print("Divisão inteira:", divisao_inteira)

modulo = 55 % 2
print("Resto de divisão:", modulo)

exponencial = 2 ** 3
print("Exponencial:", exponencial)

# Aula concatenação
concatenacao = "Murilo" + ' ' + "Santos"
print(concatenacao)

a_dez_vezes = "A" * 10
tres_vezes_murilo = 3 * "Murilo"
print(a_dez_vezes)
print(tres_vezes_murilo)

print('Idade: ' + str(idade))

# Concatenação moderna
print(f"Nome: {nome}, Idade: {idade}")



# Desafio calculo do IMC
nome = "Murilo Santos"
altura = 1.77
peso = 76
imc = peso / (altura * altura)

print(f"{nome} tem {altura} de altura")
print(f"Pesa {peso} quilos e seu IMC é {imc:.2f}")
