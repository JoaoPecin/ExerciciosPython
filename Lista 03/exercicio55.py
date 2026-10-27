cont=0
for dia in range(1,8):
    temp=int(input(f'Digite qual o {dia}º foi a temperatura do dia: '))
    if temp > 30:
        cont+=1
print(f'Teve {cont} dias quentes')