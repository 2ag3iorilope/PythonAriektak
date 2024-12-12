class TintaAmaitutaException(Exception):
    pass

class Papel:
    def __init__(self):
        self.testua = ""

    def Idatzi(self, testua):
        self.testua += testua

    def __str__(self):
        return self.testua


class Boligrafo:
    def __init__(self, Tinta_Kop):
        self.Tinta_Kop = Tinta_Kop

    def Idatzi(self, testua, papel):
        if len(testua) > self.Tinta_Kop:
            raise TintaAmaitutaException("Ez dago tintarik.")
        
        papel.Idatzi(testua)
        self.Tinta_Kop -= len(testua)
    def __str__(self):
        return "Geratzen den Tinta: " + str(self.Tinta_Kop)

class Marcador(Boligrafo):
    def __init__(self, Tinta_Kop):
        super(Marcador, self).__init__(Tinta_Kop)

    def recargar(self, cantidad):
        self.Tinta_Kop += cantidad
        print("Markadorea rekargatu da {} unitateekin.".format(cantidad))
            

papel = Papel()
marcador = Marcador(30)  

try:
    marcador.Idatzi("Markadoreko testuaa. ", papel)
    print(papel)  
    print(marcador)  
    marcador.recargar(20) 
    print(marcador) 
    marcador.Idatzi("testuGehiago. ", papel)
    print(papel) 
except TintaAmaitutaException as e:
    print(e)