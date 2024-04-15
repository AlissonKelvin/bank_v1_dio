def depositar(valor, saldo, extrato):
    print("DEPÓSITO\n")

    if valor > 0:
        saldo += valor
        extrato['Deposito'].append(valor)
    else:
        print("Valor informado é inválido!")

    return saldo, extrato

def sacar(valor, saldo, extrato, limite, numero_saques, limite_saques):
    print('\nSACAR\n')

    if saldo < valor:
        print(f'Saldo de R${saldo}, não será possível continuar com a transação.', saldo)
    elif valor > limite:
        print('Valor máximo permitido para saque é de R$500,00')
    elif numero_saques == limite_saques:
        print('Número de três saques diários atingido!')
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato['Saque'].append(valor)
    else:
        print("Valor informado é inválido!")

    return saldo, extrato

def extrato_conta(saldo, extrato):
    print('EXTRATO\n')

    print("\nDEPÓSITOS\n")
    for deposito in extrato['Deposito']:
        print(f"R${deposito}")

    print("\nSAQUES\n")
    for saque in extrato['Saque']:
        print(f"R${saque}")

    print(f"Saldo atual: R${saldo}")

def cadastrar_cliente(clientes):
    print("CADASTRO DE CLIENTES")
    
    nome = input('\nNome cliente:')
    data_nascimento = input('\nData de nascimento(DD/MM/AAAA):').replace('/', '').replace('-', '')
    cpf = input('\nCPF cliente:').replace('.', '').replace('-', '')
    endereco = input('\nEndereço (logradouro, cidade/estado):')

    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("\nCPF já cadastrado para outro cliente. Operação cancelada!")
            return

    clientes.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

def cadastrar_conta(clientes, contas):
    agencia = '001'
    numero_conta = 0

    cpf = input('\nInforme CPF do cliente para cadastrar:').replace('.', '').replace('-', '')

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            numero_conta += 1

            contas.append({
                "cpf": cliente["cpf"],
                "agencia": agencia,
                "numero_conta": numero_conta
            })
            print("Conta cadastrada com sucesso!")
            break
    else:
        print("CPF não encontrado na lista")

def main():
    saldo = 0.0
    limite = 500
    extrato = {'Deposito': [], 'Saque': []}
    clientes = []
    contas = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print('''
        
    [d] Depositar
    [s] Sacar
    [r] Registrar cliente
    [c] Cadastrar conta
    [e] Extrato
    [q] Sair

    ''')

        opcao = input('\nSelecione a opção desejada:').upper()

        if opcao == 'D':  # DEPOSITAR
            valor = float(input("Valor do depósito:"))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == 'S':  # SACAR
            valor = float(input("Valor do saque:"))
            saldo, extrato = sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == 'R':  # REGISTRAR CLIENTE
            cadastrar_cliente(clientes)

        elif opcao == 'C':  # CADASTRAR CONTA
            cadastrar_conta(clientes, contas)

        elif opcao == 'E':  # EXTRATO
            extrato_conta(saldo, extrato)

        elif opcao == 'Q':  # SAIR
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

if __name__ == "__main__":
    main()
