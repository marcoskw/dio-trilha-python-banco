# Implementar 3 operações:
    # Depósito
    # Saque
    # Extrato

# 1 usuario só

# permitir 3 saques diários de no máximo 500
# se não tiver saldo, informar que não é possivel sacar pois falta saldo
# saques devem ser exibidos no extrato

# Operação do extrato, conter as listagens de saques e depositos, e mostrar valor final com o formato R$ XXX,XX



#PARÂMETROS
menu =  """
||  .: BANCO MKW :.  ||
||.'               '.||
=======================
||  [1] - DEPÓSITO   ||
||  [2] - SAQUE      ||
||  [3] - EXTRATO    ||
||  [9] - SAIR       ||
=======================
Digite uma opção: 
"""
saldo = float(0)
limite = 500
extrato = ""
quatidade_saque_diario = int(0)
LIMITE_SAQUES_DIARIO = 3

while True:

    operacao = input(menu)

    #  deposito
    if operacao == "1":
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        valor_deposito = float(input("Informe o valor a ser depositado: R$ "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            print("Depósito falhou. A informação passada é inválida. Depósito não informado.")
        
    #  saque
    if operacao == "2":
        print("-----------------------------------------------------------------")  
        valor_saque = float(input("Informe o valor a ser sacado: R$ "))  
        print("-----------------------------------------------------------------")    
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = quatidade_saque_diario >= LIMITE_SAQUES_DIARIO

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Você excedeu o limite de saque!")

        elif excedeu_saques:
            print("Você excedeu o limite de saque diario!")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            quatidade_saque_diario += 1

        else:
            print("O valor informado é inválido")
        print("-----------------------------------------------------------------") 

    #extrato
    if operacao == "3":
        print("@@@@@@@@@@@@@@@@@@ E X T R A T O @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
        print(extrato)
        print(f"O seu saldo é: R$ {saldo:.2f}")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 

    if operacao == "9":
        break
