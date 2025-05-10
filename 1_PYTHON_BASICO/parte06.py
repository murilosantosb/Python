# # Listas

# lista = ["Banana", "Maçã", "Melão"]
# numeros = [2,5,8,1,10,22,4,3,7]

# lista3 = lista + numeros

# # Adicionar
# lista.append("Melancia")
# lista.insert(2, "Uva")

# # Deletar
# lista.remove("Maçã")
# # lista.pop(1)

# # Alterar items
# lista3[0] = "Morango"

# if "Uva" in lista:
#     print("Uva está na lista!")
    

# a = [1,2,3]
# b = a.copy() # Dessa maneira a lista A não recebe nada do B
# b.append(4)
# print(a)


# print(lista)
# print(lista3)
# print(sorted(numeros))


# lista = ["Maria", "Helena", "Luiz"]

# # for indice, nome in enumerate(lista):
# #     print(f"{indice} {nome}")

# # Empacotamento, Desempacotamento e Tuplas
    
#  # Desempacotamento: 

# a,b,c = lista
# print(f"A: {a} - B: {b} - C: {c}")

#  # Empacotamento - criar um tupla
# nomes = ("Murilo", "Luiza", "Mirella")
# # nomes[0] = "Eduardo" Tuplas são Imutáveis, não podem ser alteradas

# lista[0] = "Luiza"
# print(lista)
  
  
  
# Desafio Aula 90 - Lista de Compras

import os

lista_usuario = []
item = ""

try:
    while True:
        resposta_do_user = input(f"Selecione uma opção \n [i]nserir [a]pagar [l]istar [s]air:").lower()
        
        if resposta_do_user not in "ials":
            print("Letra digita inválida!")
            continue
        
        if resposta_do_user == "l" and len(lista_usuario) < 1:
            print("Nada a listar!")
        else:
            os.system("cls")
            for indice, nome_produto in enumerate(lista_usuario):
                print(f"{indice} {nome_produto}")
        
        if resposta_do_user == "a" and len(lista_usuario) < 1:
            print("Sua lista de compras está vazia!")
            continue
        
        if resposta_do_user == "a":
            apagar_item_pelo_indice = int(input("Digite o Índice do produto: "))
            
            if 0 <= apagar_item_pelo_indice < len(lista_usuario):
                lista_usuario.pop(apagar_item_pelo_indice)
            else:
                print("Não foi possível excluir esse índice!")
                continue
        
        if resposta_do_user == "i":
            os.system("cls")
            inserir_na_lista = input("Valor: ")
            item = inserir_na_lista if len(inserir_na_lista) > 1 else ""
            
            if item == "":
                print("Você não digitou nada!")
                continue
            elif len(item) > 1 and item.isalpha():
                os.system("cls")
                print(f"Valor: {item}") 
                lista_usuario.append(item)
                item = ""
                
        if resposta_do_user == "s":
            os.system("cls")
            print(f"Sua lista: {lista_usuario}")
            break

except ValueError:
    print("Digite apenas números!")   
except:
    print("Erro do sistema, tente novamente!")
    
    