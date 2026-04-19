from models.salle import Salle
from data.dao_salle import DataSalle
from services.service_salle import ServiceSalle
from views.view_salle import ViewSalle

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

service =ServiceSalle()
s1 = Salle("2000","salle Anglais", "Langues",35)
resultat, message = service.ajouter_salle(s1)
print(message)
resultat,message = service.modifier_salle(Salle("2000","salle Francais","Langues",35))
print(message)

salle = service.rechercher_salle("2000")
if salle:
    print(salle.afficher_infos())
for s in service.recuperer_salle():
    print(s.afficher_infos())
    print("_" * 35)
resultat,message = service.supprimer_salle("2000")
print(message)
app = ViewSalle()
app.mainloop()
