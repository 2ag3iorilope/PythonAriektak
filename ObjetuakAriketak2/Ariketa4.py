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