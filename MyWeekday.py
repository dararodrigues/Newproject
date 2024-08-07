# Correção de exercicios...
semana = input("Digite o dia da semana:")

match semana:
    case "segunda":
        print("Dia de lavar roupa!")
    case "terça":
        print("Dia de varrer casa!")
    case "quarta":
        print("Dia de cozinhar...")
    case "quinta":
        print("Dia de lavar o banheiro!")
    case "sexta": 
        print("sextou!!!")
    case "sábado":
        print("churrasco na lage!")
    case "domingo":
        print("Devo ir á missa/culto?")
    case _:
        print("Não sei o que fazer...")

nota1 = int(input("digite anota 1,"))
nota2 =int(input("Digite a nota 2,"))
nota3 =int(input("Digite a nota 3,"))
nota4 =int(input("Digite a nota 4,"))
média = (nota1*nota2*nota3*nota4) /4

if média>=6:
    print("Você está aprovado!")
else:
    print("Você está reprovado...")
    print("sua média é (média)")   

peso = int(input("Dígite o seu peso"))
altura =int(input("Dígite asua altura!"))
imc =peso / altura == 2

print("o seu imc é (IMC).")
if imc >25:
    print("Você está acima do peso!")
elif imc < 18:
    print("Você estar abaixo do peso!")
else:
    print("o seu peso está ok!")
