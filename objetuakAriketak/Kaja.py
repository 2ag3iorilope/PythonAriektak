class Kaja:
    def __init__(self):
        self.dirua = {
            500: 0,   
            200: 0,   
            100: 0,   
            50: 0,    
            20: 0,    
            10: 0,   
            5: 0,     
            2: 0,     
            1: 0,     
            2.0: 0,   
            1.0: 0,   
            0.50: 0,  
            0.20: 0,  
            0.10: 0,  
            0.05: 0,  
            0.02: 0,  
            0.01: 0      
        }
    
    def gehitu_dirua(self, balorea, kantitatea):
        """Añade dinero a la caja según el valor de la moneda/billete y la cantidad."""
        if balorea in self.dirua:
            self.dirua[balorea] += kantitatea
        else:
            raise ValueError("{} Balorea ez da egokia.".format(balorea))
    
    def totala(self):
        """Devuelve el total de dinero en la caja en euros."""
        return sum(balorea * kantitatea for balorea, kantitatea in self.dirua.items())
    
    def desglosea(self):
        """Devuelve un desglose del dinero en la caja."""
        desglosea = ""
        for balorea, kantitatea in sorted(self.dirua.items(), reverse=True):
            if kantitatea > 0:
                desglosea += "{}€ ko {} billete \n".format(balorea, kantitatea)
        return desglosea
    
    def __str__(self):
        """Devuelve un resumen del total y el desglose del dinero en la caja."""
        return "Totala kajan: {}€\nDesglosea :\n{}".format(self.totala(), self.desglosea())

# Ejemplo de uso
kaja = Kaja()
kaja.gehitu_dirua(10, 5)   # 5 billetes de 10€
kaja.gehitu_dirua(0.50, 7)  # 7 monedas de 0.50€
kaja.gehitu_dirua(0.10, 4)  # 4 monedas de 0.10€

# Imprimir el resumen de la caja
print(kaja)

# Obtener el total de dinero
print("Kajako diru totala: {}€".format(kaja.totala()))
