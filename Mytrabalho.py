# Correção de atividades...
x = int(input("Dígite o valor de x: "))
y = int(input("Dígite o valor de y: "))
z = int(input("Dígite o valor de z: "))

if x < y and y < z:
    print("Estão em ordem crescente!")
elif x > y and y > z:
    print("Estão em ordem decescente!")
else:
    print("Estão misturados...")        