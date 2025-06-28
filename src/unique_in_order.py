def unique_in_order(sequence):
    
    result = []
    previus = object()
    

    for item in sequence:
        if item != previus:
            result.append(item)
            previus = item
    return result


if __name__== "__main__":
    exemplos = [
        "AAAABBBCCDAABBB",
        "ABBCcAD",
        [1,2,2,3,3],
        (1,2,2,3,3)
    ]

    for seq in exemplos:
        print(f"Entrada: {seq}\Resultado:{unique_in_order(seq)}\n")