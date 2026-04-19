import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
#from main import resultat
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

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher",command=self.rechercher_salle)
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
    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)
        if salle:
            self.entry_description.delete(0, "end")
            self.entry_description.insert(0, salle.description)

            self.entry_categorie.delete(0, "end")
            self.entry_categorie.insert(0, salle.categorie)

            self.entry_capacit.delete(0, "end")
            self.entry_capacit.insert(0, str(salle.capacit))
        else:
            messagebox.showerror("Erreur","salle introuvable")

        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "description", "categorie",
                                                              "capacite"), show="headings")
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="DESCRIPTION")
        self.treeList.heading("categorie", text="CATEGORIES")
        self.treeList.heading("capacite", text="CAPACITE")

        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salle()

    def lister_salle(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))














