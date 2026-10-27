ing=0
num=0
while ing <= 50:
    per=input('Você quer um ingresso?(S/N):')
    if per == 'S':
        ing+=1
        pre= ing * 15
        vag= 50 - ing
        print(f'Ainda existem {vag} vagas disponíveis')
        print(f'Você comprou {ing} ingressos, ficou no total de R${pre}')
    else:
        print('Obrigado por comprar conosco!')
        break
    