import tkinter as tk
from tkinter import *
from tkinter import messagebox

class CrearUsuario():
    def guardarUsuario(self, event):
        self.usuario.crearUsuario(self.txtNomber.get(), self.txtCedula.get(), self.txtRol.get())
        messagebox.showinfo("confirmacion", "Nuevo Usuario Reistrado con exito")

    def __init__(self, menu, usuario):
        self.ventana =tk.Toplevel(menu)
        self.ventana.config(width=360, heigt=385)        
        self.ventana.resizable(0,0)
        self.ventana.title("Crear Nuevo Usuario")
        
        self.usuario = usuario

        self.lblTitulo = tk.Label(self.ventana, text="Crear Usuario")
        self.lblTitulo.place(relax=0.5, y=50, anchor="center")

        self.lblNombre = tk.Label(self.ventana, text="Nomber*:")
        self.lblNombre.place(x=50, y=125, width=80, height=25)

        self.lblCedula =  tk.Label(self.ventana, text="Cedula*:")
        self.lblCedula.place(x=50, y=180, width=80, height=25)

        self.lblRol = tk.Label(self.ventana, text="Rol*:")
        self.lblRol.place(x=50, y=235, width=80, height=25)

        self.lblNombre = tk.Entry(self.ventana)
        self.lblNombre.place(x=160, y=125, width=150, height=25)

        self.lblCedula = tk.Entry(self.ventana)
        self.lblCedula.place(x=160, y=180, width=150, height=25)

        self.lblRol = tk.Entry(self.ventana)
        self.lblRol.place(x=160, y=235, width=150, height=25)

        self.iconoGuardar = tk.PhotoImage(file=r"src\icons\disk.png")
        self.btnGuardar = tk.Button(self.ventana, text="Guardar", imagen=self.iconoGuardar, compound="left")
        self.btnGuardar.place(x=85, y=310, width=80, height=25)
        self.btnGuardar.bind("<Button-1>", self.guardarUsuario)

        self.iconoLimpiar = tk.PhotoImage(file=r"src\icons\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", imagen=self.iconoLimpiar, compound="left")
        self.btnLimpiar.place(x=195, y=310, width=80, height=25)

        self.ventana.mainloop()

