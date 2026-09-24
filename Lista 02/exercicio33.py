compra=float(input('Digite o valor da compra solicitada: '))
dividir= 10/100
desconto= compra * dividir
definicao= compra - desconto
if compra > 100:
    print('Terá desconto de 10% do valor, ficando R$', definicao)
else:
    print('A compra não terá desconto. Logo o preço permanecerá', compra)