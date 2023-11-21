class Rectangle():
    
    #def __init__(self) :
       #self.Longeur = 50
       #self.largeur = 30
    
    def __init__(self,longeur,largeur) :
       self.longeur=longeur
       self.largeur=largeur
    
    #def __init__(self,oldRectangle) :
       #self.longeur=oldRectangle.longeur
       #self.largeur=oldRectangle.largeur
    
    
    def Perimetre(self):
       P=((self.longeur+self.largeur)*2)
       return P
    
    
    def Aire(self):
       A=(self.largeur*self.longeur)
       return A
    
    def IsCarre(self):
       if self.largeur==self.longeur :
          return True
       else :
          return False
       
    def AfficherRectangle(self):
       print("longeur :",self.longeur)
       print("largeur :",self.largeur)
       print("Perimetre :",Rectangle.Perimetre(self))
       print("Aire :",Rectangle.Aire(self))
       if Rectangle.IsCarre(self) ==True :
          print("il s'agit d'un carre")
       else:
          print("Il ne s'agit pas d'un carre")







    
          
          
          
       