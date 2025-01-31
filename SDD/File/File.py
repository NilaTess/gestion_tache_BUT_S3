from SDD.File.ListeDoubleChaine import ListeDoubleChaine

class File :

    def __init__(self) :
        self.file = ListeDoubleChaine() 
        self.taille = 0 
    
    def enfiler(self, data) :
        if self.file.sommet is None : 
            self.file.sommet  = self.file.Noeud(data) 
            self.file.dernier = self.file.sommet 
        else : 
            self.file.dernier.suivant = self.file.Noeud(data) 
            self.file.dernier.suivant.precedent = self.file.dernier 
            self.file.dernier = self.file.dernier.suivant 

        self.taille = self.taille + 1 

    def defiler(self) :
        if self.file.sommet is not None : 
            data = self.file.sommet.data 
            self.file.sommet = self.file.sommet.suivant 
            self.taille = self.taille - 1 
        return data
        

    def estVide(self) :
        return self.file.sommet is None
    
    def lireSommet(self) :
        return self.file.sommet.data
    
    def lireDernier(self) :
        return self.file.dernier.data
    
    def lireTaille(self) :
        return self.taille

    def __str__(self) :
        if self.file.sommet is None :
            return "[]"
        nouvelle = File()
        tab = []
        while self.file.sommet :
            nouvelle.enfiler(self.file.sommet.data)
            tab.append(self.file.sommet.data)
            self.defiler()

        while nouvelle.file.sommet :
            self.enfiler(nouvelle.file.sommet.data)
            nouvelle.defiler()

        string = "[ "
        i = 0
        while i < self.taille - 1 :
            string = string + str(tab[i]) + ", "
            i = i + 1
        string = string  + str(tab[i]) + " ]"

        return string
    

    def maxStr(self) :
        temp_file = File()
        max = len(self.file.sommet.data)

        while self.file.sommet : 
            temp_file.enfiler(self.file.sommet.data)
            if len(self.file.sommet.data) > max :
                max = len(self.file.sommet.data)
            self.defiler()
        
        while temp_file.file.sommet :
            self.enfiler(temp_file.file.sommet.data)
            temp_file.defiler()
        
        return max


    









