def conversorDecimal(romano):
        lista = {
        "I" : 1, 
        "V" : 5, 
        "X" : 10, 
        "L" : 50, 
        "C" : 100, 
        "D" : 500, 
        "M" : 1000
        }
        decimal = 0
        valorPrev = 0 
        for char in reversed(romano):
            valorAtual = lista[char]
            if valorAtual < valorPrev:
                decimal -= valorAtual
            else:
                decimal += valorAtual
            valorPrev = valorAtual
        return decimal

romano = input("Digite o valor em algarismos romanos para ser convertido em decimal: ").upper()

try:
    resultado = conversorDecimal(romano)
    print("Conversão para decimal: ", resultado)
except KeyError:
    print("Entrada inválida")