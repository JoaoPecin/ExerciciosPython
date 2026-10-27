soma= 0
cont= 0
while True:
    num=float(input('Valor do depósito: '))
    if num == 0:
        print(f'O valor total do valor do deposito foi {soma}')
    soma = soma + num
    cont+=1