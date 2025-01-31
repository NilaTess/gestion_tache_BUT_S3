import random
import sys
import time
from composant.Box import Box


class VisuelImportation :
    """ Visuel autour de l'importation
        Auteur : Nila GIRAUD

        :param tabInput: Tableau des informations
        :type tabInput: tableau de str
        :param toutRegarder: Saboir si toutes les valeurs doivent être non null (cas de l'ajout de données)
        :type toutRegarder : boolean
        :return : estOk qui est null si toutes les informations sont valides
        :rtype : une File
        """

    def __init__(self):
        self.box = Box()

    def barreProgression(self,total):
        """ Barre de chargmement de l'importation
        Auteur : Nila GIRAUD

        :param total: valeur de repaire de temps
        :type tab: int

        """
        self.box.boxMessage("Gestion de tâches")  # taille*12 + 4
        self.box.boxMessage("Importation des données...") # taille*12 + 4

        for i in range(total + 1):
            percent = (i / total) * 100
            bar = "█" * i + "-" * (total - i)
            sys.stdout.write(f"\r[{bar}] {percent:.2f}%")
            sys.stdout.flush()
            time.sleep(0.01)
        print()

    def afficherIndiceErreurs(self, indiceErreurs) : 
        """ Affichage de l'indice des donnees en erreurs durant l'importation des donnés
        Auteur : Nila GIRAUD

        :param indiceErreurs: indices des erreurs dans le fichier json importer
        :type indiceErreurs: tableau de int

        """
        message = "[ "
        for i in range(len(indiceErreurs) ) : 
            if(i == len(indiceErreurs) - 1) : 
                message = message + str(indiceErreurs[i]+1) + " ]"
            else :
                message = message + str(indiceErreurs[i]+1) + ", "
        return message

    def ImportMessage(self, tab, indiceErreurs) :
        """ Affichage du message après l'importation des données
            Prise en compte des erreurs et indice de celles-ci
        Auteur : Nila GIRAUD

        :param tab: tableau de données valides
        :type tab: tableau
        :param indiceErreurs: indices des erreurs dans le fichier json importer
        :type indiceErreurs: tableau de int

        """
        if len(indiceErreurs) == 0 :
            messageErreurs = " Toutes les tâches ont étés importés" 
        elif len(indiceErreurs) == 1 : 
            messageErreurs = str(len(indiceErreurs)) + " tâche n'a pas pu être importé, c'est la tâche : " + self.afficherIndiceErreurs(indiceErreurs)
        elif tab == [] :
            messageErreurs = "Aucunes données n'a peu être importées"
        else :
            messageErreurs = str(len(indiceErreurs)) + " tâches n'ont pas pu être importées, ce sont les tâches : " + self.afficherIndiceErreurs(indiceErreurs)
        return messageErreurs

    