def dimensoes(matriz):
    lin = int(len(matriz))

    col = (len(matriz[0]))

    return lin, col

def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):

        soma = 0
        matriz_soma = []
        
        
        for i in range(len(m1)):
            linha = []
            
            for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
            matriz_soma.append(linha)

        print(matriz_soma)

        
        
        return matriz_soma

    else:
        print('False')
        return False
    
