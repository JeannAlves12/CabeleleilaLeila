def perfeito(num):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    return soma_divisores == num


def raiz(num):
    return num == int(num ** 0.5) ** 2


def verificar(N):
    for i in range(1, N + 1):
        if perfeito(i):
            print(i, 'é um número perfeito')
        if i % 3 == 0:
            print(i, 'é múltiplo de 3')
        if i % 5 == 0:
            print(i, 'é múltiplo de 5')
        if raiz(i):
            print(i, 'tem raiz quadrada inteira')


N = int(input('Digite um número inteiro positivo: '))
verificar(N)
