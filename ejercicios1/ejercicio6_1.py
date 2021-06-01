# herencia en clases en python
class Pelota:
    color = ''

    def __init__(self, tamano, marca):
        self.tamano = tamano
        self.marca = marca
    
    def imprimir(self):
        print( "La pelota es de la marca " + self.marca + " y de talla " + str(self.tamano) )
    
    def setDiametro(self, diametro):
        self.diametro = diametro
    def getDiametro(self):
        return self.diametro

class PelotaTenis(Pelota):
    def setTipoFelpa(self, tipo):
        self.tipo=tipo
    def getTipoFelpa(self):
        return self.tipo

pelota1 = PelotaTenis(5,"void")
pelota2 = PelotaTenis(7,"puma")
pelota1.imprimir()
pelota2.imprimir()
pelota1.setDiametro(30)
pelota2.setDiametro(45)
print( pelota1.getDiametro() )
print( pelota2.getDiametro() )
print( pelota1.color )
print( pelota2.color )
pelota1.setTipoFelpa("Suave")
pelota2.setTipoFelpa("Burda")
print( pelota1.getTipoFelpa() )
print( pelota2.getTipoFelpa() )
