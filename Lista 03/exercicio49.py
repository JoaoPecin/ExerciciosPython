numero_maior=0
for num in range(1, 11):
    num=int(input(f'Digite o {num}º número: '))
    if num > numero_maior:
        numero_maior = num
print(f'O maior número é {numero_maior}')
    

    