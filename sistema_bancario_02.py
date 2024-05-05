# mensagem de boas vindas
apresentacao = ' SISTEMA BANCÁRIO '
print()
print(apresentacao.center(60, '*'))
print()

# função para ("menu de opções" = DEPOSITO)
def depositar(conta_do_cliente):
    '''
    Depositar na conta do cliente (previamente cadastrado) valores de deposito no "saldo" e "extrato"

    :parâmetro "conta_do_cliente": (variável global) = uma [lista] composta por {dicionários} com informações de contas individuais de cada cliente
    '''
    # variaves locais para operação
    deposito = 0
    chaves = False
    # testa se número da agencia digitado pelo usuário existe (só existe agencia 0001)
    agencia = teste_agencia('Agencia: ') # função auxiliar "teste_agencia"
    # testa se número da conta digitado pelo usuário existe
    conta = teste_int('Conta: ') # função auxiliar "teste_int"
    

    # filtra na lista "conta_do_cliente" (agencia e conta) chave = True se existir
    for c in conta_do_cliente:
        if agencia == c['agencia'] and conta == c['numero_da_conta_cliente']:
            conta_do_cliente_temporario = c # auxilia temporariamente alterações de valores na "conta_do_cliente" (aponta na posição da memória)
            chaves = True
        else:
            # caso "conta_do_cliente" não exista (chave = False) e função depositar é encerrada
            continue
    
    # se "conta_do_cliente" existe (chave = True)
    if chaves:
        try:
            print()
            # entrada de parâmetro do usuário
            deposito = float(input('Digite o valor de deposito: '))

            # tomada de decisão (regra de negócio)
            if deposito <= 0:
                print('Deposito NÃO realizado, deposito menor ou igual a R$:0.00.')
                return 
            else:
                conta_do_cliente_temporario['saldo'] += deposito # armazena "deposito" no saldo = "conta_do_cliente"
                conta_do_cliente_temporario['extrato'] += [str(f'Deposito = R$:{deposito:.2f}')] # armazena informação no extrato
                print('Deposito realizado com sucesso!!!')              
                return 
                
        # mensagem de "erro" para valores não validos digitado pelo usuário e encerrada função
        except Exception as erro:
            print(f'\nErro de operação => ({erro})')
            print('Verifique o valor digitado!!!')
            return
    else:
        # mensagem para usuário caso "conta_do_cliente" NÃO existe e encerrada função
        print(f'\nNão existe conta ou agencia solicitada...')
        return 

# função para ("menu de opções" = SAQUE)
def sacar(conta_do_cliente):
    '''
    Sacar na conta do cliente (previamente cadastrado) valores de saque no "saldo" e "extrato"

    :parâmetro "conta_do_cliente": (variável global) = uma [lista] composta por {dicionários} com informações de contas individuais de cada cliente
    '''
    # variaves locais para operação
    saque = 0
    LIMITE_DE_SAQUE = 500
    chaves = False
     # testa se número da agencia digitado pelo usuário existe (só existe agencia 0001)
    agencia = teste_agencia('Agencia: ') # função auxiliar "teste_agencia"
    # testa se número da conta digitado pelo usuário existe
    conta = teste_int('Conta: ') # função auxiliar "teste_int"

    # filtra na lista "conta_do_cliente" (agencia e conta) chave = True se existir
    for c in conta_do_cliente:
        if agencia == c['agencia'] and conta == c['numero_da_conta_cliente']:
            conta_do_cliente_temporario = c # auxilia temporariamente alterações de valores na "conta_do_cliente" (aponta na posição da memória)
            chaves = True
        else:
            # caso "conta_do_cliente" não exista (chave = False) e função depositar é encerrada
            continue
    
    # se "conta_do_cliente" existe (chave = True)
    if chaves:
        try:
            print()
            # entrada de parâmetro do usuário
            saque = float(input('Digite o valor de saque: '))

            # tomada de decisão (regra de negócio) para usuário
            if conta_do_cliente_temporario['limite_de_saque_diario'] >= 3:
                print('Saque NÃO realizar, já foi atingido limite diário de (3 saques diário).\n')
                return 
            elif saque > LIMITE_DE_SAQUE:
                print('Saque NÃO realizar seu limite para saque é de R$:500,00.\n')
                return 
            elif saque > conta_do_cliente_temporario['saldo']:
                print('Saque NÃO realizar, saldo insuficiente.\n')
                return 
            elif saque <= 0:
                print('Saque NÃO realizar, saque menor ou igual a R$:0.00.\n')
                return 
            else:
                conta_do_cliente_temporario['limite_de_saque_diario'] += 1 # (contador) limitador de saque 3x por cliente
                conta_do_cliente_temporario['saldo'] -= saque # armazena "saque" no saldo = "conta_do_cliente"
                conta_do_cliente_temporario['extrato'] += [str(f'  Sacado = R$:{saque:.2f}')] # armazena informação no extrato
                print('Saque realizado com sucesso!!!')              
                return 

        # mensagem de "erro" para valores não validos digitado pelo usuário e encerrada função
        except Exception as erro:
            print(f'\nErro de operação => ({erro})')
            print('Verifique o valor digitado!!!')
            return
    else:
        # mensagem para usuário caso "conta_do_cliente" NÃO existe e encerrada função
        print(f'\nNão existe conta ou agencia solicitada...')
        return 
    
# função para ("menu de opções" = EXTRATO)
def extrato_bancario(conta_do_cliente):
    '''
    Exibe como texto todas as atividades de "saque" e "deposito" realizado pelo usuário na conta do cliente (previamente cadastrado)

    :parâmetro "conta_do_cliente": (variável global) = uma [lista] composta por {dicionários} com informações de contas individuais de cada cliente
    '''
    # variaves locais para operação
    conta_do_cliente_temporario = 0
    chave = False
     # testa se número da agencia digitado pelo usuário existe (só existe agencia 0001)
    agencia = teste_agencia('Agencia: ') # função auxiliar "teste_agencia"

    # se agencia não existir finalizar função
    if not agencia:
        print('Agencia não existe!')
        return

    # testa se número da conta digitado pelo usuário existe
    conta = teste_int('Conta: ') # função auxiliar "teste_int"

    # filtra na lista "conta_do_cliente" (agencia e conta) chave = True se existir
    for c in conta_do_cliente:
        if agencia == c['agencia'] and conta == c['numero_da_conta_cliente']:
            conta_do_cliente_temporario = c # auxilia temporariamente alterações de valores na "conta_do_cliente" (aponta na posição da memória)
            chave = True
        else:
            # caso "conta_do_cliente" não exista (chave = False) e função depositar é encerrada
            continue
    
    # se "conta_do_cliente" existe (chave = True)
    if chave:
        print()
        print(' Extrato bancário '.center(25, '#'))
        print(f"CPF: {conta_do_cliente_temporario['cliente']['cpf']}") # exibe CPF "conta_do_cliente"
        print('-' * 25)
        if conta_do_cliente_temporario['extrato'] == []:
            print('Saldo total R$:0.00') #
        else:
            for i in conta_do_cliente_temporario['extrato']:
                print(i) # exibe todas as operações de "saque" e "deposito" armazenada no extrato "conta_do_cliente"
            print('-' * 25)
            print(f"Saldo total R$:{conta_do_cliente_temporario['saldo']}")  # exibe saldo "conta_do_cliente"      
    else:
        # mensagem para usuário caso "conta_do_cliente" NÃO existe e encerrada função
        print(f'\nNão existe conta ou agencia solicitada...')
        return       

# função para ("menu de opções" = CADASTRO CLIENTE)
def cadastro_cliente(clientes):
    '''
    Esta função realiza cadastro de dados pessoais de clientes em forma de dicionário, exemplo abaixo:
    dict(cpf = cpf, nome = nome, data_nascimento = data_nascimento, endereco = endereco)
    OBS: não será permitido cadastro de dois CPF iguais por meio de (regra de negocio)
    
    :parâmetro "clientes": (variável global) = uma [lista] para armazenamento de informações dos clientes
    '''

    #  testa se usuário digitou somente números (função "teste_int") e armazena em cpf
    cpf = teste_int('Informe o CPF (somente número): ')

    # se cpf for diferente de 11 dígitos (finaliza função com mensagem para o usuário)
    if len(str(cpf)) != 11:
        return print('CPF digitado não esta com 11 dígitos')

    # teste se CPF do cliente já possui cadastro
    cpf_existe = filtro_cpf(clientes, cpf) # função auxiliar "filtro_cpf"

    # se filtro cpf_existe retorna "True" (finaliza função com mensagem para o usuário)
    if cpf_existe:
        return print(f'Já existe usuário com esse CPF de número{cpf}')
    
    # continuação do cadastro (variaves locais para operação)
    nome = input('Informe o nome completo:')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa):')
    endereco = endereco_cliente() # função auxiliar para cadastrar endereço "endereco_cliente"

    # armazena dados dos clientes cadastrado na lista "clientes"
    clientes.append(dict(cpf = cpf, nome = nome, data_nascimento = data_nascimento, endereco = endereco))
    return print('Cadastro de cliente realizado com sucesso!!!')

# função para ("menu de opções" = ABRIR CONTA)
def abrir_conta(clientes, numero_da_conta_cliente, conta_do_cliente):
    '''
    Esta função realiza cadastro de cotas bancarias de clientes em forma de dicionário, 
    exemplo abaixo somente das chaves:
    dict(agencia, numero_da_conta_cliente, {cliente}, saldo, extrato, limite_de_saque_diario)
    OBS: um cliente pode ter varias contas, mas uma cota só pode pertencer a um cliente = 
    "CPF" (regra de negocio)

    :parâmetro "clientes": uma [lista] composta por {dicionários} com informações de contas 
    individuais de cada cliente

    :parâmetro "numero_da_conta_cliente": contador automático para criar número da cota 
    (elimina risco de duplicação no número da conta) 
    
    :parâmetro "conta_do_cliente": (variável global) = uma [lista] para armazenamento de 
    informações conta dos clientes
    '''

    # variaves locais para operação
    limite_de_saque_diario = 0
    agencia = '0001'
    extrato = []
    saldo = 0
    
    #  testa se usuário digitou somente números (função "teste_int") e armazena em cpf
    cpf = teste_int('\nInforme o CPF (somente número): ')

    # se cpf for diferente de 11 dígitos (finaliza função com mensagem para o usuário)
    if len(str(cpf)) != 11:
        return print('\nCPF digitado não esta com 11 dígitos')

    # teste se CPF do cliente já possui cadastro
    cpf_existe = filtro_cpf(clientes, cpf) # função auxiliar "filtro_cpf"
    

    # se filtro cpf_existe retorna "True" (finaliza função com mensagem para o usuário)
    if not cpf_existe:
        return print(f'\nNão existe cliente com este CPF: {cpf}')

    
    # armazena dados dos clientes cadastrado na lista "clientes"
    conta_do_cliente.append({'agencia' : agencia, 'numero_da_conta_cliente' : numero_da_conta_cliente, \
                            'cliente' : cpf_existe[1], 'saldo' : saldo, 'extrato' : extrato, 'limite_de_saque_diario' : limite_de_saque_diario})
    # OBS: cpf_existe[1] retorna uma tupla com dois valores (True, dicionário {clientes}) selecionado pelo parâmetro de "cpf" na função auxiliar "filtro_cpf")

    return print(f'\nAbertura da conta realizada com sucesso!!!\n\n {conta_do_cliente[numero_da_conta_cliente - 1]}')
    
# função para ("menu de opções" = EXIBIR CLIENTES CADASTRADOS)
def exibir_clientes_cadastrados(clientes):
    '''
    Função percorre a lista de [clientes] e exibe todos os dados cadastrados

    :parâmetro "clientes": (variável global) = uma [lista] composta por {dicionários} com informações pessoais dos clientes
    '''

    if clientes == []:
        print('\nNão há clientes cadastrados')
    else:
        print()
        print('.' * 130)
        for c in clientes:
            print(c) # exibe informações da lista [clientes]
            print('.' * 130)

# função para ("menu de opções" = EXIBIR CONTAS BANCARIAS)
def exibir_contas_bancarias(conta_do_cliente):
    '''
    Função percorre a lista [conta_do_cliente] e exibe todos os dados cadastrados

    :parâmetro "conta_do_cliente": (variável global) = uma [lista] composta por {dicionários} com informações de contas individuais de cada cliente
    '''

    if conta_do_cliente == []:
        print('\nNão há contas cadastradas')
    else:
        print()
        print('-' * 130)
        for c in conta_do_cliente:
            print(c) # exibe informações da lista [conta_do_cliente]
            print('-' * 130)

# função para ("menu de opções" = FINALIZAR)
def sair(loop_op):
    '''
    Função possibilita finalizar loop infinito da função (corpo principal do programa)

    :parâmetro "loop_op": variável global que inicia com valor "True"
    '''
    # opções para encerra loop infinito
    while True:
        # entrada de parâmetro do usuário
        loop_op = input('\nDeseja finalizar Sim = [s] ou Não = [n]:').lower()

        # resposta para usuário
        if loop_op == 's':
            loop_op = False # finalizar o programa
            break
        elif loop_op == 'n':
            loop_op = True # permanece no programa
            break
        else:
            # mensagem de erro caso  a resposta não seja Sim [s] ou Não [n]
            loop_op = True
            print('\nOpção invalida!!! \nDigite [s] para FINALIZAR ou [n] RETORNAR')
    # retorna novo valor para variável global "loop"    
    return loop_op 

# -------------------------------------------------- FUNÇÕES AUXILIARES --------------------------------------------------------

# função auxiliar para testar números inteiros
def teste_int(msg):
    """
    Testa caracteres digitada pelo usuário e verifica se é um número inteiro, caso seja retorna o número transformado, se não
    retorna uma mensagem de erro.

    :parâmetro msg : texto descrito pelo usuário em uma variável que receberá retorno
    """
    while True:
        try:
            num_str = input(msg).strip()
            num_int = int(num_str)
            return num_int
        except Exception as erro:
            print()
            print(f'\nErro de operação => ({erro})')
            print(f'Caractere "{num_str}" não é valido.')

# função auxiliar que testa se agencia digitada é igual "0001"
def teste_agencia(msg):
    """
    Testa caracteres digitada pelo usuário e verifica é igual "0001" e retorna valor, caso contrario exibe mensagem e retorna
    para função (corpo principal do programa)

    :parâmetro msg : texto descrito pelo usuário em uma variável que receberá retorno
    """
    agencia = input(msg).strip()
    if agencia == '0001':
        return agencia
    else:
        return False

# função auxiliar que testa se cpf digitado consta na lista
def filtro_cpf(clientes, cpf):
    '''
    Testa se parametro "cpf" digitado pelo usuário consta na lista [clientes] retorna (True e informação do cliente), filtrado pelo
    "cpf".

    :parâmetro "clientes": (variável global) = uma [lista] para armazenamento de informações dos clientes
    :parâmetro "cpf": (variável local) digitada pelo usuário
    '''
    # filtra se "cpf" do cliente já esta cadastrado e retorna ("True" + informações do cliente em forma de {dicionário}) ou (False)
    for cpf_existe in clientes:
        if cpf_existe['cpf'] == cpf:
            return (True, cpf_existe)
        else:
            continue
    return False

# função auxilia criação de endereço dentro da função "cadastro_cliente"
def endereco_cliente():
   '''
   Cria em forma de {dicionário} parametros do endereço:
   dict(logradouro = logradouro, numero = numero, bairro = bairro, cidade = cidade, estado = estado) 
   '''
   logradouro = input('Logradouro: ')
   numero = input('Número: ')
   bairro = input('Bairro: ')
   cidade = input('Cidade: ')
   estado = input('Estado: ')
   endereco = dict(logradouro = logradouro, numero = numero, bairro = bairro, cidade = cidade, estado = estado)
   return endereco

# ------------------------------------------------------------------------------------------------------------------

# função (corpo principal do programa)
def main():
    # variáveis globais
    loop = True # finaliza loop se False e permanece se True
    clientes = [] # lista de clientes
    conta_do_cliente = [] # lista de contas dos clientes

    # loop do sistema bancário
    while loop:
        # menu de operações existentes => "menu de opções"atingidoatigindo
        menu =  '''
============================================================
                    Menu de opções:
                    [1] DEPOSITO
                    [2] SAQUE
                    [3] EXTRATO
                    [4] CADASTRO CLIENTE
                    [5] ABRIR CONTA 
                    [6] EXIBIR CLIENTES CADASTRADOS
                    [7] EXIBIR CONTAS BANCARIAS
                    [8] FINALIZAR
                '''
        # exibir "menu de opções"
        print(menu)

        # entrada de parâmetro digitada pelo usuário
        opcao = input('Escolha uma opção:').lower()
        print('=' * 60)

        # "menu de opções" = DEPOSITO
        if opcao == '1':
            # armazena informações na lista [conta_do_cliente] "saldo" e "extrato"
            depositar(conta_do_cliente)
            
        # "menu de opções" = SAQUE
        elif opcao == '2':
            # armazena informações na lista [conta_do_cliente] "saldo" e "extrato"
            sacar(conta_do_cliente)

        # "menu de opções" = EXTRATO
        elif opcao == '3':
            # exibe informações "saldo" e "extrato" armazenado na [conta_do_cliente]
            extrato_bancario(conta_do_cliente)

        # "menu de opções" = CADASTRO CLIENTE
        elif opcao == '4':
            cadastro_cliente(clientes)

        # "menu de opções" = ABRIR CONTA 
        elif opcao == '5':
            numero_da_conta_cliente = len(conta_do_cliente) + 1 # contador automatico para criar número da conta bancaria
            abrir_conta(clientes, numero_da_conta_cliente, conta_do_cliente)

        # "menu de opções" = EXIBIR CLIENTES CADASTRADOS
        elif opcao == '6':
            exibir_clientes_cadastrados(clientes)

        # "menu de opções" = EXIBIR CONTAS BANCARIAS
        elif opcao == '7':
            exibir_contas_bancarias(conta_do_cliente)

        # "menu de opções" = FINALIZAR
        elif opcao == '8':
            loop = sair(loop)

        else:
            # caso usuário digite qualquer opção não existente no "Menu de opções" 
            print('Opção invalida, digite o NUMERO correspondente ao "Menu de opções:"')

main()
# mensagem do termino do programa
print('\nSistema finalizado com sucesso!!!\n')
