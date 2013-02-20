import Vue
import Modele
import Survivor
import random
class Controleur():
    def __init__(self):
        self.vue = Vue.Vue(self)
        self.modele = Modele.AireDeJeu(self)
        self.commencerPartie()
        self.frame = 0
        self.apparitionCaisse = 99
        
    def commencerPartie(self):
        pass
    
        
    def boucleJeu(self):
        #print self.frame
        #print ("FRAME CAISSE: ",self.apparitionCaisse)
        self.vue.dessinerZombie(self.modele.uniteEnJeu)
        self.vue.dessinerSurvivant(self.modele.survivant)
        for i in self.modele.survivant.keys():
            self.modele.survivant.get(i).prendreDecision()
        if self.frame % 1 == 0:
            self.modele.larguerCaisse()
            #self.apparitionCaisse = random.randrange(100,200)
        self.vue.dessinerCaisse(self.modele.caisse)
        self.frame +=1
        self.vue.root.after(100, self.boucleJeu)
            
        


if __name__ == '__main__':
    cont=Controleur()
    cont.vue.root.mainloop()