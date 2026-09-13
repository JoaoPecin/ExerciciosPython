horas=int(input('Quantas horas você trabalha no Mês? '))
dinheiro=float(input('Quanto você ganha por hora? '))
dia=int(input('Quantos dias você trabalha? '))
salario_mes= horas * dinheiro
dia_trabalho= salario_mes / dia
print('Você ganha', salario_mes,'por mês')
print('Você ganha', dia_trabalho,'por dia')
