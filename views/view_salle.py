import customtkinter as ctk
from tkinter import messagebox

from main import resultat
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

        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter",command=self.ajouter_salle)
        self.btn_ajouter.pack(side="left", padx=10, pady=10)

        self.btn_modifier =ctk.CTkButton(self.cadreAction, text="Modifier",command=self.modifier_salle)
        self.btn_modifier.pack(side="left", padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer",command=self.supprimer_salle)
        self.btn_supprimer.pack(side="left", padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher")
        self.btn_rechercher.pack(side="left", padx=10, pady=10)

    def ajouter_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_description.get(),
                self.entry_categorie.get(),
                int(self.entry_capacit.get())
            )
            resultat, message = self.service_salle.ajouter_salle(salle)
            if resultat:
                messagebox.showinfo("Succée", message)
            else:
                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "La capacité de la salle n'existe pas")
    def modifier_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_description.get(),
                self.entry_categorie.get(),
                int(self.entry_capacit.get())
            )
            resultat, message = self.service_salle.modifier_salle(salle)
            if resultat:
                messagebox.showinfo("Succée", message)
            else:
                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "La capacité de la salle n'existe pas")
    def supprimer_salle(self):
        code = self.entry_code.get()
        resultat, message = self.service_salle.supprimer_salle(code)
        if resultat:
            messagebox.showinfo("Succés",message)
        else:
            messagebox.showerror("Erreur",message)









