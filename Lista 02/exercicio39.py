altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))
imc= peso / altura ** 2
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso normal.')
elif imc < 30:
    print('Você está no sobrepeso.')
elif imc >=30:
    print('Você está obesa')

