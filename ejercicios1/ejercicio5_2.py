# clases en python, no se puede usar de forma declarativa
def funcion1(self, a, b):
    return a * b

class Pelota:
    color = ''

    func1 = funcion1

    def __init__(self, tamano, marca):
        self.tamano = tamano
        self.marca = marca
    
    def imprimir(self):
        print( "La pelota es de la marca " + self.marca + " y de talla " + str(self.tamano) )
    
    def setDiametro(self, diametro):
        new_diametro = func1(diametro,diametro/2)
        self.diametro = new_diametro
    def getDiametro(self):
        return self.diametro

pelota1 = Pelota(5,"void")
pelota2 = Pelota(7,"puma")
pelota1.imprimir()
pelota2.imprimir()
pelota1.setDiametro(30)
pelota2.setDiametro(45)
print( pelota1.getDiametro() )
print( pelota2.getDiametro() )
print( pelota1.color )
print( pelota2.color )
