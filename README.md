# CabeleleilaLeila
Sistema criado para teste de Dev DSIN
# Interface:
-> def leiaint(txt):
Essa função pede para o usuário digitar um número inteiro. Se o usuário digitar algo que não seja um número inteiro, ela
mostrará uma mensagem de erro e pedirá novamente para o usuário digitar. Se o usuário decidir não digitar nada e
pressionar Ctrl+C, a função mostrará uma mensagem informando que o usuário desistiu. Quando o usuário finalmente
digitar um número inteiro válido, a função retornará esse número.

-> deflinha(tam)
Mostra uma linha de tamanho fornecido no paramtro.

-> def cabecalho(txt)
Centraliza um texto informado no parametro e coloca linhas na parte superior e inferior.

-> def menu(lista)/def menu2(lista)/def menu3(lista)
Esta função exibe um menu de opções para o usuário. Ele mostra uma lista(informada no paremetro) de itens numerados e
solicita ao usuário que escolha uma opção. Depois que o usuário faz a seleção, a função retorna a opção escolhida.


# Arquivo
-> Primeiro importa as funcoes de interface e a biblioteca datetime usada para tratar as datas do sistema

-> def arquivoexiste(nome):
Verifica se o arquivo informado no parametro existe ou nao.

-> def criararquivo(nome):
Cria um arquivo para o salvamento de dados do sistema, do tipo wr+, permitindo escrita e leitura do mesmo.

-> def verificar_e_juntar_agendamentos(nome, telefone, servico, data, arquivo):
A função verifica se há agendamentos existentes para um cliente na mesma semana do novo agendamento. Se encontrar um
agendamento na mesma semana, combina o novo serviço com o serviço existente e retorna os dados do agendamento combinado
em uma string formatada. Se não encontrar agendamentos na mesma semana, retorna None.

-> def cadastrar(arq, nome='desconhecido', telefone=0, servico='Corte', data='05/05/24'):
Esta função adiciona um novo agendamento ao arquivo especificado. Ela primeiro tenta abrir o arquivo e se bem-sucedida,
ela verifica se há agendamentos na mesma semana para o cliente fornecido. Se houver, oferece a opção de combinar os
agendamentos. Se sim, os agendamentos são atualizados no arquivo. Caso contrário, o novo agendamento é simplesmente
adicionado. Se não houver agendamentos na mesma semana, o novo agendamento é adicionado diretamente.

-> def informacoes(escolha=0):
Esta função captura as informações básicas de um cliente para agendamento de serviço. Ela exibe um cabeçalho
e solicita ao usuário o nome, telefone, data e escolha do serviço. Em seguida, ela valida a data fornecida, garantindo
que seja no futuro. Por fim, chama a função cadastrar para inserir as informações do cliente no arquivo.

-> def cadastro_cliente():
Esta função apresenta ao usuário um menu de opções de serviços e permite que ele escolha um deles. Com base na escolha
do usuário, a função chama a função informacoes para capturar as informações do cliente relacionadas ao serviço
selecionado. Caso a opção digitada não seja válida, é exibida uma mensagem de erro.

-> def alterar_agendamento_cliente(arq):
Esta função permite ao usuário alterar o serviço ou a data de um agendamento existente. Primeiro, mostra os agendamentos
existentes, solicita o nome do cliente e confirma o número de telefone associado ao agendamento. Em seguida, oferece
opções para alterar o serviço, a data ou ambos. Após a confirmação das alterações pelo usuário, atualiza o arquivo de
agendamentos com as modificações realizadas.

-> def aprovar_agendamento(nome_arquivo):
A função aprovar_agendamento permite ao usuário aprovar agendamentos pendentes. Ela lê o arquivo de agendamentos,
verifica se algum agendamento ainda não foi aprovado e, em caso afirmativo, oferece a opção de aprovação.
Se um agendamento for aprovado, ele é removido do arquivo de agendamentos e adicionado ao arquivo de usuários.

-> def lerarquivo(nome):
A função é responsável por ler o conteúdo de um arquivo e exibir os dados formatados na tela. Ela abre o arquivo em modo
 de texto e itera sobre cada linha. Verifica se há dados suficientes e, se houver, extrai o nome, o serviço e a data. Em
seguida, exibe todos os dados em uma tabela formatada. Se houver dados incompletos em uma linha, uma notificação é
exibida. Se o arquivo não puder ser encontrado, uma mensagem de erro é mostrada.

-> def alterar_agendamento_usuario(arq):
A função permite ao usuário alterar o serviço ou a data de um agendamento existente. Ela começa mostrando os
agendamentos existentes, solicita o nome e lê o arquivo especificado, armazenando os dados em uma lista. Em seguida,
tenta achar o cliente na lista, permitindo ao usuário inserir um novo serviço e uma nova data válida. Se as alterações
forem feitas com sucesso, o arquivo é atualizado. Uma mensagem é exibida, se o cliente não for encontrado.

-> def aprovar_agendamento_user(nome_arquivo):
A função permite aprovar agendamentos pendentes. Ela começa lendo o arquivo de agendamentos a serem aprovados e verifica
se cada agendamento já foi aprovado anteriormente. Se um agendamento ainda não foi aprovado, exibe os detalhes desse
agendamento e solicita ao usuário que decida se deseja aprová-lo ou não. Se aprovado, remove o agendamento anterior
(se existir) dos arquivos de usuários, adiciona o novo agendamento aprovado ao arquivo de usuários e exibe uma mensagem
de confirmação. Se não for aprovado, o processo é interrompido.

-> def agendamentos_futuros(arquivo):
A função lê o arquivo de agendamentos especificado e exibe os agendamentos que estão marcados para datas futuras. Ela
exibe um cabeçalho para identificar a ação e percorre cada linha do arquivo. Para cada linha, verifica se há dados
suficientes, compara a data do agendamento com a data atual. Se a data do agendamento for posterior à data atual, os
detalhes do agendamento são exibidos. Se o arquivo não for encontrado, uma mensagem é exibida.

-> def desempenho_semanal_menu():
A função exibe um menu para escolher entre visualizar os agendamentos passados ou futuros, chama a função correspondente
com base na escolha do usuário. Exibe o menu, obtém a escolha do usuário e, dependendo da escolha, chama a função
'desempenho_semanal_passado' ou 'desempenho_semanal_futuro'. Se o usuário fornecer uma opção inválida, uma mensagem de
erro será exibida.

-> def desempenho_semanal_passado():
A função exibe o desempenho semanal dos agendamentos passados. Ele abre o arquivo de dados, lê os agendamentos, e para
cada agendamento passado, determina a semana em que ocorreu e armazena as informações dos agendamentos semanais em uma
lista. Exibe as informações semanais, incluindo o número de clientes agendados e seus detalhes. Se o arquivo não for
encontrado, exibe uma mensagem de erro.

-> def desempenho_semanal_futuro():
A função exibe o desempenho semanal dos agendamentos futuros. Ele abre o arquivo de dados, lê os agendamentos, e para
cada agendamento futuro, determina a semana em que ocorrerá e armazena as informações dos agendamentos semanais em uma
lista. Exibe as informações semanais, incluindo o número de clientes agendados e seus detalhes. Se o arquivo não for
encontrado, exibe uma mensagem de erro.


#Sistema:
Importa as funções de arquivo e de time. Cria, se ja não existente, os qruivos de armazenamento, que neste sistema eu
usei como banco de dados, define tambem uma senha para quando for um usuario(funcionario) do salão de beleza utilizar a
senha para poder continuar. No sistema, define em uma lista as opções de usuario, se selecionado usuario 1(cliente),
tera uma sequencia de opções de ações para serem feitas, onde estão sendo chamada as funções de arquivo para serem
executadas da forma certa, se algo der errado mensagens de erro aparecerão. O mesmo serve  para se for um
usuario(funcionario). Sistema é fechado se opção sair do sistema for selecionada.


# coisas que eu adicionaria no sistema com mais tempo: função para adiconar e/ou modificar os tipos de serviços
oferecidos no salão. Adicionar as horas do atendimento, para melhor controle do dia.
