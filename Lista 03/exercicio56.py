per=input('Quer jogar ímpar ou par? (S ou N) ')
num1=35
while 'S' == per:
    esc=input('Impar ou Par? ')
    num2=int(input('Digite o número: '))
    print(f'Meu número é {num1}')
    res= num1 + num2
    if res % 2 == 0 and esc == 'Par':
        print('O número é par, parabéns voce ganhou')
    elif res % 2 == 0 and esc == 'Impar':
        print('O número é par, você perdeu')
    elif res % 2 != 0 and esc == 'Impar':
        print('O número é Impar, parabéns voce ganhou')
    elif res % 2 != 0 and esc == 'Par':
        print('O número é Impar, você perdeu ')
    if num2 < 0:
        print('Esse número é impossível de calcular')
    per=input('Quer jogar ímpar ou par? (S ou N)')
if per == 'N':
    print('foi bom jogar com você!')
    
    