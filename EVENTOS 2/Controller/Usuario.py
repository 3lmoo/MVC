from modelo.conexionDB import conexion
import tkinter
from tkinter import messagebox

from vista.ConsultarUsuarios import ConsultarUsuarios


class Usuario():
    def __init__(self):
        self.cedula=None
        self.nombre = None
        self.rol = None
        
    #poner aqui getter y setter 

    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[2]== nombreUsuario and usuario[1]== password):
                self.cedula= usuario[1]
                self.nombre= usuario[2]
                self.rol = usuario[3]
                if (usuario[3]== "Admin"):
                    messagebox.showinfo("Informacion"," Acceso correcto! Administrador")
                #crear el objeto mesero 
                    miMenu=ConsultarUsuarios(loggin,self)
                else:
                    messagebox.showinfo("Informacion"," Acceso correcto! Usuario")
                miConexion.cerrarConexion()
                return
        messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseñ a no existen, verifique e intente nuevamente!")


    def consultarTabla(self):
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        return listaUsuario

    def crearUsuario(self, nombreUsuario, cedulaUsuario, rolUsuario):
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuario (Cedula, Nombre, Rol) VALUES (?, ?, ?), (cedulaUsuario,  nombreUsuario, rolUsuario)",)
        miConexion.cerrarConexion()

    def eliminarUsuario(self, cedulaUsuario): 
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("DELETE from usuario WHERE cedula ="+cedulaUsuario)
        miConexion.cerrarConexion()

    def modificarUsuario(self, nombreUsuario, cedulaUsuario, rolUsuario): 
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("UPDATE usuario SET nombre=?, rol=? WHERE cedula=?", (nombreUsuario, rolUsuario, cedulaUsuario))
        miConexion.cerrarConexcio()

    def buscarUsuario(self, cedulaUsuario):
        miConexion = conexion()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        cursor.execute("SELECT * from usuario WHERE cedula="+cedulaUsuario)
        listaUsuarios = cursor.fetchall()
        miConexion.cerrarConexcio()
        if(len(listaUsuarios)) > 0:
            usuario = listaUsuarios[0]
            return usuario
        else:
            return None
