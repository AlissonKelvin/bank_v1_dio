menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''



saldo = 0.0
limite = 500
extrato ={'Deposito':[],'Saque':[]} #armazenando os valores de deposito e saque
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao =input(menu + 'Selecione a opção desejada:').upper()
    
    if opcao == 'D':
        print("DEPOSITO\n")

        depositar = int(input("Valor do deposito:"))
        
        if depositar > 0:
            saldo += depositar
            extrato['Deposito'].append(depositar)
        else:
            print("Valor informado é invalido!")        
        
    elif opcao == 'S':
        print('SACAR\n')
        
        saque = float(input("Valor saque:"))
                
        if saldo < saque:
            print(f'Saldo de R${saldo}, não será possível continuar com a transação.',saldo)
        elif saque > 500:
            print('Valor máximo permitido para saque é de R$500,00')
        elif numero_saques == 3:
            print('Número de três saques diario atingido!')
        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato['Saque'].append(saque)
        else:
            print("Valor informado é inválido!")

    elif opcao == 'E':
        print('EXTRATO\n')

        print("DEPOSITOS\n")        
        for deposito in extrato['Deposito']:
            print(f"R${deposito}")

        print("SAQUES\n")
        for saque in extrato['Saque']:
            print(f"R${saque}")         

        print(f"Saldo atual:{saldo}")

    elif opcao == 'Q':
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
