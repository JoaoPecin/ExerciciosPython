valor = float(input("Digite o valor da compra: R$ "))
pagamento = input("Digite a forma de pagamento (dinheiro ou cartao): ")

if pagamento == "dinheiro":
    valor_final = valor * 0.90
    print(f"Valor final: R$ {valor_final:.2f}")

elif pagamento == "cartao":
    parcelas = int(input("Digite o número de parcelas: "))

    if parcelas > 3:
        valor_final = valor * (1.02 ** parcelas)
        print("Haverá juros de 2% ao mês.")
    else:
        valor_final = valor
        print("O pagamento será sem juros.")

    print(f"Valor final: R$ {valor_final:.2f}")
