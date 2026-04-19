import customtkinter as ctk
from tkinter import messagebox
from models.salle import Salle
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title = "Gestion de salles"
        self.geometry = "600x400"

        self.service_salle = ServiceSalle()

