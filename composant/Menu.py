import os
from composant.Box import Box
from composant.Formulaire import Formulaire
from data.data import Data

class Menu : 
    """ Menu | interface utilisateur
    Auteur: Nila GIRAUD

    Primaire
        Principale
        Afficher
        Modifier
        données
    Secondaire
        Tri
        Recherche
        """

    def __init__(self):
        self.box = Box()
        self.formulaire = Formulaire()

    # AFFICHAGE

    def afficherMenuPrincipale(self) :
        """Affichage Menu principale
        Auteur: Nila GIRAUD

            """
        tab =[]
        tab.append("1. Affichage")      
        tab.append("2. Modification")
        tab.append("3. Données")                       
        tab.append("q. Quitter")      
        self.box.boxTitre("Menu Principal", tab)

    def afficherMenuAffichage(self) :
        """Affichage Menu d'affichage
        Auteur: Nila GIRAUD

            """
        tab =[]                                                                                                                 
        tab.append("1. Afficher les tâches")                                                                    
        tab.append("2. Tri des tâches     ")                       
        tab.append("3. Recherche tâche    ")
        tab.append("4. Afficher l'archive ")   
        tab.append("r. Retour             ")                             
        self.box.boxTitre("Affichage", tab)

    def afficherMenuModification(self) :
        """Affichage Menu de modification
        Auteur: Nila GIRAUD

            """ 
        tab =[]
        tab.append("1. Ajouter                      ")      
        tab.append("2. Supprimer                    ")            
        tab.append("3. Modifier                     ")
        tab.append("4. Archiver                     ")
        tab.append("5. Désarchiver                  ")             
        tab.append("r. Retour                       ")      
        self.box.boxTitre("Modification", tab)

    def afficherMenuDonnees(self) :
        """Affichage Menu donnes
        Auteur: Nila GIRAUD

            """
        tab =[]
        tab.append("1. Importer un fichier json (depuis le dossier /json dans /data )   ")                       
        tab.append("r. Retour                  ")      
        self.box.boxTitre("Données", tab)

    def afficherMenuTri(self) :
        """Affichage Sous Menu de tri
        Auteur: Nila GIRAUD

            """
        tab =[]
        tab.append("1. Par Titre")      
        tab.append("2. Par Responsable")
        tab.append("3. Par Priorité Croissante")
        tab.append("4. Par Date")
        tab.append("r. Retour")      
        self.box.boxTitre("Tris", tab)

    def afficherMenuRecherche(self) :
        """Affichage Sous Menu de recherche
        Auteur: Nila GIRAUD

            """
        tab =[]
        tab.append("1. Par Titre")      
        tab.append("2. Par Responsable")
        tab.append("3. Par Priorité")
        tab.append("4. Par Date")
        tab.append("r. Retour")      
        self.box.boxTitre("Recherche", tab)

    # CHOIX MENU

    def choixMenuPrincipal(self,liste,pile,data) :
        """Menu principale
        Auteur: Nila GIRAUD

        :param liste : Liste de tâches
        :type liste : tableau de dictionnaire
        :param pile : Liste de tâches
        :type pile : Pile de dictionnaire
        :param data : Objet mertmettant la gestion de données
        :type data : Data
        """
        sortir = False 
        while not sortir :

            self.afficherMenuPrincipale()
            choix = input("Entrez votre choix (1-q) >>> ").lower().strip()

            match choix : 
                case "1" :
                    self.effacer_terminal()
                    self.choixMenuAffichage(liste,pile)
                    self.effacer_terminal()
                case "2" :
                    self.effacer_terminal()
                    self.choixMenuModification(liste,data,pile)
                    self.effacer_terminal() 
                case "3" :
                    self.effacer_terminal()
                    self.choixMenuDonnees(liste)
                    self.effacer_terminal() 
                case "q" :
                        sortir = True
                        self.partir()
                case _:
                    self.effacer_terminal()
                    print("Erreur dans l'input, veuillez réessayer")
    
    def choixMenuAffichage(self,liste,pile) :
        """Menu Affichage
        Auteur: Nila GIRAUD

        :param liste : Liste de tâches
        :type liste : tableau de dictionnaire
        :param pile : Liste de tâches
        :type pile : Pile de dictionnaire
        :param data : Objet mertmettant la gestion de données
        :type data : Data
        """
        sortir = False

        while not sortir : 

            self.afficherMenuAffichage()
            choix = input("Entrez votre choix (1-r) >>> ").lower().strip()

            self.effacer_terminal()
            match choix :
                case "1" :
                    liste.__str__()
                    self.appuyerContinuer() 
                    self.effacer_terminal()
                case "2" :
                    self.effacer_terminal()
                    self.choixMenuTri(liste)
                case "3" :
                    self.effacer_terminal()
                    self.choixMenuRecherche(liste)
                case "4" :
                    pile.__str__()
                    self.appuyerContinuer() 
                    self.effacer_terminal()
                case "r" :
                    sortir = True
                case _:
                    print("Erreur dans l'input, veuillez réessayer")
    
            

    def choixMenuModification(self, liste, data , pile) : 
        """Menu Modification
            Auteur: Nila GIRAUD

            :param liste : Liste de tâches
            :type liste : tableau de dictionnaire
            :param pile : Liste de tâches
            :type pile : Pile de dictionnaire
            :param data : Objet mertmettant la gestion de données
            :type data : Data
            """
        sortir = False
        
        while not sortir :

            self.afficherMenuModification()
            choix = input("Entrez votre choix (1-r) >>> ").lower().strip() 

            self.effacer_terminal()
            match choix :
                case "1" :
                    file = self.formulaire.formulaireAjouter()
                    resultat = liste.convertirEnDictionnaire(file,data)

                    if isinstance(resultat, dict): 
                        liste.inserer(resultat)
                        self.box.boxMessage("Ajouté avec succès !")
                    else :
                        self.box.boxErreur(resultat) 
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "2" :
                    if liste.longueur() != 0 : 
                        self.effacer_terminal()
                        liste.afficherliste()
                        self.formulaire.formulaireSupprimer(liste)
                    else :
                        liste.afficherliste()
                        self.appuyerContinuer()
                    self.effacer_terminal()
                case "3" :
                    liste.afficherliste()
                    if liste.longueur() != 0 :
                        indice = self.formulaire.formulaireIndice(liste)
                        if indice is not None :
                            liste.afficherClé()
                            self.formulaire.formulaireModifier(liste, indice)
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "4" :
                    liste.afficherliste()
                    if liste.longueur() != 0 :
                        indice = self.formulaire.formulaireIndice(liste) 
                        if indice is not None :
                            self.box.boxMessage(pile.empiler(liste.recuperer(indice)))
                            liste.supprimerIndice(indice)
                    self.appuyerContinuer()
                    self.effacer_terminal() 
                case "5" :
                    if pile.longueur() != 0 :
                        noeud = pile.depiler().data
                        self.box.boxMessage("Désarchivage de | " + noeud["titre"] + " |")
                        liste.inserer(noeud)  
                        liste.afficherliste() 
                    else : 
                        pile.__str__()
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "r" :
                    sortir = True
                case _:
                    print("Erreur dans l'input, veuillez réessayer")

    def choixMenuDonnees(self,liste) :
        """Menu 
            Auteur: Nila GIRAUD

            :param liste : Liste de tâches
            :type liste : tableau de dictionnaire
            """
        sortir = False

        while not sortir : 

            self.afficherMenuDonnees()
            choix = input("Entrez votre choix (1-r) >>> ").lower().strip()

            self.effacer_terminal()
            match choix :
                case "1" :
                    data = Data()
                    fichier = input("Nom du fichier dans /json >>> ")
                    data.importer(fichier)
                    if len(data.tab) is not None :
                        data.afficherIndiceErreurs()
                        liste.ajouterAll(data.tab)
                    self.appuyerContinuer() 
                    self.effacer_terminal() 
                case "r" :
                    sortir = True
                case _:
                    print("Erreur dans l'input, veuillez réessayer")


    # CHOIX SOUS MENUS

    def choixMenuTri(self, liste):
        sortir = False
        
        while not sortir :
            self.afficherMenuTri()
            choix = input("Entrez votre choix (1-r) >>> ").lower().strip()

            self.effacer_terminal()
            match choix:
                case "1":
                    liste.trier("titre")
                    liste.__str__()
                    self.appuyerContinuer() 
                    self.effacer_terminal()
                case "2":
                    liste.trier("responsable")
                    liste.__str__()
                    self.appuyerContinuer() 
                    self.effacer_terminal()
                case "3":
                    liste.trier("priorite")
                    liste.__str__()
                    self.appuyerContinuer() 
                    self.effacer_terminal()
                case "4":
                    liste.trier("date_limite")
                    liste.__str__()
                    self.appuyerContinuer() 
                    self.effacer_terminal()
                case "r":
                    sortir = True
                case _:
                    print("Erreur dans l'input, veuillez réessayer")

    def choixMenuRecherche(self, liste):
        sortir = False
        
        while not sortir :
            self.afficherMenuRecherche()
            choix = input("Entrez votre choix (1-r) >>> ").lower().strip()
            self.effacer_terminal()
            match choix:
                case "1":
                    self.formulaire.formulaire_recherche("titre", liste)
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "2":
                    self.formulaire.formulaire_recherche("responsable", liste)
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "3":
                    self.formulaire.formulaire_recherche("priorite", liste)
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "4":
                    self.formulaire.formulaire_recherche("date_limite", liste)
                    self.appuyerContinuer()
                    self.effacer_terminal()
                case "r":
                    sortir = True
                case _:
                    print("Erreur dans l'input, veuillez réessayer")

    # MODIFICATION TERMINAL   

    def appuyerContinuer(self) :
        """Input d'attente pour continuer, attendre que l'utilisateur prenne considération des informations
            Auteur: Nila GIRAUD

            """ 
        print("\n           >>> Appuyez pour continuer\n")
        input()

    def partir(self) : 
        """Message lors de l'arret de l'application

            """ 
        self.box.boxMessage("À une prochaine fois !")


    def effacer_terminal(self):
        """Efface le terminal 
            Auteur: Nila GIRAUD

            """ 
        os.system('cls' if os.name == 'nt' else 'clear')
