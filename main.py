from models.salle import Salle
from data.dao_salle import DataSalle

dao = DataSalle()
connexion = dao.get_connection()
print("Connexion reussie")
connexion.close()

s1 = Salle("1000","salle chimie", "Genie de procedes",30)
dao.insert_salle(s1)
print("salle ajoutée")

s1_modifiee = Salle("1000","salle science humaine", "Scientifique",20)
dao.update_salle(s1_modifiee)
print("salle modifiée")

salle = dao.get_salle("1000")
if salle:
    print(salle.afficher_infos())

liste = dao.get_salles()
for s in liste:
    print(s.afficher_infos())
    print("_" * 30)

dao.delete_salle("1000")
print("Salle supprimée")
