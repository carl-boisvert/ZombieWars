import Caisse
import random
class Livraison():
    def __init__(self):
        self.nbrTotalCaisse = 0
        self.tabCaisse = {
                            "1":[],
                            "2":[],
                            "3":[],
                            "4":[]
                            }
        self.positionCaisse = {
                                "1":[190,190],
                                "2":[600,190],
                                "3":[190,410],
                                "4":[600,410]
                                }
    
    def envoyerPetiteCaisse(self):
        nbrCaisse = 1
        for i in range(nbrCaisse):
            memeEndroit = False
            self.nbrTotalCaisse += 1
            pos = random.randrange(1,5)
            newCaisse = Caisse.PetiteCaisse(self.nbrTotalCaisse)
            newCaisse.position = self.positionCaisse.get(str(pos))
            self.tabCaisse[str(pos)].append(newCaisse)
            for i in self.tabCaisse.keys():
                position = self.tabCaisse.get(i)
                for caisse in position:
                    if caisse.position == self.positionCaisse.get(str(pos)):
                            memeEndroit = True
            
                #if memeEndroit == True:
                    #self.tabCaisse.get(self.nbrTotalCaisse).position = self.positionCaisse.get(str(pos))
                    #self.tabCaisse.get(self.nbrTotalCaisse).position[0] += random.randrange(1,10)
                    #self.tabCaisse.get(self.nbrTotalCaisse).position[1] += random.randrange(1,10)
        return self.tabCaisse