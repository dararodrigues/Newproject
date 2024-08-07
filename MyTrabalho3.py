# correção exercicios...
execucao = input("O serviço foi feito (sim/não)? ")
avaliacao = int (input("Qual a nota da avaliação (1/5)?"))

if execucao == "sim" and avaliacao == 1:
    prin("O serviço foi péssimo!")
elif execucao == "sim" and avaliacao == 2:
    print ("O serviço foi ruim!")
elif execucao == "sim" and avaliacao == 3:
    print("O serviço foi razoálvel!") 
elif execucao == "sim" and avaliacao == 4:
    print("O serviço foi bom!")
elif execucao == "sim" and avaliacao == 5:
    print("O serviço foi excelente!")
else:
    if execucao == "não" and avaliacao == 0:
       reclamacao = input("Dígite a sua reclamação: ")
    else:
        print("As suas avaliações não fazem sentido!")      