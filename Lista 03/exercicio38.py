num= 0
num_corr= 45
while num != num_corr:
    num=int(input('Digite o número secreto: '))
    if num <= 20:
        print('Está muito longe')
    elif num <=40:
        print('Está chegando perto')
    elif num <=44:
        print('Está muito perto')
    elif num == 45:
        print('Você acertou!!!')
    elif num >= 46:
        print('Passou do numero')