id = 0
cont1=0
cont2=0
cont3=0
cont4=0
while id >= 0:
    id=int(input('Qual a sua idade? '))
    if id < 12:
        cont1= cont1 + 1
        print(f'Existem {cont1} crianças')
    elif id < 18:
        cont2= cont2 + 1
        print(f'Existem {cont2} adolescentes')
    elif id < 60:
        cont3= cont3 + 1
        print(f'Existem {cont3} adultos')
    elif id >= 60:
        cont4= cont4 + 1
        print(f'Existem {cont4} idosos')
    