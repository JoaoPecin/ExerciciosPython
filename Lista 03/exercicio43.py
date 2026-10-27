for num in range(1,11):
    num=int(input('Digite a nota de 10 alunos:'))
    if num >=9:
        print('Você tirou nota A')
    elif num >=7:
        print('Você tirou nota B')
    elif num >=5:
        print('Você tirou nota C')
    elif num < 5:
        print('Você tirou nota D')
print('Acabou os alunos.')