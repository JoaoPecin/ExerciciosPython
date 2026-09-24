numero=int(input('Digite um número que corresponde a um mês do ano: '))
if numero <= 2:
    print('É verão.')
elif numero <= 5:
    print('É outono.')
elif numero <= 8:
    print('É inverno.')
elif numero <= 11:
    print('É primavera.')
elif numero == 12:
    print('É verão.')