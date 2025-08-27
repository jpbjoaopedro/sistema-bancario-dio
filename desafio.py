saldo = 0
limite_valor_saque = 500
limite_quantidade_saque_diario = 3
saques_realizados = 0
extrato = []

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    match opcao:
        case 'd':
            deposito = int(input("Valor a ser depositado: "))
            if deposito <= 0:
                print("Valor de depósito inválido")
                continue
            saldo += deposito
            extrato.append(f"Deposito: {deposito}; Saldo: {saldo:.2f}")
        case 's':
            saque = int(input("Digite o valor a ser sacado: "))

            if saques_realizados >= limite_quantidade_saque_diario:
                print("Limite diário de saques antingido!")
                continue
            if saque > limite_valor_saque:
                print("Tentative de saque maior que a permitida (500)!")
            if saldo >= saque:
                saques_realizados += 1
                saldo -= saque
                extrato.append(f"Saque: {saque}; Saldo: {saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        case 'e':
            print("Mostrando extrato.")
            print(f"Saldo atual: {saldo:.2f}\nHistórico: {extrato}" if extrato else "Nenhuma movimentação realizada.")
        case 'q':
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida!")