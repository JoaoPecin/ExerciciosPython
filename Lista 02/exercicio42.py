nota=float(input('Digite a sua nota final: '))
falta=int(input('Digite o seu número de faltas: '))
if falta > 15:
    print('Reprovado por falta.')
elif nota >= 9:
    print('Você foi um aluno nota A')
elif nota >= 7:
    print('Você foi um aluno nota B')
elif nota >= 5:
    print('Você foi um aluno nota C')
elif nota < 5:
    print('Você fpo um aluno nota D')