class Voiture:
    def __init__(self, couleur, marque, modele):
        self.couleur = couleur
        self.marque = marque
        self.modele = modele
        
    def demarrer(self):
        return "wroom!"