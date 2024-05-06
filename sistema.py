from Leila.lib.arquivo import *
from time import sleep

arq = 'clientes.txt'
arq2 = 'usuario.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

if not arquivoexiste(arq2):
    criararquivo(arq2)

senha = 1234

while True:
    usuario = menu(['Cliente', 'Usuario', 'Sair do Sistema'])
    if usuario == 1:
        while True:
            resposta = menu2(['Agendamento de serviço', 'Alteração de serviço ou de data', 'Sair do Sistema'])
            if resposta == 1:
                cadastro_cliente()
            elif resposta == 2:
                alterar_agendamento_cliente(arq2)
            elif resposta == 3:
                cabecalho('Saindo do Sistema... Até Logo!')
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
    elif usuario == 2:
        validar = int(input('Digite a senha: '))
        if senha == validar:
            cabecalho('SEJA BEM VINDO COLABORADOR')
            while True:
                funcoes = menu2(['Agendar Cliente', 'Agendamentos Feitos', 'Alterar Agendamentos',
                                 'Aprovação de Agendamentos', 'Desempenho Semanal', 'Sair do Sistema'])
                if funcoes == 1:
                    cadastro_cliente()
                elif funcoes == 2:
                    agendamentos_futuros(arq2)
                elif funcoes == 3:
                    cabecalho('Alterar Agendamentos')
                    alterar_agendamento_usuario(arq)
                elif funcoes == 4:
                    aprovar_agendamento_user(arq)
                elif funcoes == 5:
                    desempenho_semanal_menu()
                elif funcoes == 6:
                    cabecalho('Saindo do Sistema... Até Logo!')
                    break
                else:
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
        else:
            print('\033[31mSENHA INCORRETA! Tente novamente:\033[m')
    elif usuario == 3:
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
