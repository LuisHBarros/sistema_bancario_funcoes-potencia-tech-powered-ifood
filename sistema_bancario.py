"""
Sistema bancario basico Python, implementando as funcoes deposito, saque e extrato
"""

saldo = 0.0


def saque() -> None:
    global saldo
    valor = float(input("Qual o valor do saque?"))
    if saldo < valor:
        print(
            """
        Operacao nao concluida!
        Saldo insuficiente
    """
        )
        return
    saldo -= valor
    return


def deposito() -> None:
    global saldo
    valor = float(input("Qual o valor do deposito?"))
    saldo += valor
    return


def extrato() -> None:
    global saldo
    print(
        f"""
    EXTRATO
    SALDO : R${saldo:.2f}
"""
    )
    return


print("Bem vindo ao Pybank!")
saldo = 0.0
e = "Sim"
while e == "Sim":
    operacao = int(
        input("Qual operacao deseja executar?\n1-)Deposito 2-)Saque 3-)Extrato")
    )
    if operacao == 1:
        deposito()
    if operacao == 2:
        saque()
    if operacao == 3:
        extrato()
    e = input("Deseja realizar outra operacao?\n(Sim) (NAO)")
print("Obrigado pela preferencia, Pybank")
