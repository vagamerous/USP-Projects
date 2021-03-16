def encontra_impares(lista):
    
    x = len(lista)
    
    
    if x == 0:
        return lista
        
        
    else:
        if lista[0] % 2 == 0:
            
            return encontra_impares(lista[1:])
        else:
            
            return [lista[0]] + encontra_impares(lista[1:])



        
        
        
            
            
        

    
