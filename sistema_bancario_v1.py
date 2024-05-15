menu  = f'''
          (1) Depositar
          (2) Sacar
          (3) Extrato
          (0) Sair 
          '''

saldo = 0
qtde_saque = 3
extrato = ""
valor_saque = 0
limite_saque = 500

while True:
    print(menu)
    opcao  = int(input('Digite a opção desejada : '))

    if opcao == 1:
        deposito = float(input('Digite o valor do depósito: '))
        if deposito <= 0:
            print("Valor inválido!!!")
            print("Tente novamente!!!")
            continue
        saldo += deposito
        
    if opcao == 2:
        if qtde_saque == 0:
            print("Quantidade de saque excedido")
        
        else:
            saque = float(input("Digite o valor do saque: "))
            if saque > saldo:
                print('Saldo insuficiente')
            elif saque <= 0:
                print("Valor inválido")
            elif limite_saque < valor_saque + saque:
                print("Limite de saque diário excedido") 
            else:
                saldo -= saque
                qtde_saque -=1
                valor_saque += saque
                
    if opcao == 0 :
        print("saindo do sistema!!!")
        break


    print(f"Seu saldo é { saldo}")
    
