from SDD.File.File import File
from composant.Box import Box
from data.data import Data

class Formulaire :
    """ Formulaire soumis à l'utilisateur pour récupérer les données de modifications
        Auteur : Nila GIRAUD

        Supprimer
        Ajouter
        Modifier
        Récuperer indice
        Récuperer clé
        Recherche
        """
    def __init__(self) :
        self.box = Box()
        self.data = Data()

    
    def formulaireSupprimer(self,liste) :
        """ Formulaire de suppression de données, demande de l'indice
        Auteur : Nila GIRAUD

        :param liste: Liste des tâches
        :type liste: str
        """
        indice = self.formulaireIndice(liste)
        if indice is not None :
            liste.supprimerIndice(indice)

    def formulaireAjouter(self) :
        """ Formulaire d'ajout des données,  demande des informations de la tâches (input)
        Auteur : Nila GIRAUD

        :return : Une file
        :rtype : file contenant des str
        """
        file = File()

        tab = []
        tab.append("Titre de la tâche")
        tab.append("Description de la tâche")
        tab.append("Responsable de la tâche")
        tab.append("Priorité de la tâche entre 1 et 10")
        tab.append("Date limite de la tâche | Format : AAAA-MM-JJ")

        for i in range(len(tab)) :
            self.box.boxMessage(tab[i])
            file.enfiler(input(">>> "))
        return file
    
    def formulaireModifier(self, liste,indice) :
        """ Formulaire de modification d'un champ d'une tâche, selection de la clé
        Auteur : Nila GIRAUD

        :param liste: Liste des tâches
        :type liste: str
        :param indice: Indice de la tâche dans la liste
        :type indice: int
        """
        tabCle = ["titre","descpription","responsable","priorite","date_limite"]

        sortir = False

        while not sortir :

            print("r- Retour")
            choix = input("Entrez votre choix (1-r) >>> ").lower().strip()

            if choix == "r":
                sortir = True
            elif choix.isdigit() and (int(choix)-1) <= (len(tabCle)) and (int(choix)-1) >= 0  :
                valeur = self.formulaireCle(tabCle[int(choix)-1])
                file = File()
                file = liste.modifier(liste.recuperer(indice), tabCle[int(choix)-1], valeur,self.data)
                if not file.estVide() :
                    self.box.boxErreur(file)
                sortir = True
            else :
                print("Erreur dans l'input, veuillez réessayer")       

    def formulaireIndice(self, liste) :
        """ Formulaire de selection d'une tâche
        Auteur : Nila GIRAUD

        :param liste: Liste des tâches
        :type liste: str
        :return : l'indice de la tâche
        :rtype : int ou None
        """
        if liste.longueur() != 0 :
            sortir = False
            print("r- Retour")
            while not sortir :

                choix = input("Entrez votre choix (1-r) >>> ").lower().strip()

                if choix == "r":
                    sortir = True
                
                elif choix.isdigit() and (int(choix)-1) < liste.longueur() and (int(choix)-1) >= 0 :
                    return int(choix) - 1
                else :
                    print("Erreur dans l'input, veuillez réessayer")
            return None

    def formulaireCle(self,clé) :
        """ Formulaire de selection d'une tâche
        Auteur : Nila GIRAUD

        :param liste: Liste des tâches
        :type liste: str
        :return : l'indice de la tâche
        :rtype : int ou None
        """   
        self.box.boxMessage(clé)
        valeur = input(">>> ").lower().strip()
        return valeur
    
    def formulaire_recherche(self, categorie, liste):
        """ Formulaire de selection d'une tâche
        Auteur : Nila GIRAUD
        
        :param liste: Liste des tâches
        :type liste: str
        :return : l'indice de la tâche
        :rtype : int ou None
        """ 
        self.box.boxMessage("Indiquez votre recherche")
        recherche = input(">>> ").lower().strip()
        print(recherche)
        listeRecherche = liste.rechercher(recherche, categorie)
        listeRecherche.__str__()




        
