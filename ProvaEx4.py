saldo = 0
saque = 0
deposito = 0
sair = 0
saldo = 0



print("Digite 1 p/ acessar saldo")
print("Digite 2 p/ acessar saque")
print("Digite 3 p/ acessar deposito")
print("Digite 4 p/ sair")
opcoes = float(input("Digite sua opcao:"))

if opcoes == 1:
    print("Seu saldo e:" + str(saldo))
    opcoes = input("Digite sua proxima opcao: 1-saldo 2-saque 3-deposito 4-sair")

if opcoes == 2:
    saque =int(input(("Qnto vc deseja sacar:")))
    deposito = deposito - saque
    saldo = saldo + deposito
    opcoes = input("Digite sua proxima opcao: 1-saldo 2-saque 3-deposito 4-sair")
if opcoes == 3:
    deposito = int(input("Qnto vc deseja depositar:"))
    saldo = saldo + deposito

if opcoes == 4:
    print("Ok, vc escolheu sair.")

