class Personaje:
    def __init__(self, Bizitza, posizioa, abiadura):
        self.Bizitza = Bizitza
        self.posizioa = posizioa
        self.abiadura = abiadura

    def recibir_ataque(self, cantidad):
     
        self.Bizitza -= cantidad
        if self.Bizitza <= 0:
            raise Exception("Pertsonaiaren bizitza 0ra iritsi da.")

    def mover(self, norabidea):
      
        if norabidea == "arriba":
            self.posizioa[1] += self.abiadura
        elif norabidea == "abajo":
            self.posizioa[1] -= self.abiadura
        elif norabidea == "izquierda":
            self.posizioa[0] -= self.abiadura
        elif norabidea == "derecha":
            self.posizioa[0] += self.abiadura
        else:
            raise ValueError("Norabide Desegokia. Erabili 'arriba', 'abajo', 'izquierda' o 'derecha'.")

class Soldado(Personaje):
    def __init__(self, Bizitza, posizioa, abiadura, eraso):
        super(Soldado, self).__init__(Bizitza, posizioa, abiadura)
        self.eraso = eraso

    def atacar(self, otro_personaje):
       
        if not isinstance(otro_personaje, Personaje):
            raise ValueError("Helburuak pertsonaia izan behar du.")
        
        otro_personaje.recibir_ataque(self.eraso)
        print("Soldadoak {} bizitza puntu kendu dizkio.".format(self.eraso))


class Campesino(Personaje):
    def __init__(self, Bizitza, posizioa, abiadura, cosecha):
        super(Campesino, self).__init__(Bizitza, posizioa, abiadura)
        self.cosecha = cosecha

    def cosechar(self):
        
        print("Baserritarrak {} unitate landare bildu ditu.".format(self.cosecha))
        return self.cosecha




personaje = Personaje(100, [0, 0], 5)


soldado = Soldado(100, [10, 10], 5, 30)


campesino = Campesino(80, [5, 5], 4, 50)


soldado.atacar(personaje)
print("Bizitza geratzen da:", personaje.Bizitza)

cantidad_cosechada = campesino.cosechar()
print("Bildutako Kantitatea:", cantidad_cosechada)


soldado.mover("arriba")
print("Posizioa mugitu ondoren:", soldado.posizioa) 
