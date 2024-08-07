# Este é um comentario!

local = input("Qual foi o local  que você viajou? ")
match local:
    case "Disney":
        print("Então você levou as crianças!")
    case "Paris":
        print("Lugar perfeito para passeios românticos.")
    case _:
        print("Não conheço estelugar...")