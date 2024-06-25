def imprimir_titulo(text1, text2):
    tamanho_total = max(len(text1), len(text2))
    borda = '|'
    print(borda * (tamanho_total + 6))
    print(borda * 2, (text1.center(tamanho_total)), borda * 2)
    print(borda * 2, (text2.center(tamanho_total)), borda * 2)
    print(borda * (tamanho_total + 6))


texto1 = input("Digite a parte superior do título: ")
texto2 = input("Digite a parte inferior do título: ")
imprimir_titulo(texto1, texto2)
