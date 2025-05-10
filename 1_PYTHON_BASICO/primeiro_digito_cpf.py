
# cpf = "746.824.890-70"
cpf = "777.577.850-49"
cpf_nove_primeiros_digitos = cpf.replace(".", "")[:9]

mult = int()
soma = int()
primeiro_digito = cpf[12]
resultado_do_calculo = int()
indices_negativos = [10,9,8,7,6,5,4,3,2]
lista_numeros = []

try:
    while True:
        
        for indice, digito in enumerate(cpf_nove_primeiros_digitos):
            lista_numeros.append(int(digito) * indices_negativos[indice])
            print(lista_numeros)
          

        if len(lista_numeros) >= len(indices_negativos):
            soma = sum(lista_numeros)
            mult = soma * 10
        
        if mult > 0:
            resultado_do_calculo = mult % 11
            print(resultado_do_calculo)
            
        if resultado_do_calculo == int(primeiro_digito):
            print(f"""
                CPF VÁLIDO!
                O CPF: {cpf} , foi verificado!
            """)
        else:
            print(f"CPF INVÁLIDO!")
        break
except:
    ...