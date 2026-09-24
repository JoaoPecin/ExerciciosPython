idade=int(input('Digite a sua idade: '))
sexo=input('Digite o seu gênero(M ou F): ')
if sexo == 'M' and idade >= 18:
    print('Você está apto ao serviço militar.')
else:
    print('Você não pode se alistar.')
