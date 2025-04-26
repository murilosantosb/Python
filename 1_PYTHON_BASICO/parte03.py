# Operadores in e not in

frutas = ["maçã", "banana", "pera"]

# IN usado para procura valores presentes
if "banana" in frutas:
    print("Tem banana")
    
# NOT IN usado para verificar se os valores estão ausentes
if "melância" not in frutas:
    print("Não está na lista")
   
    
#  Intepolação de string com %

"""
    %s para strings
    %d para números inteiros
    %f para número de ponto flutuante
"""

nome = "Murilo"
idade = 18
altura = 1.77

print("Nome do usuário: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)


# Avançando em f-strings

variavel = "ABC"
price = 12345687.55454

print(f"{variavel:>10}")
print(f"{variavel}")
print(f"Preço: {price:,.2f}")

# Fatiamento de strings e função len()

# Função len()
lista = ["Python", "JavaScript", "PHP"]
print(len(lista))


# Fatiamento de Strings

palavra = "Programar"

print(palavra[0])
print(palavra[0:])
print(palavra[4:])
print(palavra[:4])
print(palavra[3:7])
print(palavra[::2]) # pula de 2 em 2 letras
print(palavra[::-1]) # Inverte a string


# Desafio da Aula 47

user_name = input("Digite seu nome:")
user_age = input("Digite sua idade:")
your_name_has_spaces = "Sim" if " " in user_name else "Não"

message = (
    f"Seu nome é {user_name}\n"
    f"Seu nome invertido é {user_name[::-1]}\n"
    f"Seu não contém espaços: {your_name_has_spaces}\n"
    f"Seu nome tem {len(user_name.replace(" ", ""))} letras\n"
    f"A primeira letra do seu nome é {user_name.strip()[0]}\n"
    f"A última letra do seu nome é {user_name.strip()[-1]}"
)

if user_name and user_age:
    print(message)
else:
    print("Desculpe, você deixou campos vazios.")    

# Condicionais ténarias

nota = 10

condicao_nota_do_aluno = "Aprovado" if nota >= 60 else "Recuperação" if nota >= 30 else "Reprovado"
print(condicao_nota_do_aluno) 

# Indentação e quebra linha em strings com f-string
nome = "Murilo"
idade = 18

user = (
    f"Nome do usuário: {nome}\n"
    f"Idade: {idade}"
)

print(user)

# Indenação com f"""...""""

print(f"""
Nome: {nome}
Idade: {idade}
""")


# try / except

"""
FLUXO

 * Executa o try
 * Se tiver algum erro executa o except
 * Se não tiver erro executa o try e depois o else
 * E independentemente se ouve erro ou não é executado o finally
"""

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError: # Erro quando a divisão por zero
    print("Erro: divisão por zero!")
except ValueError: # Erro quando não recebemos o tipo correto
    print("Erro: entrada inválida!")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Finalizando operação...")