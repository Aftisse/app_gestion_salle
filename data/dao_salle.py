import json
import mysql.connector
from models.salle import Salle

class DataSalle:
    def __init__(self):
        self.config_path = "data/config.json"
    def get_connection(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
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
