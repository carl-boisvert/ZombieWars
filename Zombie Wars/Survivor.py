import random
from helper import Helper
class Survivor():
    def __init__(self, position, parent, nom):
        self.parent = parent
        self.nom = nom
        self.vie = 30
        self.vitesse = 5
        self.munition = 50
        self.arme = ["Pistolet"]
        self.dicDegatArme = {
                             "Pistolet" : 20,
                             "Machine-Gun": 20
                             }
        self.position = position
        self.cibleDeplacement = None
        self.caisseCible = None
        
    def prendreDecision(self):
        if self.cibleDeplacement != None:
            self.deplacer()
        if self.parent.caisse.__len__() != 0 and self.cibleDeplacement == None:
            print("TROUVE CIBLE", self.nom)
            self.trouverCible()
        elif self.parent.caisse.__len__() == 0:
            self.cibleDeplacement = [400,300]
                
        
    def deplacer(self):
        if Helper.calcDistance(self.position[0],self.position[1],self.cibleDeplacement[0],self.cibleDeplacement[1]) > self.vitesse:
            angle=Helper.calcAngle(self.position[0],self.position[1],self.cibleDeplacement[0],self.cibleDeplacement[1])
            nouvellePosition=Helper.getAngledPoint(angle,self.vitesse,self.position[0],self.position[1])
            self.position[0]=int(round(nouvellePosition[0]))
            self.position[1]=int(round(nouvellePosition[1]))
                
        else:
            self.position = self.cibleDeplacement
            self.cibleDeplacement = None
            if self.caisseCible != None:
                print(self.position)
                print(self.parent.caisse)
                print(self.caisseCible.id)
                self.parent.caisse.pop(self.caisseCible.id)
                self.parent.caisseAttribuer.pop(self.caisseCible.id)
                self.attribuerCaisse()
                self.caisseCible = None
    
    def attribuerCaisse(self):
        self.vie = self.caisseCible.soin
        self.munition = self.caisseCible.munition
        self.arme.append(self.caisseCible.arme)
    
    def trouverCible(self):
        for i in self.parent.caisse.keys():
            if i not in self.parent.caisseAttribuer.keys() and self.caisseCible == None:
                if self.parent.caisse[i] != []:
                    self.cibleDeplacement = self.parent.caisse[i][0].position
                    self.caisseCible = self.parent.caisse[i][0]
                    self.parent.caisseAttribuer[i] = self.parent.caisse[i][0]
        