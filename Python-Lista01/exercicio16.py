nome=input('Qual é o seu nome? ')
salario=(float(input('Quanto é o seu salário? ')))
aumento=(float(input('Quanto será o percentual de aumento? ')))
porcentagem=aumento / 100
desconto=salario * porcentagem
novo_salario=salario + desconto
print('Nome:', nome)
print('Salário antigo:', salario)
print('Salário novo:', novo_salario)
print('Diferença entre salários:', novo_salario - salario)