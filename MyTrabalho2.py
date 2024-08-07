# Correção de exercicios
posicao = input("Digite a posição  que você joga: ")

if posicao == "goleiro" or posicao == "zagueiro" or posicao == "lateral":
    print("Você joga no meio - campo!")
elif posicao == "volante" or posicao == "meia":
    print("Você joga no meio-campo!")
elif posicao == "ponta" or posicao == "atacante" or posicao == "centroavante":
    print("Você joga no ataque!")
else:
    print("Você joga de teimoso...")          