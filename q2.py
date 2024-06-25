A = int(input('Digite um valor: '))
B = int(input('Digite outro valor: '))
C = int(input('Digite outro valor: '))
D = int(input('Digite outro valor: '))

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and (A % 2 == 0):
    print('Valores Aceitos!')
else:
    print('Valores NÃO Aceitos!')
