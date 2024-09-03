menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def criar_extrato(valor:float):
    hola = f"Depósito: R$ {valor:.2f}\n"
    return hola


while True:
    extrato = criar_extrato(saldo)
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor>500:
            print("O numero maximo de saque é 500 R$ por dia")
            continue
        elif numero_saques>3:
            print("O número maximo de saques por dia é 3")
            continue
        elif saldo<valor:
            print("A quantidade do saldo não é suficiente para o saque")
            continue
        
        saldo -= valor

    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")