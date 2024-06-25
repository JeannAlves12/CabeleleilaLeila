a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a == 0 and b == 0 and c != 1:
    print('solução impossível')
else:
    x = (1 - c) / (a + b)
    print(f'O valor de X é: {x}')
