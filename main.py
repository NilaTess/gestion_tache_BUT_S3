from SDD.Pile.Pile import Pile
from SDD.Liste.ListeChainee import MaListeChainee
from composant.Menu import Menu
from data.data import Data



def main() :

    # Condition de sortie
    sortir = False

    # Importation de la base de donnée
    data = Data()
    data.importer("fichierdeBase.json") # importation du fichier de base
    # # Maitenant le but est d'importer les données dans la liste chainée ( La première étape étant un sas de données)
    liste = MaListeChainee()
    liste.ajouterAll(data.tab)

    pile = Pile()

    # Création de l'objet menu 
    menu = Menu()

    # Menu principale
    menu.choixMenuPrincipal(liste,pile,data)  

main()




