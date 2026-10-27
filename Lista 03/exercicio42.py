depositar=0
sacar= 0
while True:
    opcao=int(input('Digite 1 para depositar, 2 para sacar e 3 para sair: '))
    if opcao == 1:
       depositar=float(input('Digite o valor do depósito: '))
       print(f'O valor do depósito foi {depositar}')
    elif opcao == 2:
        sacar=float(input('Digite o valor do saque: '))
        restante= depositar - sacar
        print(f'Você tirou {sacar} Reais, ainda resta {restante}')
    elif opcao ==3:
        print('Obrigado por usar nosso programa!')
        break
