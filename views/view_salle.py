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

        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code salle").grid(row=0, column=0, padx=10, pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Description").grid(row=1, column=0, padx=10, pady=10)
        self.entry_description = ctk.CTkEntry(self.cadreInfo)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Categorie").grid(row=2, column=0, padx=10, pady=10)
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
        self.entry_categorie.grid(row=2, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.cadreInfo, text="Capacité").grid(row=3, column=0, padx=10, pady=10)
        self.entry_capacit = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacit.grid(row=3, column=1, padx=10, pady=10)




