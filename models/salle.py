class Salle:
    def __init__(self, codee,descriptions,categorie, capacite):
        self.codee = codee
        self.descriptions = descriptions
        self.categorie = categorie
        self.capacite = capacite
    def afficher_infos(self):
        return (
            f"codee: {self.codee}\n"
            f"descriptions: {self.descriptions}\n"
            f"categorie: {self.categorie}\n"
            f"capacite: {self.capacite}\n"
        )
