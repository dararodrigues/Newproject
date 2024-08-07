# Demostração do uso de estrutura repetitiva...
numero = 1
while numero >= 0:
    print("Dígite um número negativo para sair:")
    numero = int(input())
    break
    print("Este texto não sera exibido! Mas...")
else:
    print("o número digitado foi:", numero)