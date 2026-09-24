minuto=int(input('Digite o minuto usado no telefone: '))
if  minuto <= 100:
    print('Até 100 minutos: R$ 0,25')
elif minuto <= 200:
    print('De 101 a 200 minutos: R$ 0,20')
elif minuto <= 500:
    print('De 201 a 500 minutos: R$ 0,15')
elif minuto > 500:
    print('Acima de 500 minutos: R$ 0,10')