def validar_placa(placa):
    if len(placa) != 7:
        return False

    if not placa[:3].isalpha() or not placa[:3].isupper():
        return False

    if not placa[3].isdigit() or not placa[5].isdigit():
        return False

    if not placa[6].isdigit():
        return False

    return True


def converter_placa(placa):
    list_placa = []
    merc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for n in placa:
        list_placa.append(n)
    # BR -> MERC
    if placa[4].isdigit():
        num = int(placa[4])
        return placa[:4] + merc[num] + placa[5:]
    # MERC -> BR
    if placa[4].isalpha():
        letra = str(placa[4])
        if letra in merc:
            print('Correspondente: ', end='')
            print(placa[:4], end='')
            print(merc.index(letra), end='')
            print(placa[5:])


placa = input('Digite a placa: ')
if validar_placa(placa):
    padrao = 'Brasil' if placa[4].isdigit() else 'Mercosul'
    print('Padrão:', padrao)
    converter_placa(placa)
else:
    print('Formato inválido')
