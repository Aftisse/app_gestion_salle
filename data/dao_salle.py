import json
import os
import mysql.connector
from models.salle import Salle

class DataSalle:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_path = os.path.join(base_dir,"data","config.json")
    def get_connection(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
            auth_plugin="caching_sha2_password"
        )
        return connexion
    def insert_salle(self, salle):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete = """
        INSERT INTO salle (codee,descriptions,categorie,capacite)
        VALUES (%s,%s,%s,%s)
        """
        valeurs =(salle.codee,salle.descriptions,salle.categorie,salle.capacite)
        cursor.execute(requete, valeurs)
        connexion.commit()
        cursor.close()
        connexion.close()
    def update_salle(self, salle):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete = """
        UPDATE salle
        SET descriptions = %s,categorie = %s,capacite = %s
        WHERE codee = %s
        """
        valeurs = (salle.descriptions,salle.categorie,salle.capacite,salle.codee)
        cursor.execute(requete, valeurs)
        connexion.commit()
        cursor.close()
        connexion.close()
    def delete_salle(self, codee):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete = "DELETE FROM salle WHERE codee = %s"
        cursor.execute(requete, (codee,))
        connexion.commit()
        cursor.close()
        connexion.close()
    def get_salle(self, codee):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete = "SELECT codee,descriptions,categorie,capacite from salle WHERE codee = %s"
        cursor.execute(requete, (codee,))
        results = cursor.fetchone()
        cursor.close()
        connexion.close()
        if results:
            return Salle(results[0], results[1], results[2], results[3])
        return None
    def get_salles(self):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete = "SELECT codee,descriptions,categorie,capacite from salle"
        cursor.execute(requete)
        result = cursor.fetchall()
        cursor.close()
        connexion.close()
        salles = []
        for ligne in result:
            salles.append(Salle(ligne[0], ligne[1], ligne[2], ligne[3]))
        return salles


