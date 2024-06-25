horas_dia = float(input('Digite a quantidade de horas trabalhadas por dia: '))
preco_hr = float(input('Digite o preço da hora de trabalho: '))
dias_trabalho = int(input('Digite a quantidade de dias trabalhados no mês: '))

salario_bruto = horas_dia * preco_hr * dias_trabalho

desconto = salario_bruto * 0.03

salario_liq = salario_bruto - desconto

print(f'O salário líquido é: R${salario_liq:.2f}'.replace('.', ','))

'''
# Sei fazer também criando uma função:
def calc_sal_liq(horas_dia, preco_hr, dias_trabalho):
    salario_bruto = horas_dia * preco_hr * dias_trabalho
    desconto = salario_bruto * 0.03
    salario_liq = salario_bruto - desconto
    return salario_liq


horas_dia = float(input('Digite a quantidade de horas trabalhadas por dia: '))
preco_hr = float(input('Digite o preço da hora de trabalho: '))
dias_trabalho = int(input('Digite a quantidade de dias trabalhados no mês: '))

salario = calc_sal_liq(horas_dia, preco_hr, dias_trabalho)

print(f'O salário líquido é: R${salario:.2f}'.replace('.', ','))
'''