# Demostração do uso de estrutura repetitiva...
contador = 0; senha =""
while senha != "s3nh4":
    print("Dígite a senha:")
    senha = input9

    if senha == "s3nh4":
        print("senha correta!")
        break
    else
        print("Senha errada...")

        contador = contador +1
        if contador == 3:
            print("Tentativa excedidas!")
            break