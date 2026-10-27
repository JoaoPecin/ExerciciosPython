uni= 100
cont=0
valor=int(input('Digite quantas unidades deseja: '))
while uni > 0:
    uni= uni - valor
    print(f'restam {uni} unidades')
    valor=int(input('Digite quantas unidades deseja: '))
    if uni <= 0:
            print('Não há como pedir mais, acabou o estoque')
            break
    if uni > 50:
        print('O estoque ainda ta cheio')
    elif uni>=20:
        print('O estoque está acabando')
    




    
   


            