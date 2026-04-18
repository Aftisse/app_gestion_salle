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