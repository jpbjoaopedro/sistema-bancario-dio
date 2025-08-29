usuarios = []
contas_corrente = []
agencia = '0001'

saldo = 0
limite_valor_saque = 500
limite_quantidade_saque_diario = 3
saques_realizados = 0
extrato = []


# Conta ADM

menu_adm = """
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

def criar_usuario(*, nome=None, data_nascimento=None, cpf=0, endereco=None):
    global usuarios
    for usuario in usuarios:
        if cpf in usuario:
            print("Cpf já cadastrado!")
            return
    usuarios.append({cpf: {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}})


def criar_conta(cpf_usuario):
    global contas_corrente, agencia
    saldo = 0
    if not contas_corrente:
        conta = 1
    else:
        conta = list(contas_corrente[-1].keys())[0] + 1
    contas_corrente.append({conta: {'agencia': agencia, 'saldo': saldo, 'usuario': cpf_usuario}})


# Conta corrente

menu_conta = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def depositar(deposito, saldo, extrato):
    if deposito <= 0:
        print("Valor de depósito inválido")
    else:
        saldo += deposito

        extrato.append(f"Deposito: {deposito}; Saldo: {saldo:.2f}")
    return saldo


def sacar(*, saldo, saque, saques_realizados, limite_diario_valor, limite_diario_quantidade, extrato):
    if saques_realizados >= limite_diario_quantidade:
        print("Limite diário de saques antingido!")
    elif saque > limite_diario_valor:
        print(f"Tentative de saque maior que a permitida ({limite_diario_valor})!")
    elif saldo >= saque:
        saques_realizados += 1
        saldo -= saque
        extrato.append(f"Saque: {saque}; Saldo: {saldo:.2f}")
    else:
        print("Saldo insuficiente.")
    return saldo, saque, saques_realizados, limite_diario_valor, limite_diario_quantidade


def mostrar_extrato(saldo, /, extrato):
    print("Mostrando extrato.")
    print(f"""
Saldo atual: {saldo:.2f}
Histórico: 
{'\n'.join(extrato) if extrato else "Nenhuma movimentação realizada"}.
    """)
    return


# Main
main_menu = """
[1] Conta ADM
[2] Conta Cliente
[3] Sair

=> """

while True:
    opcao_menu = int(input(main_menu))

    match opcao_menu:
        case 1:
            while True:
                opcao = input(menu_adm)

                match opcao:
                    case 'u':
                        nome = input("Nome: ")
                        cpf = input("CPF: ")
                        endereco = input("Endereco: ")
                        data_nascimento = input("Data nascimento: ")

                        criar_usuario(nome= nome, cpf=cpf, endereco=endereco, data_nascimento=data_nascimento)
                    case 'c':
                        cpf = input("CPF: ")
                        
                        criar_conta(cpf)
                        print()
                    case 'q':
                        print("Retornando a o menu...")
                        break
                    case _:
                        print("Opção inválida!")
        case 2:
            while True:
                opcao = input(menu_conta)

                match opcao:
                    case 'd':
                        deposito = float(input("Valor a ser depositado: "))
                        saldo = depositar(deposito, saldo, extrato)
                    case 's':
                        saque = float(input("Digite o valor a ser sacado: "))
                        saldo, _, saques_realizados, _, _ = sacar(
                            saldo=saldo, 
                            saque=saque, 
                            saques_realizados=saques_realizados,
                            limite_diario_valor=limite_valor_saque, 
                            limite_diario_quantidade=limite_quantidade_saque_diario, 
                            extrato=extrato
                            )
                    case 'e':
                        mostrar_extrato(saldo, extrato=extrato)
                    case 'q':
                        print("Retornando a o menu...")
                        break
                    case _:
                        print("Opção inválida!")
        case 3:
            print("Finalizando o sistema...")
            break

        case _:
            print("Opção inválida!")