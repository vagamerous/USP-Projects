class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return int(self.a + self.b + self.c)

    def tipo_lado(self):

        if self.a == self.b:
            if self.a == self.c:
                
                return 'equilátero'
            else:
                
                return 'isósceles'
        elif self.a == self.c:
            if self.a == self.b:
                
                return 'equilátero'
            else:
                
                return 'isósceles'
                

        elif self.b == self.c:
            if self.b == self.a:
                
                return 'equilátero'
            else:
                
                return 'isósceles'

        else:
            
            return 'escaleno'

        
