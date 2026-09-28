numero=int(input('Digite um número: '))
dig = 0

while numero != 0:
    numero //= 10
    dig = dig + 1
    
    print(f'Esse número tem {dig} digitos')

