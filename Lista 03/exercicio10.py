num=int(input('Digite um número: '))
contador = 1
while 0 <= num:
    print('Tente novamente.')
    contador = contador + 1     
    num = int(input('Digite outro número: '))

print(f'foram {contador} tentativas até o acerto')