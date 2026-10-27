for num in range(1,31):
    if num % 5 == 0 and num % 3 ==0:
            print(f'O número {num} é multiplo dos dois')
    elif num % 3 == 0:
        print(f'O número {num} é multiplo de 3')
    elif num % 5 == 0:
        print(f'O número {num} é múltiplo de 5')
    elif num % 3 != 0 and num % 5 != 0:
        print(f'O número {num} não é multiplo de nenhum dos dois. ')