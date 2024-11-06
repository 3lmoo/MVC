import tkinter as tk
from tkinter import *
from tkinter import messagebox

class EliminarUsuario():
    def __init__(self, menu):
        self.ventana =tk.Toplevel(menu)
        self.ventana.config(width=415, heigt=385)        
        self.ventana.resizable(0,0)
        self.ventana.title("Eliminar Usuario")

        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Usuario")
        self.lblTitulo.place(relax=0.5, y=50, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nomber*:")
        self.lblNombre.place(x=50, y=125, width=80, height=25)

        self.lblCedula =  tk.Label(self.ventana, text="Cedula*:")
        self.lblCedula.place(x=50, y=180, width=80, height=25)

        self.lblRol = tk.Label(self.ventana, text="Rol*:")
        self.lblRol.place(x=50, y=235, width=80, height=25)

        self.lblNombre = tk.Entry(self.ventana, state="disabled")
        self.lblNombre.place(x=160, y=125, width=150, height=25)

        self.lblCedula = tk.Entry(self.ventana)
        self.lblCedula.place(x=160, y=180, width=150, height=25)

        self.lblRol = tk.Entry(self.ventana, state="disabled")
        self.lblRol.place(x=160, y=235, width=150, height=25)

        self.iconoBuscar = tk.PhotoImage(file=r"MVC\EVENTOS 2\src\icons\icons\magnifier.png")
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", imagen=self.iconoBuscar)
        self.btnBuscar.place(x=340, y=180, width=25, height=25)

        self.iconoEliminar = tk.PhotoImage(file=r"MVC\EVENTOS 2\src\icons\icons\bin_closed.png")
        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", imagen=self.iconoEliminar, compound="left")
        self.btnEliminar.place(x=85, y=310, width=80, height=25)

        self.iconoLimpiar = tk.PhotoImage(file=r"MVC\EVENTOS 2\src\icons\icons\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", imagen=self.iconoLimpiar, compound="left")
        self.btnLimpiar.place(x=195, y=310, width=80, height=25)

        self.ventana.mainloop()