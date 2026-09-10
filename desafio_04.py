

""" 
O Problema: "Posso comprar isso?"

O objetivo é criar um assistente que não apenas subtrai valores, mas ajuda você a decidir se uma compra vai atrapalhar seus planos financeiros.
Fase de Construção Ativa (Minutos 5-40):

Entradas: Peça ao usuário seu saldo_atual, o valor_da_compra e uma meta_de_reserva.

(o valor mínimo que você quer manter na conta para emergências).

    Lógica do Sistema:

O programa deve calcular quanto sobraria após a compra.

Condição 1: Se o saldo for insuficiente para a compra, avise que não há dinheiro.

Condição 2: Se houver dinheiro, mas o saldo final ficar abaixo da sua meta de reserva, 
o programa deve emitir um alerta: "Você tem dinheiro, mas isso vai furar sua meta de economia!".

Condição 3: Se a compra for segura e mantiver você acima da meta, dê o "sinal verde".

"""
print("***** POSSO COMPRAR ISSO? *******")


saldo_atual = float(input("Digite o valor do saldo atual da sua conta bancaria: R$: "))

valor_da_compra = float(input("Digite o valor da compra: R$: "))

meta_de_reserva = float(input("Digite o valor minimo para ficar na conta como reserva de emergencia: R$ "))

saldo_apos_compra = saldo_atual - valor_da_compra

if saldo_apos_compra < meta_de_reserva:

    print(f"ALERTA: Você terá R$ {saldo_apos_compra:.2f}, o que fura sua meta de reserva de R$ {meta_de_reserva:.2f}!")

else:

    print(f"Compra segura! Você ainda terá R$ {saldo_apos_compra:.2f} guardados.")