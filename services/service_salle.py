from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
    def ajouter_salle(self,salle):
        if not salle.codee or not salle.descriptions or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs obligatoire"
        if int(salle.capacite) < 1:
            return False, "la capacite doit etre >= a 1"
        try:
            self.dao_salle.insert_salle(salle)
            return True,"confirmation de l'ajout de salle"
        except Exception as e:
            return False, f"Erreur: {e}"
    def modifier_salle(self,salle):
        if not salle.codee or not salle.descriptions or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs obligatoire"
        if int(salle.capacite) < 1:
            return False, "la capacite doit etre >= a 1"
        try:
            self.dao_salle.update_salle(salle)
            return True,"confirmation de l'ajout de salle"
        except Exception as e:
            return False, f"Erreur: {e}"
    def supprimer_salle(self,codee):
        try:
            self.dao_salle.delete_salle(codee)
            return True,"confirmation de suppression"
        except Exception as e:
            return False, f"Erreur de suppression: {e}"
    def rechercher_salle(self,codee):
        return self.dao_salle.get_salle(codee)
    def recuperer_salle(self):
        return self.dao_salle.get_salles()




