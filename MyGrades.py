# Correção de execicios...
clube = input("Digite o nome do clube: ")
posicao =int(input("Dígite a sua posição: "))

if posicao == 1:
    print("É campeão")
elif posicao > 1 and posicao <= 6:
    print("Libertadores!")
elif posicao > 6 and posicao <= 12:
    print("Sul-Americanos!")
elif posicao > 12 and posicao <= 16:
    print("Sem classificação.")
elif posicao >= 17 and posicao <= 20:
    print("Rebaixado...")
else:
    print("Dídite aposição correta")               














