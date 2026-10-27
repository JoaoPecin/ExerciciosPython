num=float(input('Digite o valor da compra: '))
soma= 0
total=0
while num != -1:
    soma= soma + num
    print(f'O valor da compra está em {soma}')
    num=float(input('Digite o valor da compra: '))
if soma >= 500:
    print('Você ganhou um desconto de 10%')
    total= soma * .9
elif soma >= 1000:
    print('Você ganhou um desconto de 5%')
    total= soma * .95
print(f'O valor total da sua compra é: {total}')

