num_corr=12439
cont=3
print('Você tem 3 tentativas para acertar a senha')
num=int(input('Digite a senha correta: '))
while num != num_corr:
    cont-=1
    print(f'Você errou, restam {cont} tentativas')
    num=int(input('Digite a senha correta: '))
    if cont == 1:
        print('Você excedeu o limite de tentativas.')
        break
if num == num_corr:
    print('Você acertou a senha!')