import Zombie
import Survivor
import Livraison
import random
class AireDeJeu():
    def __init__(self, parent):
        self.parent = parent
        self.livraison = Livraison.Livraison()
        self.uniteEnJeu = {}
        self.survivant = {}
        self.caisse = {}
        self.caisseAttribuer = {}
        self.creerSurvivor()
        pos = []
        for i in range(10):
            porteDepart = random.randrange(1,5)
            edgeX = random.randrange(1,10)
            edgeY = random.randrange(1,10)
            if porteDepart == 1:
                pos = [755+edgeX,250+edgeY]
            elif porteDepart == 2:
                pos =[755+edgeX,350+edgeY]
            elif porteDepart == 3:
                pos =[35+edgeX,250+edgeY]
            elif porteDepart == 4:
                pos =[35+edgeX,350+edgeY]
            self.uniteEnJeu[i] = Zombie.Zombie(pos, porteDepart)
  
    def creerSurvivor(self):
        self.survivant["Greg"] = Survivor.Survivor([375,300], self, "Greg")
        self.survivant["Luc"] = Survivor.Survivor([425,300],self, "Luc")
        
    def larguerCaisse(self):
        self.caisse = self.livraison.envoyerPetiteCaisse()
    
class GrandeBase():
    pass

class PetiteBase():
    pass