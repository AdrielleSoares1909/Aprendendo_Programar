
valor_da_compra = float(input("Digite o valor da compra: "))

idade = int(input("Digite sua idade: "))

estudante = str(input("Voçe é estudante: SIM/NÃO ")).upper()


if idade >= 60:

    desconto = valor_da_compra * 0.85

    print(f"Voce recebeu um desconto:  voce ira pagar apenas R$ {desconto:.2f} na sua compra.")


elif estudante == "SIM":

    desconto  = valor_da_compra * 0.90

    print(f"Voce recebeu um desconto:  voce ira pagar apenas R$ {desconto:.2f} na sua compra.")

else:

    print(f"Voce não recebeu nenhum valor de desconto pois não é estudante, o valor a ser pago é : R$ {valor_da_compra:.2f}")