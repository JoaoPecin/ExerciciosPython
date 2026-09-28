soma = 0
while True:
    numero=int(input('Digite um número até acertar: '))
    soma = soma + numero
    if numero == 0:
        print(f'O resultado das somas foi: {soma}')
        break


