# Programa para converter temperaturas...
print("converter de Celsium para Kelvin e Fahrenheit...")
celsius = int (input("digite a temperatura:"))

kelvin = celsius + 273
Fahrenheit = (9 / 5 * celsius) - 32
Fahrenheit = (9 / 5 * celsius) - 32
print(f"A temperatura em fahrenheit será {Fahrenheit} .")
# seria possivel utilizar as estruturascondicionais if/elif/else ou eatch/case.
# para facillitar este programa da forma que ele ofereça as três conversôes
# por exemplo ele poderia perguntar ao usuarioqual a unidade da medida e qual
# valor de temperatura ela quer convertere a partirdai, realizaros cáiculos
#
print("Qual conversão você desejar realizar? ") 
ecolha = int(input("1. celsius / 2. kelvin / 3. fahrenheit: "))
tempertura = int(input("Digite o valor da temperatura:"))

match escolha:
    case 1:
        kelvin = tempertura +273
        Fahrenheit = (9 /5 * tempertura) - 32
        print(f"A conversão de celsius para kelvin sera {kelvin}.")
        print(f"a convesão de celsius para fahrenheit será {Fahrenheit}")
    case 2:
        celsius = tempertura - 273
        Fahrenheit = 1.8* (tempertura -273) +32
        print(f"A conversão de kelvin para celsius será {celsius}.")
        print(f"A conversão de kelvin para fahrenheit será {Fahrenheit}") 
    case 3:
        celsius =5/9 *(tempertura -32) 
        kelvin =(tempertura -32) /  1.8 + 273
        print(f"A conversão de fahrenheit para calsius será {celsius}.")
        print(f"A conversão de fahrenheit para kelvin será {kelvin}.")         