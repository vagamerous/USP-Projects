# Esse programa simples, mas poderoso, é um ordenador de lista, que ordena a lista em ordem crescente. Sua aplicação pode ser muito útil em diversos tipos de negócios diferentes.  
# This simple but powerful program is a list sorter, which sorts the list in ascending order. Its application can be very useful in several different types of businesses. 

def bubble_sort(lista):  # definindo a função, colocando como parâmetro a lista a ser ordenada; defining the function, placing the list to be sorted as a parameter. 

    fim = len(lista) # colocando em uma variável o tamanho da lista; placing the list size in a variable; 

    for i in range(fim-1, 0, -1): # fazemos um range que vai de trás para frente; we make a range from the end to the beginning. 
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print (lista)

    return lista
