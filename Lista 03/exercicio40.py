num= 1
cont_pos= 0
cont_neg=0
while num != 0:
    num=int(input('Digite um número: '))
    if num > 0:
        print('O número é positivo')
        cont_pos+=1
    elif num < 0:
        print('O número é negativo')
        cont_neg+=1
    else:
        print(f'Tiveram {cont_pos} números positivos e {cont_neg} numeros negativos')
