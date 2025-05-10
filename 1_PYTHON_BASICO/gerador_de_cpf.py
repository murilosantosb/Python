import random

cpf = "".join([str(random.randint(0, 9)) for _ in range(9)])

digitos_cpf = []

indice_inverso = [11,10,9,8,7,6,5,4,3,2]

for i in range(2):
    lista_numeros = []
    
    for indice, digito in enumerate(cpf):
        lista_numeros.append(int(digito) * indice_inverso[indice + (1 - i)])
        
    resultado = (sum(lista_numeros) * 10) % 11
    digito_valido = 0 if resultado > 9 else resultado
    
    digitos_cpf.append(digito_valido)
    cpf += str(digito_valido)
    
print(f"CPF Válido: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")