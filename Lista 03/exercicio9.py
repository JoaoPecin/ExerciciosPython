numero=int(input('Digite um número: '))
fatorial= 1
cont = 1

while cont <= numero:
    fatorial = fatorial * cont
    cont = cont + 1

print(f'O número escolhido é {numero}, e o fatorial dele é {fatorial}')