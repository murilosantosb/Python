# Formatações simples

# Formatando milhares
numero = 12345678.78
print(f"Número formatado: {numero:,.2f}")

# Formatação de espaços na palavras
nome = "Python"
print(f"{nome:>10}")  # Alinha à direita em 10 espaços
print(f"{nome:<10}")  # Alinha à esquerda
print(f"{nome:^10}")  # Centraliza 

# Aula sobre formatação usando o .format()

nome = "Murilo"
idade = 19
print("Nome: {}, Idade: {}".format(nome, idade)) # Padrão

print("Nome {1}, Idade: {0}".format(idade, nome)) # Utilizando posições

print("Nome: {n}, Idade: {i}".format(n="Murilo",i=18))

# Função Input()

# nome = input("Qual é o seu nome?")
# # Trocando tipos
# idade = int(input("Qual a sua idade?"))
# print(f"Usuário: {nome=} com idade: {idade=}") # O sinal = no final traz em formato de variável: nome="murilo"

#  Condicionais if, elif e else

tem_cateira = True

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
elif idade >= 18 and tem_cateira:
    print("Pode dirigir!")    
else:
    print("Maior de idade")          


# Desafio  

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

primeiro_valor_num = 0
segundo_valor_num = 0

if type(primeiro_valor) and type(segundo_valor) == str:
    primeiro_valor_num = int(primeiro_valor)
    segundo_valor_num = int(segundo_valor)
    
if primeiro_valor_num > segundo_valor_num:
    print(f"{primeiro_valor_num=} é maior do que o {segundo_valor_num=}")
elif segundo_valor_num > primeiro_valor_num:
    print(f"{segundo_valor_num=} é maior do que o {primeiro_valor=}")
else:
    print(f"Os valores {primeiro_valor_num} e {segundo_valor_num} são iguais")        
    
    
# Operadores lógicos    
    
if primeiro_valor_num == 0 or primeiro_valor_num == 10:
    print("Verdadeiro")
else:
    print("Falso")    
    
user_login = False

if not user_login:
    print("Usúario não está logado")
else:
    print("Seja bem-vindo(a)")
    

entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrou!")
else:
    print("Saiu!")