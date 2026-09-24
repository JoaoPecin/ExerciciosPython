compra=float(input('Digite o valor da compra: '))
dividir1= 5/100
dividir2= 10/100
dividir3= 15/100
porcentagem1= compra * dividir1
porcentagem2= compra * dividir2
porcentagem3= compra * dividir3
desconto1= compra - porcentagem1
desconto2= compra - porcentagem2
desconto3= compra - porcentagem3
if compra <= 50:
    print('Esse valor não terá desconto.')
elif compra <= 200:
    print('Esse valor terá 5% de desconto, ficando', desconto1)
elif compra <= 500:
    print('Esse valor terá 10% de desconto, ficando', desconto2)
elif compra > 500:
    print('Esse valor terá 15% de desconto, ficando', desconto3)