class Punto(object):
  
  def __init__(self, x=0,y=0):
      
     if es_numero(x) and es_numero(y):
       self.x= x
       self.y= y
       
     else:
        raise TypeError("X eta Y zenbaki numerikoak izan behar dira")    
      
   
  def __str__(self):
   
    return "(" + str(self.x) + ", " + str(self.y) + ")"
  
  def __add__(self, otro):
  
    return Punto(self.x + otro.x, self.y + otro.y)

  def __sub__(self,otro):
   return Punto(self.x - otro.x, self.y - otro.y)
   
  def distancia(self, otro):
    # dx= self.x -otro.x
    # dy = self.y - otro.y
    # return (dx*dx + dy*dy)**0.5
    r = self.restar(otro)
    return r.norma()   

  def restar(self,otro):
   return Punto(self.x - otro.x, self.y - otro.y)

  def norma(self):
   return (self.x *self.x  + self.y*self.y)**0.5 
  
def es_numero(valor):
      
    return isinstance(valor,(int,float,complex))

   

# p = Punto("A",True)
# print (p)
# print (p.x)
# print(p.y)
# p = Punto(5,7)
# q = Punto(2,3)
# r = p.restar(q)
# print (r.x, r.y)
# print (r.norma())
# print (q.distancia(r))
# print (p.distancia(q))

# p = Punto(-6,18)
# str(p)
# print(p)
p = Punto(3,4)
q = Punto(2,5)
print (p - q)
print (p + q)

    