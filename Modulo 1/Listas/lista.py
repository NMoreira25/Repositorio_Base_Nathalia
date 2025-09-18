opcão = 4

while opcão !=3: 
    opcão = int(input(" oq quer fazer \n1converter real para dolar \n2 converter dolar para real "))
    if opcão == 1:
        def converter_real_para_dolar():
            cotação = 5.30
            real = float(input("quanto vc tem em real ?"))
            converter = real * cotação
            print(converter)
        converter_real_para_dolar()
        
        def converter_dolar_para_real():
            cotaçao = 0.18
            dolar = float(input("quantos vc tem em dolar ?"))
            converter = dolar * cotaçao
            print(converter)
        converter_dolar_para_real()   
