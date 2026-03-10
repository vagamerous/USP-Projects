# This code identifies plagiarism between texts. 
# For this, metrics used by professionals to identify plagiarism, such as the Hapax Legomana ratio, are calculated from the text data.  
# Esse código identifica plágio entre textos.
# Para isso, métricas utilizadas por profissionais para identificar os plágios, como a Razão Hapax Legomana, são calculadas a partir dos dados dos textos.

import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    

    wal = abs(as_a[0] - ass_cp[0])
    ttr = abs(as_a[1] - ass_cp[1])
    hlr = abs(as_a[2] - ass_cp[2])
    sal = abs(as_a[3] - ass_cp[3])
    sac = abs(as_a[4] - ass_cp[4])
    pal = abs(as_a[5] - ass_cp[5])

    s = (wal + ttr + hlr + sal + sac + pal) / 6

    return s

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    QntPalavras = 0
    QntFrases = 0
    sentencas = separa_sentencas(texto)
    TotalCaractEspaco = 0  
    TotalCaracteres = 0
    TotalCaractFraseEspaco = 0

    palavras = []
        
    for sentenca in sentencas:
        TotalCaractEspaco += len(sentenca)
        
        for frase in separa_frases(sentenca):
            QntPalavras += len(separa_palavras(frase))
            QntFrases += 1
            TotalCaractFraseEspaco += len(frase)
            
            for palavra in separa_palavras(frase):
                TotalCaracteres += len(palavra)
                palavras.append(palavra)

    PalavrasDiferentes = n_palavras_diferentes(palavras)

    PalavrasUnicas = n_palavras_unicas(palavras)

    QntSentencas = len(separa_sentencas(texto))
                
    wal = float(TotalCaracteres / QntPalavras)
    ttr = float(PalavrasDiferentes / QntPalavras)
    hlr = float(PalavrasUnicas / QntPalavras)
    sal = float(TotalCaractEspaco / QntSentencas)
    sac = float(QntFrases / QntSentencas)
    pal = float(TotalCaractFraseEspaco / QntFrases)
    
    return [wal, ttr, hlr, sal, sac, pal]
    

   
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    similaridade = []
    

    for texto in textos:
        as_a = calcula_assinatura(texto)
        similaridade.append(compara_assinatura(as_a, ass_cp))

    n = (len(similaridade) - 1)
    infectado = similaridade[n]

    while n >= 1:
        if similaridade[n - 1] < similaridade [n]:
            infectado = similaridade[n - 1]
        n -= 1

    x = 0
    igualdade = False
    NumeroTextoInfectado = 0
    
    while igualdade == False:
        if similaridade[x] == infectado:
            NumeroTextoInfectado = x + 1
            igualdade = True
        else:
            x += 1
            
            
    print("O autor do texto", NumeroTextoInfectado, "está infectado com COH-PIAH")        

    return NumeroTextoInfectado


ass_cp = le_assinatura()
print()
textos = le_textos()
print()
avalia_textos(textos, ass_cp)

    
