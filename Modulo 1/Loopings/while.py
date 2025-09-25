nome_cadastro = input("digite seu nome de cadastro: ")
senha_cadastro = input("digite sua senha de cadastro: ")
opçao = 7
while opçao !=3:  

    nome_digitado = input("digite seu nome digitado: ")
    senha_digitada = input("digite sua senha de cadastro: ")

    if nome_cadastro == nome_digitado and senha_cadastro == senha_digitada:
        print("correto")
    else: 
        print("errado") 
    opçao  = int(input("digite 2 para tentar novamente /n 3 para sair"))
