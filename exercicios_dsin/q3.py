valor = int(input('Digite o valor: R$'))
notas = [200, 100, 50, 20, 10, 5, 2, 1]
contagem = {}
for nota in notas:
    qtd_notas = valor // nota
    contagem[nota] = qtd_notas
    valor %= nota

print(f'Para R${valor:.2f}: '.replace('.', ','))
for nota, qtd in contagem.items():
    print(f'-{qtd} nota(s) de R${nota:.2f}'.replace('.', ','))