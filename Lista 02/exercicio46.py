nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
frequencia=int(input('Digite sua frequência escolar: '))
media = nota1 + nota2 / 2
if frequencia >= 75 and media >= 6:
    print('Aprovado')
elif frequencia < 75:
    print('Reprovado por falta')
elif media < 6:
    print('Reprovado por nota')

