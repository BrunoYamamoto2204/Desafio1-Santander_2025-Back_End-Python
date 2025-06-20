menu = """ 
-- || Opções de operações || -- 

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

Escolha: """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # Depósito
    if opcao == "0":
        valor = float(input("Informe o valor do depósito: R$"))

        if valor > 0:
            saldo += valor
            extrato += f" - [+] Depósito:  R${valor:.2f} \n"
        else:
            print("[!] Depósito falhou! Valor Inválido")

    # Sacar
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: R$"))

        # Limites de saque
        if numero_saques >= LIMITE_SAQUES:
            print("[!] Saque falhou! Número de saques diários atingido")

        # Valor inválido
        elif valor <= 0:
            print("[!] Saque falhou! Valor informado é inválido")

        # Valor saldo
        elif valor <= saldo:
            if valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f" - [-] Saque: R${valor:.2f}\n" 
            else:
                print("[!] Saque falhou! Valor limite atingido")
        
        # Valor passa do limite 
        else: 
            print("[!] Saque falhou! Saldo insuficiente")

    # Extrato
    elif opcao == "2":
        print("\n" + "EXTRATO".center(30,"="))
        print("Não foram realiadas movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R${saldo:.2f}")
        print("=".center(30,"="))

    # Sair
    elif opcao == "3":
        print("\n" + "APLICAÇÃO ENCERRADA".center(30,"-") + "\n")
        break

    else:
        print("[!] Operação inválida! Selecione novamente a operação desejada")