

nota1 = float(input("Digite a nota do primeiro Bimestre: "))
nota2 = float(input("Digite a nota do segundo Bimestre: "))


if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 :

    print("Erro: Uma das notas digitadas é inválida! Digite valores entre 0 e 10.")

else:

    resultado = (nota1 + nota2) / 2

    if resultado >= 7 :


        print(f"A media dos dois bimestres foi de : {resultado:.2f} pontos. PARABENS, voce esta aprovado!!!")

    elif resultado >= 5:

        print(f"A media dos dois bimestres foi de : {resultado:.2f} pontos voce se enrolou,esta na media!!! Vai estudar mais.")

    else:
    
        print(f"A media dos dois bimestres foi de : {resultado:.2f} pontos.Voce esta Reprovado!!!")