temp=int(input('Digite a temperatura: '))
umi=int(input('Digite a umidade do ar: '))
if temp > 30:
    if umi<30:
        print('Cuidado! O risco de incêndio é alto!')
    else:
        print('O risco de incêndio é baixo!')    
else:
    print('Está tudo bem!')                