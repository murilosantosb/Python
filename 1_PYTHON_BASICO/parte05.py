# Loop For, In e range

frutas = ["Banana", "Maçã", "Uva"]
palavra = "Python"

# for fruta in frutas:
#     print(fruta, end="!\n")

# for letra in palavra:
#     print(letra)

# for numero in range(5):
#     print(numero)

# nomes = ["Murilo", "Lucas", "Ana"]

# for indice, nome in enumerate(nomes):
#     print(f"Indice: {indice} - Nome: {nome}")

# for i in range(5):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10):
#     if i == 2:
#         print("O iterador atual é 2 então pulamos!")
#         continue
#     if i == 8:
#         print("Operação encerrada!")
#         break
        
#     for j in range(1, 5):
#         print(f"Iterador: {i} - {j}")
# else:
#     print("Operação não encontrou um break!")


# Desafio Aula 76 - Jogo da palavra secreta

PALAVRA_SECRETA = "Jesus"
palavra_secreta_sem_espacos = PALAVRA_SECRETA.replace(" ", "").lower()
tentativas = 0
palavra_escondida = palavra_secreta_sem_espacos.replace(palavra_secreta_sem_espacos, "*" * len(palavra_secreta_sem_espacos))


try:
    lista_palavra = list(palavra_escondida)
    palavra = "".join(lista_palavra)
    while True:
    
        if palavra != palavra_secreta_sem_espacos:
            tentativa_do_usuario = input("Digite uma letra: ")
            
            if len(tentativa_do_usuario) > 1:
                print("Não é permitido digita mais de um digito por vez!")
                continue
            
            acertou = False
            
            for indice, letra in enumerate(palavra_secreta_sem_espacos):
               
               if letra == tentativa_do_usuario:    
                   lista_palavra.pop(indice)
                   lista_palavra.insert(indice, letra)
                   
                   palavra = "".join(lista_palavra)
                   print(palavra)
                   acertou = True
                
            
            if acertou == False:
                print(f"Essa letra não está presente na palavra, {palavra} ")
            
            elif palavra == palavra_secreta_sem_espacos:
                print(f"""
                      Meus parabéns, você acertou a palavra!
                      Palavra secreta: {PALAVRA_SECRETA}
                      Número de tentativas: {tentativas}
                """)
                break
            
            tentativas += 1
except:
    print("Erro do sistema!")
finally:
    print("Jogo finalizado!")