
class Box : 
    """ Box pour les différents messages du terminal
        Menu
        Message
        Message d'erreur.s
        """
    
    def __init__(self) :
        pass

    def boxTitre(self, titre, tableau) : 
        """ Box menu avec un titre de section
        :param titre: le titre de la section
        :type titre: str
        :param tableau: Tableau de str avec les fonctionnalités de la section
        :type tableau: tableau
        """
        tailleMax = max(len(element) for element in tableau)

        haut = "\n╭────"
        milieu = "├────"
        bas = "╰────" 
        for i in range (tailleMax) :
            haut = haut + '─'
            milieu = milieu + "─"
            bas = bas + '─'
        
        haut = haut + "╮"
        milieu = milieu + "┤"
        bas = bas + "╯\n"

        print(haut)
        espaces = " " * (tailleMax - len(titre))
        print("│  " + titre + espaces + "  │")
        print(milieu)
        for i in range(len(tableau)) :
            espaces = " " * (tailleMax - len(tableau[i]))
            print("│  " + tableau[i] + espaces + "  │")    
        print(bas)


    def boxMessage(self,message) :
        """ Box pour un message simple
        :param message: le message 
        :type message: str
        """
        haut = "\n╭────"
        bas = "╰────" 
        for i in range (len(message)) :
            haut = haut + '─'
            bas = bas + '─'
        
        haut = haut + "╮"
        bas = bas + "╯\n"

        print(haut)
        print("│  " + message + "  │")
        print(bas)

    def boxMessageMultiple(self,tableau) :
        """ Box pour un message en plusieurs lignes
        :param tableau : les messages
        :type tableau : tableau de str
        """
        tailleMax = max(len(element) for element in tableau)

        haut = "\n╭────"
        bas = "╰────" 
        for i in range (tailleMax) :
            haut = haut + '─'
            bas = bas + '─'
        
        haut = haut + "╮"
        bas = bas + "╯\n"

        print(haut)
        for i in range (len(tableau)) :
            element = tableau[i]
            espaces = " " * (tailleMax - len(element))
            print("│  " + element + espaces + "  │")
        print(bas)

    def boxErreur(self,file) :
        """ Box pour un message d'erreurs (peuvent être sur plusieurs lignes)
        :param file: File contenant le.s message.s d'erreur
        :type file: File contenant des str
        """
        tailleMax = file.maxStr()

        haut = "\n╭──────"
        bas = "╰──────" 
        for i in range (tailleMax) :
            haut = haut + '─'
            bas = bas + '─'
        
        haut = haut + "╮"
        bas = bas + "╯\n"

        print(haut)
        
        for i in range (file.lireTaille()) :
            element = file.defiler()
            espaces = " " * (tailleMax - len(element))
            print("│  • " + element + espaces + "  │")
        print(bas)



    