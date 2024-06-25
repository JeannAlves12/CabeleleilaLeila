def criar_matriz_caracol(N):
    matriz = [[0] * N for _ in range(N)]
    limite_superior = 0
    limite_inferior = N - 1
    limite_esquerdo = 0
    limite_direito = N - 1
    valor = N
    incremento = N

    while limite_superior <= limite_inferior and limite_esquerdo <= limite_direito:
        for coluna in range(limite_esquerdo, limite_direito + 1):
            matriz[limite_superior][coluna] = valor
            valor += incremento
        limite_superior += 1
        for linha in range(limite_superior, limite_inferior + 1):
            matriz[linha][limite_direito] = valor
            valor += incremento
        limite_direito -= 1
        for coluna in range(limite_direito, limite_esquerdo - 1, -1):
            matriz[limite_inferior][coluna] = valor
            valor += incremento
        limite_inferior -= 1
        for linha in range(limite_inferior, limite_superior - 1, -1):
            matriz[linha][limite_esquerdo] = valor
            valor += incremento
        limite_esquerdo += 1
        incremento *= -1
        if incremento < 0:
            incremento -= 5
        else:
            incremento += 5

    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end="\t")
        print()


N = 5

matriz_caracol = criar_matriz_caracol(N)
imprimir_matriz(matriz_caracol)
