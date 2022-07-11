from re import T


def reverseDigits(value):
    return reverseAux(value, 0)

def reverseAux(partValue, partReversed):
    if partValue == 0:
        return partReversed
    unidades = partValue % 10
    dezenas = partValue // 10
    return reverseAux(dezenas, partReversed*10 + unidades)

print(reverseDigits(1234))