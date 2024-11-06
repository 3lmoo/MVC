import tkinter as tk    
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from View.CrearUsuario import crearUsuario
from View.EliminarUsuario import eliminarUsuario
from View.ModificarUsuario import modificarUsuario

class ConsultarUsuarios():
    def crearUsuario(self, event):
        crear = crearUsuario(self.ventana, self.usuario)

    def eliminarUsuario(self, event):
        eliminar = eliminarUsuario(self.ventana)

    def modificarUsuario(self, event):
        modificar = modificarUsuario(self.ventana)


    def __init__(self, loggin, usuario):
        self.ventana= tk.Toplevel(loggin)
        self.ventana.config(width=600)
        self.ventana.title("Tabla de Usuarios")


        self.lbltitulo=tk.Label(self.ventana,text="Listado de Usuarios")
        self.lbltitulo.pack()

        self.tabla=ttk.Treeview(self.ventana)
        self.tabla["columns"]=["ID","Cedula","Nombre","Rol"]
        self.tabla.heading("#1",text="ID")
        self.tabla.heading("#2",text="Cedula")
        self.tabla.heading("#3",text="Nombre")
        self.tabla.heading("#4",text="Rol")

        self.listaUsuario=usuario.consultarTabla()

        for usuario in self.listaUsuario:
            self.tabla.insert("","end",values=[usuario[0],usuario[1],usuario[2],usuario[3]])

        self.tabla["show"]="headings"
        self.tabla.column("#1",width=50)  
        self.tabla.column("#2",width=100)
        self.tabla.column("#3",width=300)
        self.tabla.column("#4",width=100)

        self.scorllbar=ttk.Scrollbar(self.ventana,orient="vertical",command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scorllbar.set)
        self.scorllbar.pack(side="right",fill="y")  

        self.tabla.pack(fill="both",expand=True)

        self.botones = tk.Frame(self.ventana)
        self.botones.config(width=600, height=100)
        self.botones.pack(fill="both", expand=True)

        self.iconoCrear = tk.PhotoImage(filer=r"MVC\EVENTOS 2\src\icons\icons\user_add.png")
        self.btnCrearUsuario = tk.Button(self.botones, image=self.iconoCrear)
        self.btnCrearUsuario.place(relx=05, x=-50, y=25, anchor="nw")
        self.btnCrearUsuario.bind("<Button-1>", self.crearUsuario)

        self.iconoEliminar = tk.PhotoImage(file=r"MVC\EVENTOS 2\src\icons\icons\user_delete.png")
        self.btnEliminarUsuario = tk.Button(self.botones, image=self.iconoEliminar)
        self.btnLimpiar.place(relx=0.5, y=25, anchor="n")
        self.btnEliminarUsuario.bind("<Button-1>", self.eliminarUsuario)

        self.iconoModificar = tk.PhotoImage(filer=r"MVC\EVENTOS 2\src\icons\icons\user_edit.png")
        self.bntModificarUsuario = tk.Button(self.botones, image=self.iconoModificar)
        self.bntModificarUsuario.place(relx=0.5, y=25, x=50, anchor="ne")
        self.btnModificarUsuario.bind("<Button-1>", self.modimficarUsuario)


        self.ventana.mainloop()