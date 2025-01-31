
import datetime
import json
from SDD.File.File import File
from composant.Box import Box
from composant.VisuelImportation import VisuelImportation
import os


class Data :
    """ Class permettant la gestion des données
    Auteur: Nila GIRAUD

    Gestion d'erreur
    Importation
        """

    def __init__(self) :
        self.tab = []   
        self.indiceErreurs = []
        self.box = Box()
        self.visuel = VisuelImportation()
    
    def estCorrect(self,tabInformations, toutRegarder = False) : 
        """ Vérification que les informations de la tâche sont conformes
        Auteur : Nila GIRAUD

        :param tabInput: Tableau des informations
        :type tabInput: tableau de str
        :param toutRegarder: Saboir si toutes les valeurs doivent être non null (cas de l'ajout de données)
        :type toutRegarder : boolean
        :return : estOk qui est null si toutes les informations sont valides
        :rtype : une File
        """
        estOk = File() 
        valeurNull = False 

        if tabInformations[0] != "" : 
            if len(tabInformations[0])  > 50 : 
                estOk.enfiler("le titre |" + tabInformations[0] + "| est trop long de " + str((len(tabInformations[0]) - 25)) + " caractères | max 50") 
        else :
            if toutRegarder and not valeurNull : 
                estOk.enfiler("Pas de valeurs vides") 
                valeurNull = True 

        if tabInformations[1] != "" : 
            if len(tabInformations[1]) > 300 : 
                estOk.enfiler("la description est trop long de " + str(len(tabInformations[1]) - 100) + " caractères | max 300") 
        else :
            if toutRegarder and not valeurNull : 
                estOk.enfiler("Pas de valeurs vides") 
                valeurNull = True 

        if tabInformations[2] != "" : 
            if len(tabInformations[2]) > 20 : 
                estOk.enfiler("le nom |" + tabInformations[2] + "| est trop long de " + str(len(tabInformations[2]) - 15) + " caractères | max 15") 
        else :
            if toutRegarder and not valeurNull : 
                estOk.enfiler("Pas de valeurs vides") 
                valeurNull = True 
        
        if tabInformations[3] != "" : 
            if str(tabInformations[3]).isdigit() : 
                if int(tabInformations[3]) > 10 or int(tabInformations[3]) < 0 :  
                    estOk.enfiler("Priorité | "+ str(tabInformations[3])  + " | en dehors de la plage") 
            else :
                estOk.enfiler("La Priorité doit être un nombre (entre 1 et 10)") 
        else :
            if toutRegarder and not valeurNull :
                estOk.enfiler("Pas de valeurs vides") 
                valeurNull = True 

        if tabInformations[4] != "" : 
            try:
                datetime.datetime.strptime(tabInformations[4], "%Y-%m-%d") 
            except ValueError: 
                estOk.enfiler("La date est invalide") 
        else :
            if toutRegarder and not valeurNull : 
                estOk.enfiler("Pas de valeurs vides") 
                valeurNull = True

        return estOk
    
    
    def importer(self, fichier) : 
        """ Importation d'un fichier json depuis le dossier ./json
        Auteur : Nila GIRAUD

        :param fichier: Nom du fichier json
        :type fichier: str
        """
        indice = 0 
        self.tab = []   
        self.indiceErreurs = [] 

        path = os.getcwd() 

        try :
            with open(path + "/data/json/" + fichier, "r", encoding="utf-8") as f : 
                data = json.load(f)
                for dico in data :
                    try :
                        tabTest = self.tabTest(dico)  
                        if self.estCorrect(tabTest,True).estVide() :
                            self.tab.append(dico) 
                        else :
                            self.indiceErreurs.append(indice) 
                    except :
                        self.indiceErreurs.append(indice) 
                    
                    indice = indice + 1 

            self.visuel.barreProgression(30)  
            print((self.visuel.ImportMessage(self.tab, self.indiceErreurs)))     
        except FileNotFoundError : 
            self.box.boxMessage("Le fichier n'a pas été trouvé. Vérifiez le chemin du fichier.")
        except Exception as e: 
            self.box.boxMessage(f"Une erreur est survenue : {e}") 

    def tabTest(self, dico) :
        """ Tableau de vérification de clé
        Auteur : Nila GIRAUD

        :param dico: Dictionnaire à regarder
        :type dico: dictionnaire
        :return : le tableau des valeurs sinon raise une exception en cas de mauvaise clé
        :rtype : un tableau
        """
        tab = []
        clés_voulu = ["titre", "description","responsable","priorite","date_limite"]  # les clés souhaitées

        for cle in clés_voulu:
            if cle not in dico:
                raise Exception

        tab.append(dico["titre"])
        tab.append(dico["description"])
        tab.append(dico["responsable"])
        tab.append(dico["priorite"])
        tab.append(dico["date_limite"])
        return tab


    

    





