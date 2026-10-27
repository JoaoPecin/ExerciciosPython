temp=0
while temp >= -99:
    temp=int(input('Digite a temperatura do lugar: '))
    if temp == -100:
        print('Acabou o teste')
    elif temp <= 0:
        print('Está congelando!')
    elif temp <= 5:
        print('O local está muito frio')
    elif temp <= 15:
        print('O local está frio')
    elif temp <= 30:
        print('A temperatura está agradável.')
    elif temp <= 40:
        print('O local está quente')
    elif temp > 41:
        print('Está muito quente!')
    