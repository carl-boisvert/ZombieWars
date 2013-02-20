from Tkinter import *

class Vue():
    def __init__(self,parent):
        self.root=Tk()
        self.parent = parent
        self.root.title("Zelda Like")
        self.positionY = 0
        self.positionX = 400
        self.positionXGame = 800
        self.positionYGame = 300
        self.imageTitre = 0
        self.boucle()
        self.choix = "Commencer"

        
    def boucle(self):
        self.menu = Frame(self.root,width = 800, height = 600)
        self.menu.grid(row = 0, column = 0)
        self.canevas = Canvas(self.menu, width = 800, height = 600)
        self.canevas.grid(row = 0, column = 0)
        self.canevas.create_rectangle(0,0,800,600, fill="White")
        #self.canevas.bind("<Button-1>", self.drag)
        self.menuPrincipal()
        #self.animationHautNom()
        
     
    def menuPrincipal(self):
        self.imageTitre = PhotoImage(file="images/zombiewars.gif")
        self.canevas.create_image(400,150, image=self.imageTitre, tags="titre")
        self.canevas.create_text(400,250, text="Commencer une partie", tags="commencer")
        self.canevas.create_text(360,300,text="Quitter", tags="quitter")
        self.canevas.create_rectangle(300,245,310,255, fill="Green", tags="square")
        self.canevas.bind('<Key>', self.choixMenu)
        self.canevas.bind('<Return>', self.choixMenu)
        self.canevas.focus_set()
        self.canevas.update()
        
    def choixMenu(self,e):
        if e.keysym == 'Down':
            self.canevas.delete("square")
            self.canevas.create_rectangle(300,295,310,305, fill="Green", tags="square")
            self.choix = "Quitter"
        elif e.keysym == 'Up':
            self.canevas.delete("square")
            self.canevas.create_rectangle(300,245,310,255, fill="Green", tags="square")
            self.choix = "Commencer"
        elif e.keysym == 'Return':
            if self.choix == "Commencer":
                self.commencerPartie()
            elif self.choix == "Quitter":
                self.root.destroy()
    
    def dessinerSurvivant(self, survivant):
        for i in survivant.keys():
            self.canevas.delete(i)
            self.canevas.create_oval(survivant.get(i).position[0]+5,survivant.get(i).position[1]+5,survivant.get(i).position[0]-5,survivant.get(i).position[1]-5, fill="RED", tags=i)
    
    
    def dessinerZombie(self, dicUnite):
        for i in dicUnite.keys():
            unite = dicUnite.get(i)
            self.canevas.create_rectangle(unite.position[0]+5,unite.position[1]+5,unite.position[0]-5,unite.position[1]-5, fill="Green", tags = i)
    
    def dessinerCaisse(self, tabCaisse):
        self.canevas.delete("Caisse")
        for i in tabCaisse.keys():
            caisse = tabCaisse.get(i)
            print("CAISSE: ", caisse)
            if caisse.grandeur == "Petite":
                print("POSITION: ", caisse.position)
                self.canevas.create_rectangle(caisse.position[0]+5,caisse.position[1]+5,caisse.position[0]-5,caisse.position[1]-5, fill="Blue", tags=("Caisse",caisse.id))
            elif caisse.grandeur == "Moyenne":
                self.canevas.create_rectangle(caisse.position[0]+10,caisse.position[1]+10,caisse.position[0]-10,caisse.position[1]-10, fill="Blue", tags=("Caisse",caisse.id))
            else:
                self.canevas.create_rectangle(caisse.position[0]+15,caisse.position[1]+15,caisse.position[0]-15,caisse.position[1]-15, fill="Blue", tags=("Caisse",caisse.id))
                    
    def commencerPartie(self):
        self.canevas.delete("titre")
        self.canevas.delete("commencer")
        self.canevas.delete("quitter")
        self.canevas.delete("square")
        self.creerAireJeu()
        self.creerBaseEnnemie()
        self.parent.boucleJeu()
    
    def creerBaseEnnemie(self):
        #haut
        self.canevas.create_rectangle(200,0,600,75, fill="Green")
        #droite
        self.canevas.create_rectangle(800,250,725,350, fill="Green")
        #bas
        self.canevas.create_rectangle(200,600,600,525, fill="Green")
        #gauche
        self.canevas.create_rectangle(0,250,75,350, fill="Green")
        
    def creerAireJeu(self):
        #haut
        self.canevas.create_rectangle(350,225,450,235, fill="Green")
        #droite
        self.canevas.create_rectangle(465,250,475,350, fill="Green")
        #bas
        self.canevas.create_rectangle(350,360,450,370, fill="Green")
        #gauche
        self.canevas.create_rectangle(330,250,340,350, fill="Green")
      
    def drag(self,e):
        self.evenement = e
        self.canevas.bind("<B1-Motion>", self.motion)
        
    def motion(self,evt):
        self.canevas.delete("Rect")
        self.canevas.create_rectangle(self.evenement.x,self.evenement.y, evt.x, evt.y, outline="White", tags="Rect")
        self.canevas.bind("<ButtonRelease-1>", self.selection)
        
    def selection(self, evt):
        self.canevas.delete("Rect")
        print("YOU'RE A MOTHERFUCKING BAWSSSSS!!!!!")
        self.selection = self.canevas.find_enclosed(self.evenement.x,self.evenement.y, evt.x, evt.y)
    
    def animHautNom(self):
        self.canevas.delete("nom")
        self.canevas.create_text(self.positionX,self.positionY,text="Carl Boisvert", tags="nom")
        self.positionY = self.positionY + 5
        self.root.after(10, func=self.animationHautNom)
    
    def animationHautNom(self):
        if self.positionY < 300:
            self.animHautNom()
        else:
            self.root.after(1000, func= self.animationSortieNom)
    
    def animationSortieNom(self):
        if self.positionX < 900:
            self.animSortieNom()
        else:
            self.canevas.delete("nom")
            self.positionX = 0
            self.positionY = 300
            self.animationPresent()
            
    def animSortieNom(self):
        self.canevas.delete("nom")
        self.canevas.create_text(self.positionX,self.positionY,text="Carl Boisvert", tags="nom")
        self.positionX = self.positionX + 5
        self.root.after(10, func=self.animationSortieNom)
        
    def animationPresent(self):
        if self.positionX < 400:
            self.animPresent()
        else:
            self.root.after(1000, func= self.animationSortiePresent)
            
    def animPresent(self):
        self.canevas.delete("present")
        self.canevas.create_text(self.positionX,self.positionY,text="Present", tags="present")
        self.positionX = self.positionX + 5
        self.root.after(10, func=self.animationPresent)
        
    def animationSortiePresent(self):
        if self.positionY < 700:
            self.animSortiePresent()
        else:
            self.canevas.delete("present")
            self.positionX = 0
            self.positionY = 300
            self.animationGame()
            
    def animSortiePresent(self):
        self.canevas.delete("present")
        self.canevas.create_text(self.positionX,self.positionY,text="Present", tags="present")
        self.positionY = self.positionY + 5
        self.root.after(10, func=self.animationSortiePresent)
        
    def animationGame(self):
        if self.positionX < 367:
            self.animAn()
        if self.positionXGame > 410:
            self.animGame()
        else:
            self.root.after(1000, func= self.animationSortieGame)
            
    def animAn(self):
        self.canevas.delete("an")
        self.canevas.create_text(self.positionX,self.positionY,text="An", tags="an")
        self.positionX= self.positionX + 5
        
    def animGame(self):
        self.canevas.delete("amnesia")
        self.canevas.create_text(self.positionXGame,self.positionYGame,text="Amnesia Game", tags="amnesia")
        self.positionXGame= self.positionXGame - 5
        self.root.after(10, func=self.animationGame)
        
    def animationSortieGame(self):
        if self.positionY < 700:
            self.animSortieGame()
        else:
            self.canevas.delete("an")
            self.canevas.delete("amnesia")
            self.menuPrincipal()
            
    def animSortieGame(self):
        self.canevas.delete("an")
        self.canevas.create_text(self.positionX,self.positionY,text="An", tags="an")
        self.positionY= self.positionY + 5
        self.canevas.delete("amnesia")
        self.canevas.create_text(self.positionXGame,self.positionYGame,text="Amnesia Game", tags="amnesia")
        self.positionYGame= self.positionYGame - 5
        self.root.after(10, func=self.animationSortieGame)
        
        
        
        