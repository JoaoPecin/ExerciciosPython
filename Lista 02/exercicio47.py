numero1=int(input('Digite o primeiro número: '))
numero2=int(input('Digite o segundo número: '))
numero3=int(input('Digite o terceiro número: '))
if numero1 > numero2 and numero1 > numero3:
    print('O', numero1,'é o maior número')
elif numero2 > numero1 and numero2 > numero3:
    print('O', numero2,'é o maior número')
elif numero3 > numero1 and numero3 > numero2:
    print('O', numero3,'é o maior número')