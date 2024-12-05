def es_numero(valor):
      
    return isinstance(valor,(int,float,complex))
    
def es_cadena_no_vacia(valor):
   
    return isinstance(valor, str) and bool(valor.strip())

  

class Hotel(object):
    def __init__(self, nombre="*", ubicacion="*", puntaje=0, precio=float("inf")):
        if es_cadena_no_vacia(nombre):
            self.nombre = nombre
        else:
            raise TypeError("Izenak ezin du hutsik joan")
        
        if es_cadena_no_vacia(ubicacion):
            self.ubicacion = ubicacion
        else:
            raise TypeError("Ubikazioak ezin du hutsik joan")
        
        if es_numero(puntaje):
            self.puntaje = puntaje
        else:
            raise TypeError("Puntajeak zenbaki bat izan behar du")
        
        if es_numero(precio):
            if precio != 0:
                self.precio = precio
            else:
                self.precio = float("inf")
        else:
            raise TypeError("Prezioak zenbaki bat izan behar du")
    
    def ratio(self):
        return ((self.puntaje**2)*10.)/self.precio      
    
    def __str__(self):
        return self.nombre + " de " + self.ubicacion + " - Puntaje: " + str(self.puntaje) + " - Precio: " + str(self.precio) + " euroak."
    
    def __lt__(self, otro):
        if self.ubicacion == otro.ubicacion:
            return self.ratio() < otro.ratio()  
        return self.ubicacion < otro.ubicacion  
    
    def __le__(self, otro):
        if self.ubicacion == otro.ubicacion:
            return self.ratio() <= otro.ratio()
        return self.ubicacion <= otro.ubicacion
    
    def __gt__(self, otro):
        if self.ubicacion == otro.ubicacion:
            return self.ratio() > otro.ratio()
        return self.ubicacion > otro.ubicacion
    
    def __ge__(self, otro):
        if self.ubicacion == otro.ubicacion:
            return self.ratio() >= otro.ratio()
        return self.ubicacion >= otro.ubicacion
    
    def __eq__(self, otro):
        return self.ubicacion == otro.ubicacion and self.ratio() == otro.ratio()
    
    def __ne__(self, otro):
        return self.ubicacion != otro.ubicacion or self.ratio() != otro.ratio()
    
    def cmpPrecio(self, otro):
       
        return self.precio - otro.precio  
     
    
    
      
   




# h = Hotel("Hotel City", "Mercedes", 3.25, 78)
# print(h)
# h = Hotel("Hotel City", "Mercedes", 3.25, 78)
# i = Hotel("Hotel Mascardi", "Bariloche", 6, 150)
# print (h< i)

h1=Hotel("Hotel 1* normal", "MDQ", 1, 10)
h2=Hotel("Hotel 2* normal", "MDQ", 2, 40)
h3=Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
h4=Hotel("Hotel vale la pena" ,"MDQ", 4, 130)
lista = [ h1, h2, h3, h4 ]
lista.sort()

for hotel in lista:
    print (hotel)
    
 