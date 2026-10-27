soma= 0
media  = 0
cont = 0
while True:
    nota=int(input('Digite a nota do aluno: '))
    if nota == -1:
        media = soma/cont
        print(f'A media inteira da sala é {media}')
        break
    soma = soma + nota
    cont = cont + 1

