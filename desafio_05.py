"""Assistente de Decisão de Lazer


O Projeto: "O que vamos fazer hoje?" 
Entradas:

temperatura (número).
esta_chovendo (sim/não).
tem_carro (sim/não).

Lógica de Decisão (Onde você treina os operadores):

> Cenário 1 (Praia/Parque): Se a temperatura for maior 
que 25 E não estiver chovendo.

> Cenário 2 (Cinema/Shopping): Se estiver chovendo 
E você tiver carro (ou se estiver muito frio).

> Cenário 3 (Ficar em Casa): Se estiver chovendo 
E você não tiver carro.

> Cenário 4 (Invenção sua): Use o or para criar uma 
condição onde você aceita sair se estiver calor OU se tiver um compromisso importante.

"""
print("******O que vamos fazer hoje? *******")

      
temperatura = int(input("Digite a temperatura de hoje: "))

esta_chovendo = str(input("Me responde: esta Chovendo: sim/não ")).upper()

tem_carro = str(input("Me responde: Voçe tem carro: sim/não ")).upper()

if temperatura >= 25 and esta_chovendo == "NÃO":

    print("Vamos para a praia. ")

elif  esta_chovendo == "SIM" and tem_carro == "SIM":

    print("Vamos para o shopping.")

elif esta_chovendo == "SIM" and tem_carro == "NÃO":

    print("Vamos ficar em casa hoje.")

elif temperatura >= 30 or tem_carro == "SIM":

    print("vamos de qualquer jeito, sair.")




