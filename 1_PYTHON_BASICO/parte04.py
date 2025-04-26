# Constante no Python
"""
    Constante no Python é só questão de sintaxe para não
    repetir atribuição aquela variável no código.
"""

velocidade = 60
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print("Velocidade do carro passou do radar1")
    
if local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print("Carro multado em radar 1")
    
    
#  Identificadores ID

v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))


# Desafios da Aula 54

# Desafio 01:
# int_number = input("Digite um número inteiro: ")

# try:
#     if int_number.isdigit():
#         odd_or_even = "Par" if int(int_number) % 2 == 0 else "Ímpar"
#         print(odd_or_even)
#     else:
#         raise ValueError("Entrada inválida!")
# except ValueError:
#     print("Erro, você não digitou um número!")
# except:
#     print("Erro do sistema, tente novamente!")
# else:
#     print(f"Você digitou {int_number} e o valor é {odd_or_even}")
# finally:
#     print("Fim!")



# Desafio 02:
# time = input("Que horas são agora?")

# if not time.isdigit():
#     print("Erro, você não digitou um número")

# try:
#     time = int(time)
#     if time >= 0 and time <= 11:
#         print("Bom dia, usuário!")
#     elif time >= 12 and time <= 17:
#         print("Boa tarde, usuário!")
#     elif time >= 18 and time <= 23:
#         print("Boa noite, usuário!")
#     else:
#         print("Digite uma hora válida: 0-23")
# except:
#     print("Erro no sistema, tente novamente!")
# finally:
#     print("Fim!")



# Desafio 03

# name = input("Digite seu nome?")
# name_length = len(name)

# if not name.isalpha() or name_length <= 1:
#     print("Você não digitou um nome!")
# else:
#     try:
#          if name_length >= 2 and name_length <= 4:
#              print("Seu nome é pequeno!")
#          elif name_length >= 5 and name_length <= 6:
#              print("Seu nome é normal")
#          else:
#              print("Seu nome é muito grande!")
#     except:
#         print("Erro do servidor!")
#     else:
#         print(f"{name} seu nome tem {name_length} digitos.")
#     finally:
#         print("Fim!")


# While e Break

contador = 0

while contador < 18:
    print(contador)
    contador += 1
    
    if contador == 17:
        break