import random
from composant.Box import Box
from SDD.Pile.ListeChaine import *

class Pile : 

    def __init__(self) :
        self.pile = ListeChaine()
        self.taille = 0
        self.box = Box()

    def empiler(self, data) :
        tempNoeud = self.pile.sommet
        self.pile.sommet = self.pile.Noeud(data)
        self.pile.sommet.suivant = tempNoeud
        self.taille = self.taille + 1
        
        return "Archivage completé"

    
    def depiler(self) :
        sommet = self.pile.sommet
        if self.pile.sommet is not None : 
            self.pile.sommet = self.pile.sommet.suivant   
            self.taille = self.taille - 1 
        return sommet

    def enlever(self, data) : 
        trouver = False
        temp = Pile()
        while not trouver and self.pile.sommet :
            if self.pile.sommet.data == data :
                trouver = True
                self.pile.sommet = self.pile.sommet.suivant
            else :
                temp.empiler(self.pile.sommet.data)
                self.pile.sommet = self.pile.sommet.suivant
                self.taille = self.taille - 1

        while temp.pile.sommet :
            self.empiler(temp.pile.sommet.data)
            temp.pile.sommet = temp.pile.sommet.suivant

        self.taille = self.taille - 1 

    def estVide(self) :
        return self.pile.sommet is None
    
    def sommet(self) :
        return self.pile.sommet.data
    
    def longueur(self) :
        return self.taille
    
    def reverse(self) :
        temp = Pile()
        while self.pile.sommet :
            temp.empiler(self.pile.sommet.data)
            self.depiler()

        while  temp.pile.sommet :
            self.empiler(temp.pile.sommet.data)
            temp.depiler()  

    def __str__(self) :
        if self.pile.sommet is None :
            self.box.boxMessage("Aucune valeures dans l'archive")
        else :
            nouvelle = Pile()
            tab = []
            while self.pile.sommet :
                nouvelle.empiler(self.pile.sommet.data)
                tab.append(self.pile.sommet.data["titre"])
                self.depiler()

            while nouvelle.pile.sommet :
                self.empiler(nouvelle.pile.sommet.data)
                nouvelle.depiler()
            
            self.reverse()

            self.box.boxMessageMultiple(tab)


        







    
        
