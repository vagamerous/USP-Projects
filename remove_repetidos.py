


def remove_repetidos(lista):
    
    x = 0
    n = x + 1
    while x <= (len(lista) - 2):
        while n <= (len(lista) - 1):
            if lista[x] == lista[n]:
                del lista[n]
            else:    
                n = n + 1
        x = x + 1
        n = x + 1

    return sorted(lista)
            
    
