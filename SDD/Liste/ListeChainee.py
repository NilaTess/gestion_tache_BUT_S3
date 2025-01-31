import re
from SDD.File.File import File
from SDD.Liste.Maillon import MonMaillon
from composant.Box import Box

class MaListeChainee:
    def __init__(self) :
        self.tete = None
        self.taille = 0
        self.tri = None
        self.box = Box()

    def ajouterAll(self,tableau) :
        for i in range(len(tableau)) :  
            self._ajouter(tableau[i]) 
    
    def _ajouter(self, dictionnaire) :
        if self.tete is None:                     
            self.tete = MonMaillon(dictionnaire)  
        else:
            maillon = self.tete                
            for i in range(self.taille - 1) :  
                maillon = maillon.suivant      
            maillon.suivant = MonMaillon(dictionnaire) 
        self.taille = self.taille + 1 

    def inserer(self, dictionnaire) : 
        if self.tri is None :
            self._ajouter(dictionnaire)
        else : 
            if self.tete is None:
                self.tete = MonMaillon(dictionnaire)
            else :
                maillon = self.tete  
                precedent = None
                noeud = MonMaillon(dictionnaire)
                while (dictionnaire[self.tri] > maillon.valeur[self.tri]) or maillon.suivant is None:
                    precedent = maillon
                    maillon = maillon.suivant
                if maillon.suivant == None :
                    self._ajouter(dictionnaire)
                if maillon == self.tete :
                    self.tete = noeud
                    self.tete.suivant = maillon
                else :
                    precedent.suivant = noeud
                    noeud.suivant = maillon          
    
    def supprimerIndice(self, indice):
        if self.tete is not None:
            maillon = self.tete
            maillonPrecedent = None
            if indice <= self.taille - 1 : 
                for i in range(indice) :
                    maillonPrecedent = maillon
                    maillon = maillon.suivant
                if maillon is self.tete:
                        self.tete = self.tete.suivant
                else:
                    maillonPrecedent.suivant = maillon.suivant
            else : 
                print("L'index : " + indice + "est hors de la plage")
            self.taille = self.taille - 1

    def supprimerValeur(self, dictionnaire) :
        if self.tete is not None:
            maillon = self.tete
            maillonPrecedent = None
            while maillon is not None and maillon.valeur != dictionnaire : 
                    maillonPrecedent = maillon
                    maillon = maillon.suivant
            if maillon is not None : 
                if maillon.suivant is not None :
                    if maillon == self.tete :
                        self.tete = self.tete.suivant
                    else :
                        maillonPrecedent.suivant = maillon.suivant
                else :
                   maillonPrecedent.suivant = None 
                self.taille = self.taille - 1
            else : 
                print("Pas d'occurence de ce type")

    def indice(self, clé, valeur) :
        maillon = self.tete
        while maillon is not None and maillon.valeur[clé] != valeur  : 
                maillon = maillon.suivant
        if maillon is not None : 
            return maillon.valeur
        else : 
            return None

    def afficherClé(self) :
        tabCle = ["1. titre","2. descpription","3. responsable","4. priorite","5. date_limite"]
        self.box.boxMessageMultiple(tabCle)

        
    def afficherliste(self):
        if self.tete is not None :
            maillon = self.tete
            index = 1
            for i in range(self.taille) :
                dictionnaire = maillon.valeur
                self.box.boxMessage(str(index) + ' - ' + dictionnaire["titre"])
                print()  
                maillon = maillon.suivant
                index = index + 1
        else : 
            self.box.boxMessage("aucune tâches encore crées")


    def __str__(self) :
        if self.tete is not None :
            maillon = self.tete
            for i in range(self.taille) :
                dictionnaire = maillon.valeur
                tab = []
                tab.append("Description : " + dictionnaire["description"])
                tab.append("Responsable : " + dictionnaire["responsable"])
                tab.append("Priorité : " + str(dictionnaire["priorite"]))
                tab.append("Date butoire : " + dictionnaire["date_limite"]) # strftime('%Y-%m-%d')

                self.box.boxTitre(dictionnaire["titre"],tab)
                maillon = maillon.suivant
        else : 
            self.box.boxMessage("aucune tâches encore crées")

    def est_vide(self):
        if self.tete == None:
            return True
        else:
            return False
        
    def recuperer(self, index):
        maillon = self.tete

        if index  < self.taille  : 
            for i in range(index) :
                maillon = maillon.suivant
        else : 
            return 0
        return maillon.valeur
    
    def recupererMaillon(self, index):
        maillon = self.tete

        if index  < self.taille  : 
            for i in range(index) :
                maillon = maillon.suivant
        else : 
            return 0
        return maillon
        
    def longueur(self):
        return self.taille
    
    def convertirEnDictionnaire(self,file,data) : 
        """Convertir les données entré par l'utilisateur en un dictionnaire
        Auteur: Nila GIRAUD

        :param file: une file contenant les input de la personne
        :type file: file
        :param data: Object de la classe data, pour la manipulation de données
        :type data: Data
        :return: file ou dictionnaire
        :rtype: file ou dictionnaire
        """
        tabInput = []
        for i in range(5) :
            tabInput.append(file.defiler()) 

        file = data.estCorrect(tabInput,True)

        if(file.estVide()) :
            dictionnaire = {
            "titre" : tabInput[0],
            "description" : tabInput[1],
            "responsable" : tabInput[2],
            "priorite" : int(tabInput[3]),
            "date_limite" : tabInput[4],
        }
            return dictionnaire
        else :
            return file

    def modifier(self, dico, clé, valeur, data) :
        """Modifier l'information d'un champs depuis sa clé
        Auteur: Nila GIRAUD

        :param dico: Tache selectionnée par l'utilisateur 
        :type dico: dictionnaire
        :param clé: Clé du champs de la valeur à modifier
        :type clé: str
        :param valeur: Valeur de la modification
        :type valeur: str
        :param data: Object de la classe data, pour la manipulation de données
        :type data: Data
        :return: file 
        :rtype: file ou None
        """  
        file = File()
        if clé in dico.keys() :
            tableau = [""] * 5
            indexClé = list(dico.keys()).index(clé)
            tableau[indexClé] = valeur
            if data.estCorrect(tableau).estVide() :
                dico[clé] = valeur
                return file
            else :
                return data.estCorrect(tableau)
        else :
            return file

    def _permuter(self, index1, index2):
        if index1 != index2 and index1 < self.taille and index2 < self.taille and index1 >= 0 and index2 >= 0:
            element1 = self.recupererMaillon(index1)
            elementAvant1 = self.recupererMaillon(index1 - 1)
            element2 = self.recupererMaillon(index2)
            elementAvant2 = self.recupererMaillon(index2 - 1)

            if element1 == self.tete:
                elementAvant2.suivant = element1
                self.tete = element2
            elif element2 == self.tete:
                elementAvant1.suivant = element2
                self.tete = element1
            else:
                elementAvant1.suivant = element2
                elementAvant2.suivant = element1

            tmp = element1.suivant
            element1.suivant = element2.suivant
            element2.suivant = tmp

    def trier(self, typeTri):
        ii = self.taille - 1
        while ii > 0:
            jj = 0
            while jj < ii:
                if self.recuperer(jj)[typeTri] > self.recuperer(jj + 1)[typeTri]:
                    self._permuter(jj, jj + 1)
                jj += 1
            ii -= 1
        self.tri =  typeTri

    def rechercher(self, element, categorie):
        nouvelleListe = MaListeChainee()
        ii = 0
        while ii < self.taille:
            regEx = str(element)+"+"
            if re.search(regEx , str(self.recuperer(ii)[categorie]).lower()):
                nouvelleListe._ajouter(self.recuperer(ii))
            ii += 1
        return nouvelleListe