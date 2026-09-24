salario=float(input('Quanto você ganha mensalmente? '))
tempo=int(input('Quanto tempo de empresa você tem? '))
if salario < 2000 and tempo >= 5:
    print('Elegível a reajuste.')
else:
    print('Não está apto a reajuste')