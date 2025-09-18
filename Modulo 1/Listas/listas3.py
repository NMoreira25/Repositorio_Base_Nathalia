lista_de_compras = []
opção = 6
while opção !=0:    opção = int(input("digite a opção que quer: \n\n 1- adicionar item \n 2- ver item \n 3- modificar item \n 4- remover item \n 5- apagar tudo"))   
  if opção==1:           novo = input("digite o item que quer inserir: \n")        lista_de_compras.append(novo)        print(f"\n item adicionado!!")   
elif opção ==2:        print(lista_de_compras)     
elif opção ==3:         antigo = input("digite o item que deseja modificar: \n")       
if antigo in lista_de_compras:             novo = input("digite o produto novo: \n")            index = lista_de_compras.index(antigo)           
lista_de_compras[index] = novo            print(f"lista atualizada!1: \n {lista_de_compras} \n")          
else:            print(f"\n item não encontrado \n")   
elif opção ==4:      remover = input ("digite o item que quer remover: \n ")       lista_de_compras.remove(remover)      print(f"\n item removido!!")  
elif opção == 5:        lista_de_compras.clear()        print(f" \nlista excluida !! {lista_de_compras} \n")
0 commit commentsComments0 (0)Lock conversationComment
