import tkinter as tk
from tkinter import END, Toplevel, messagebox, ttk

import articulo as art
import cliente as cli
import compra as com
import dbarticulos as dba
import dbclientes as dbc
import dbcompras as dbcom
import dbproveedores as dbp
import dbusuarios as dbu
import dbventas as dbv
import proveedor as pro
import usuario as usr
import venta as ven

perfiles = ["Administrador", "Gerente", "Cajero"]

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=300, height=500, bg="black")
        self.title("Login")

        self.label_titulo = tk.Label(self, text="Farmacia", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.label_titulo.place(x=100, y=10)

        self.label_username = tk.Label(self, text="Username: ", font=("Arial", 10, "bold"), bg="black", fg="white")
        self.label_username.place(x=10, y=60)
        self.entry_username = tk.Entry(self)
        self.entry_username.place(x=100, y=60)
        self.label_password = tk.Label(self, text="Password: ", font=("Arial", 10, "bold"), bg="black", fg="white")
        self.label_password.place(x=10, y=90)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.place(x=100, y=90)

        self.btn_login = tk.Button(self, text="Login", command=lambda:buttonLogin_clicked())
        self.btn_login.place(x=100,y=130)


        def buttonLogin_clicked():
            aux = usr.Usuario()
            aux.setUsername(self.entry_username.get())
            aux.setPassword(self.entry_password.get())

            dbus = dbu.dbusuarios()
            userLogged = dbus.autentificar(aux)

            if userLogged == 0:
                messagebox.showerror("Error", "La contraseña es incorrecta. Revisa tus datos.")
                return
            if userLogged == 1:
                messagebox.showerror("Error", "El username ingresado no existe. Revisa tus datos.")
            if userLogged:
                self.destroy()
                app=App(userLogged)
                app.mainloop()
            else:
                messagebox.showerror("Error", "Hubo un error al intentar ingresar. Revisa tus datos.")

class App(tk.Tk):

    def __init__(self, userLogged:usr.Usuario):
        super().__init__()
        self.config(width=500, height=500)
        self.title("Menú principal")

        self.label_titulo = tk.Label(self, text="Farmacia", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.label_titulo.place(x=180, y=20)
        
        #self.btn_usuarios = tk.Button(self, text="Usuarios", font=("Arial", 10, "bold"), command=lambda: ventanaTablaUsuarios())
        #self.btn_usuarios.place(x=210, y=80)
        
        self.menu_bar = tk.Menu(self)
        
        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        print(userLogged.getPerfil())
        if userLogged.getPerfil() == "Administrador":
            self.menu_archivo.add_command(label="Usuario", command=lambda: ventanaUsuarios(self))
        else:
            self.menu_archivo.add_command(label="Usuario", command=lambda: ventanaUsuarios(self), state="disabled")
        self.menu_archivo.add_separator()
        if userLogged.getPerfil() in ["Administrador", "Cajero"]:
            self.menu_archivo.add_command(label="Clientes", command=lambda: ventanaClientes(self))
        else:
            self.menu_archivo.add_command(label="Clientes", command=lambda: ventanaClientes(self), state="disabled")
            
        self.menu_archivo.add_separator()
        if userLogged.getPerfil() in ["Administrador", "Gerente"]:
            self.menu_archivo.add_command(label="Compras", command=lambda: ventanaSeleccionarProveedor(self))
        else:
            self.menu_archivo.add_command(label="Compras", command=lambda: ventanaSeleccionarProveedor(self), state="disabled")
            
        self.menu_archivo.add_separator()
        if userLogged.getPerfil() in perfiles:
            self.menu_archivo.add_command(label="Ventas", command=lambda: ventanaVentas(self))
        else:
            self.menu_archivo.add_command(label="Ventas", command=lambda: ventanaVentas(self), state="disabled")
            
        self.menu_archivo.add_separator()
        if userLogged.getPerfil() in ["Administrador"]:
            self.menu_archivo.add_command(label="Proveedores", command=lambda: ventanaProveedores(self))
        else:
            self.menu_archivo.add_command(label="Proveedores", command=lambda: ventanaProveedores(self), state="disabled")
        self.menu_archivo.add_separator()
        if userLogged.getPerfil() in ["Administrador"]:
            self.menu_archivo.add_command(label="Articulos", command=lambda: ventanaArticulos(self))
        else:
            self.menu_archivo.add_command(label="Articulos", command=lambda: ventanaArticulos(self), state="disabled")
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=lambda: salir())
        
        self.menu_bar.add_cascade(label="File", menu=self.menu_archivo)
        
        self.config(menu=self.menu_bar, bg="black")
        
        self.dbu = dbu.dbusuarios()
        self.dbc = dbc.dbclientes()
        self.dbp = dbp.dbproveedores()
        self.dba = dba.dbarticulos()
        self.dbcom = dbcom.dbcompras()
        self.dbv = dbv.dbventas()
        
        def salir():
            self.destroy()
            login = Login()
            login.mainloop()
            

        self.userLogged = userLogged

def ventanaUsuarios(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=500, height=500, bg="black")
    ventana.title("Usuarios")
    
    label_id_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
    label_id_buscar.place(x=30, y=10)
    entry_id_buscar = tk.Entry(ventana, width=30)
    entry_id_buscar.place(x=140, y=10)
    btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
    btn_id_buscar.place(x=330, y=10)
    
    label_id = tk.Label(ventana, text="ID:", bg="black", fg="white")
    label_id.place(x=30, y=50)
    entry_id = tk.Entry(ventana, state="disabled")
    entry_id.place(x=100, y=50)
    
    label_nombre = tk.Label(ventana, text="Nombre:", bg="black", fg="white")
    label_nombre.place(x=30, y=80)
    entry_nombre = tk.Entry(ventana, width=50)
    entry_nombre.place(x=100, y=80)
    
    label_username = tk.Label(ventana, text="Username:", bg="black", fg="white")
    label_username.place(x=30, y=110)
    entry_username = tk.Entry(ventana, width=50)
    entry_username.place(x=100, y=110)
    
    label_password = tk.Label(ventana, text="Password:", bg="black", fg="white")
    label_password.place(x=30, y=140)
    entry_password = tk.Entry(ventana, width=30, show="*")
    entry_password.place(x=100, y=140)
    
    label_perfil = tk.Label(ventana, text="Perfil:", bg="black", fg="white")
    label_perfil.place(x=30, y=170)
    combo_perfil = ttk.Combobox(ventana, values=perfiles, width=30)
    combo_perfil.place(x=100, y=170)
    
    frame_botones = tk.Frame(ventana, bg="black")
    frame_botones.place(x=30, y=210)
    
    btn_nuevo = tk.Button(frame_botones, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
    btn_guardar = tk.Button(frame_botones, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
    btn_cancelar = tk.Button(frame_botones, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
    btn_editar = tk.Button(frame_botones, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
    btn_remover = tk.Button(frame_botones, text="Remover", state="disabled", command=lambda: ventanaEliminarUsuario())
    
    btn_nuevo.pack(side="left", padx=5)
    btn_guardar.pack(side="left", padx=5)
    btn_cancelar.pack(side="left", padx=5)
    btn_editar.pack(side="left", padx=5)
    btn_remover.pack(side="left", padx=5)
    
    if app.userLogged.getPerfil() != "Administrador": btn_nuevo.config(state="disabled")
    

    def buttonGuardar_clicked():
            if entry_nombre.get() == "" or entry_username.get() == "" or entry_password.get() == "" or combo_perfil.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif not (combo_perfil.get() in perfiles):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                ventana.focus()
            else:
                auxUser= usr.Usuario()
                newID = int(entry_id.get())
                if not newID:
                    auxUser.setID(1)
                else:
                    auxUser.setID(newID)
                    auxUser.setNombre(entry_nombre.get())
                    auxUser.setUsername(entry_username.get())
                    auxUser.setPassword(entry_password.get())
                    auxUser.setPerfil(combo_perfil.get())
                try:
                    app.dbu.guardarUser(auxUser)
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente al usuario en los registros con el ID {auxUser.getID()}.", )
                    ventana.focus()
                    
                    entry_id.config(state="normal")
                    entry_id.delete(0, END)
                    entry_id.config(state="disabled")
                    entry_nombre.delete(0, END)
                    entry_username.delete(0, END)
                    entry_password.delete(0, END)
                    combo_perfil.delete(0, END)
                    
                    if app.userLogged.getPerfil() == "Administrador" or app.userLogged.getPerfil() == "Auxiliar": btn_guardar.config(state="disabled")
                    if app.userLogged.getPerfil() == "Administrador" or app.userLogged.getPerfil() == "Auxiliar": btn_nuevo.config(state="normal")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)


    def buttonBuscar_clicked():
        try:
            usr_ = usr.Usuario()
            usr_.setID(int(entry_id_buscar.get()))
            auxUser = app.dbu.buscarUser(usr_)
            
            if auxUser:
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.insert(0, auxUser.getID())
                entry_id.config(state="disabled")
                entry_nombre.delete(0, END)
                entry_nombre.insert(0, auxUser.getNombre())
                entry_username.delete(0, END)
                entry_username.insert(0, auxUser.getUsername())
                entry_password.delete(0, END)
                entry_password.insert(0, auxUser.getPassword())
                combo_perfil.delete(0, END)
                combo_perfil.insert(0, auxUser.getPerfil())
                
                btn_cancelar.config(state="normal")
                if app.userLogged.getPerfil() == "Administrador" or app.userLogged.getPerfil() == "Auxiliar": btn_editar.config(state="normal")
                if app.userLogged.getPerfil() == "Administrador" or app.userLogged.getPerfil() == "Auxiliar": btn_remover.config(state="normal")
                
                
            else:
                messagebox.showerror("Usuario no encontrado", "El usuario no se encuentra registrado en la DB.")
                ventana.focus()
            
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar un número entero en el campo 'ID'.")
            print(e)
            ventana.focus()
            
    def buttonCancelar_clicked():
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_id_buscar.delete(0, END)
        entry_nombre.delete(0, END)
        entry_username.delete(0, END)
        entry_password.delete(0, END)
        combo_perfil.delete(0, END)
        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        
    def buttonNuevo_clicked():
        btn_nuevo.config(state="disabled")
        newID = app.dbu.maxSQL("usuario_id", "usuarios")[0] + 1
        entry_id.config(state="normal")
        entry_id.insert(0, newID)
        entry_id.config(state="disabled")
        btn_guardar.config(state="normal")
        
    def buttonEditar_clicked():
        try:
            if entry_nombre.get() == "" or entry_username.get() == "" or entry_password.get() == "" or combo_perfil.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                ventana.focus()
            elif not (combo_perfil.get() in perfiles):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                ventana.focus()
            else:
                auxUser = usr.Usuario()
                auxUser.setID(int(entry_id.get()))
                auxUser.setNombre(entry_nombre.get())
                auxUser.setUsername(entry_username.get())
                auxUser.setPassword(entry_password.get())
                auxUser.setPerfil(combo_perfil.get())
                edicion = app.dbu.editarUser(auxUser)
                if edicion:
                    messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del usuario.")
                    buttonCancelar_clicked()
                    ventana.focus()
                    
                else:
                    messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del usuario.")
                    ventana.focus()
                
        except Exception as e:
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
            print(e)
            
    def ventanaEliminarUsuario():
        auxUsr = usr.Usuario()
        auxUsr.setID(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar al usuario con ID {auxUsr.getID()}?")
        if confirmation:
            if app.dbu.eliminarUser(auxUsr.getID()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente al usuario con ID {auxUsr.getID()}.")
                buttonCancelar_clicked()
                ventana.focus()
                
            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar al usuario.")
                ventana.focus()
                
        else:
            ventana.focus()

def ventanaClientes(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=500, height=500, bg="black")
    ventana.title("Clientes")

    rfcs = app.dbc.rfcsClientes()
    
    label_id_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
    label_id_buscar.place(x=30, y=10)
    entry_id_buscar = tk.Entry(ventana, width=30)
    entry_id_buscar.place(x=140, y=10)
    btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
    btn_id_buscar.place(x=330, y=10)
    
    label_id = tk.Label(ventana, text="ID:", bg="black", fg="white")
    label_id.place(x=30, y=50)
    entry_id = tk.Entry(ventana, state="disabled")
    entry_id.place(x=100, y=50)
    
    label_nombre = tk.Label(ventana, text="Nombre:", bg="black", fg="white")
    label_nombre.place(x=30, y=80)
    entry_nombre = tk.Entry(ventana, width=50)
    entry_nombre.place(x=100, y=80)
    
    label_rfc = tk.Label(ventana, text="RFC:", bg="black", fg="white")
    label_rfc.place(x=30, y=110)
    entry_rfc = tk.Entry(ventana, width=50)
    entry_rfc.place(x=100, y=110)
    
    label_telefono = tk.Label(ventana, text="Direccion:", bg="black", fg="white")
    label_telefono.place(x=30, y=140)
    entry_direccion = tk.Entry(ventana, width=30)
    entry_direccion.place(x=100, y=140)
    
    label_usuario_id = tk.Label(ventana, text="Usuario ID:", bg="black", fg="white")
    label_usuario_id.place(x=30, y=170)
    entry_usuario_id = tk.Entry(ventana, width=30)
    entry_usuario_id.place(x=100, y=170)
    entry_usuario_id.insert(0, app.userLogged.getID())
    entry_usuario_id.config(state="disabled")
    
    frame_botones = tk.Frame(ventana, bg="black")
    frame_botones.place(x=30, y=210)
    
    btn_nuevo = tk.Button(frame_botones, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
    btn_guardar = tk.Button(frame_botones, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
    btn_cancelar = tk.Button(frame_botones, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
    btn_editar = tk.Button(frame_botones, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
    btn_remover = tk.Button(frame_botones, text="Remover", state="disabled", command=lambda: ventanaEliminarCliente())
    
    btn_nuevo.pack(side="left", padx=5)
    btn_guardar.pack(side="left", padx=5)
    btn_cancelar.pack(side="left", padx=5)
    btn_editar.pack(side="left", padx=5)
    btn_remover.pack(side="left", padx=5)
    

    def buttonBuscar_clicked():
        try:
            cli_ = cli.Cliente()
            cli_.setID(int(entry_id_buscar.get()))
            auxCli = app.dbc.buscarCliente(cli_, [app.userLogged.getID(), app.userLogged.getPerfil()])
            
            
            if auxCli:
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.insert(0, auxCli.getID())
                entry_id.config(state="disabled")
                entry_nombre.delete(0, END)
                entry_nombre.insert(0, auxCli.getNombre())
                entry_rfc.delete(0, END)
                entry_rfc.insert(0, auxCli.getRfc())
                entry_direccion.delete(0, END)
                entry_direccion.insert(0, auxCli.getDireccion())
                
                if app.userLogged.getPerfil() == "Administrador":
                    btn_editar.config(state="normal")
                    btn_remover.config(state="normal")

                btn_cancelar.config(state="normal")
                
            else:
                messagebox.showerror("Cliente no encontrado", "El cliente no se encuentra registrado en la DB.")
                ventana.focus()
            
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar un número entero en el campo 'ID'.")
            print(e)
            ventana.focus()

    def buttonGuardar_clicked():
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_rfc.get() == "" or entry_direccion.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            if entry_rfc.get() in rfcs:
                messagebox.showerror("RFC existente", "El RFC ingresado ya pertenece a un cliente registrado.")
                ventana.focus()
            
            else:
                auxCliente= cli.Cliente()
                newID = int(entry_id.get())
                if not newID:
                    auxCliente.setID(1)
                else:
                    auxCliente.setID(newID)
                    auxCliente.setNombre(entry_nombre.get())
                    auxCliente.setRfc(entry_rfc.get())
                    auxCliente.setDireccion(entry_direccion.get())
                    auxCliente.setUsuarioID(app.userLogged.getID())
                try:
                    app.dbc.guardarCliente(auxCliente)
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente al cliente con el ID {auxCliente.getID()}. Se registra bajo el username {app.userLogged.getUsername()}", )
                    ventana.focus()
                    
                    entry_id.config(state="normal")
                    entry_id.delete(0, END)
                    entry_id.config(state="disabled")
                    entry_nombre.delete(0, END)
                    entry_rfc.delete(0, END)
                    entry_direccion.delete(0, END)
                    btn_guardar.config(state="disabled")
                    btn_nuevo.config(state="normal")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)
    
    def buttonNuevo_clicked():
        btn_nuevo.config(state="disabled")

        max = app.dbc.maxSQL("cliente_id", "clientes")[0]
        if max == None:
            newID = 1
        else:
            newID = max + 1

        entry_id.config(state="normal")
        entry_id.insert(0, newID)
        entry_id.config(state="disabled")
        btn_guardar.config(state="normal")
        
    def buttonEditar_clicked():
        try:
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_rfc.get() == "" or entry_direccion.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                ventana.focus()

            if entry_rfc.get() in rfcs:
                messagebox.showerror("RFC existente", "El RFC ingresado ya pertenece a un cliente registrado.")
                ventana.focus()

            else:
                auxCli = cli.Cliente()
                auxCli.setID(int(entry_id.get()))
                auxCli.setNombre(entry_nombre.get())
                auxCli.setRfc(entry_rfc.get())
                auxCli.setDireccion(entry_direccion.get())
                auxCli.setUsuarioID(app.userLogged.getID())
                edicion = app.dbc.editarCliente(auxCli)
                if edicion:
                    messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del cliente.")
                    buttonCancelar_clicked()
                    ventana.focus()
                    
                else:
                    messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del cliente.")
                    ventana.focus()
                
        except Exception as e:
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
            print(e)

    def buttonCancelar_clicked():
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_id_buscar.delete(0, END)
        entry_nombre.delete(0, END)
        entry_rfc.delete(0, END)
        entry_direccion.delete(0, END)

        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        
    def ventanaEliminarCliente():
        auxCli = cli.Cliente()
        auxCli.setID(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar al cliente con ID {auxCli.getID()}?")
        if confirmation:
            if app.dbc.eliminarCliente(auxCli.getID()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente al cliente con ID {auxCli.getID()}.")
                buttonCancelar_clicked()
                ventana.focus()
                
            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar al cliente.")
                ventana.focus()
                
        else:
            ventana.focus()

def ventanaProveedores(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=500, height=500, bg="black")
    ventana.title("Proveedores")
    
    label_id_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
    label_id_buscar.place(x=30, y=10)
    entry_id_buscar = tk.Entry(ventana, width=30)
    entry_id_buscar.place(x=140, y=10)
    btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
    btn_id_buscar.place(x=330, y=10)
    
    label_id = tk.Label(ventana, text="ID:", bg="black", fg="white")
    label_id.place(x=30, y=50)
    entry_id = tk.Entry(ventana, state="disabled")
    entry_id.place(x=100, y=50)
    
    label_nombre = tk.Label(ventana, text="Nombre:", bg="black", fg="white")
    label_nombre.place(x=30, y=80)
    entry_nombre = tk.Entry(ventana, width=50)
    entry_nombre.place(x=100, y=80)
    
    label_empresa = tk.Label(ventana, text="Empresa:", bg="black", fg="white")
    label_empresa.place(x=30, y=110)
    entry_empresa = tk.Entry(ventana, width=30)
    entry_empresa.place(x=100, y=110)
    
    label_telefono = tk.Label(ventana, text="Telefono:", bg="black", fg="white")
    label_telefono.place(x=30, y=140)
    entry_telefono = tk.Entry(ventana, width=30)
    entry_telefono.place(x=100, y=140)
    
    frame_botones = tk.Frame(ventana, bg="black")
    frame_botones.place(x=30, y=210)
    
    btn_nuevo = tk.Button(frame_botones, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
    btn_guardar = tk.Button(frame_botones, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
    btn_cancelar = tk.Button(frame_botones, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
    btn_editar = tk.Button(frame_botones, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
    btn_remover = tk.Button(frame_botones, text="Remover", state="disabled", command=lambda: ventanaEliminar())
    
    btn_nuevo.pack(side="left", padx=5)
    btn_guardar.pack(side="left", padx=5)
    btn_cancelar.pack(side="left", padx=5)
    btn_editar.pack(side="left", padx=5)
    btn_remover.pack(side="left", padx=5)
    
    def buttonBuscar_clicked():
        try:
            pro_ = pro.Proveedor()
            pro_.set_proveedor_id(int(entry_id_buscar.get()))
            auxPro = app.dbp.buscarProveedor(pro_)
            
            if auxPro:
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.insert(0, auxPro.get_proveedor_id())
                entry_id.config(state="disabled")
                entry_nombre.delete(0, END)
                entry_nombre.insert(0, auxPro.get_nombre())
                entry_empresa.delete(0, END)
                entry_empresa.insert(0, auxPro.get_empresa())
                entry_telefono.delete(0, END)
                entry_telefono.insert(0, auxPro.get_telefono())

                btn_cancelar.config(state="normal")
                btn_editar.config(state="normal")
                btn_remover.config(state="normal")

                
            else:
                messagebox.showerror("Proveedor no encontrado", "El proveedor no se encuentra registrado en la DB.")
                ventana.focus()
            
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar un número entero en el campo 'ID'.")
            print(e)
            ventana.focus()

    def buttonGuardar_clicked():
            if entry_empresa.get() == "" or entry_id.get() == "" or entry_nombre.get() == "" or entry_telefono.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()
            
            else:
                auxProveedor= pro.Proveedor()
                newID = int(entry_id.get())
                if not newID:
                    auxProveedor.set_id(1)
                else:
                    auxProveedor.set_proveedor_id(newID)
                    auxProveedor.set_nombre(entry_nombre.get())
                    auxProveedor.set_empresa(entry_empresa.get())
                    auxProveedor.set_telefono(entry_telefono.get())
                try:
                    app.dbp.guardarProveedor(auxProveedor)
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente el proveedor con el ID {auxProveedor.get_proveedor_id()}.")
                    ventana.focus()
                    
                    entry_id.config(state="normal")
                    entry_id.delete(0, END)
                    entry_id.config(state="disabled")
                    entry_nombre.delete(0, END)
                    entry_empresa.delete(0, END)
                    entry_telefono.delete(0, END)
                    btn_guardar.config(state="disabled")
                    btn_nuevo.config(state="normal")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)
    
    def buttonNuevo_clicked():
        btn_nuevo.config(state="disabled")

        max = app.dbp.maxSQL("proveedor_id", "proveedores")[0]
        if max == None:
            newID = 1
        else:
            newID = max + 1

        entry_id.config(state="normal")
        entry_id.insert(0, newID)
        entry_id.config(state="disabled")
        btn_guardar.config(state="normal")
        
    def buttonEditar_clicked():
        try:
            if entry_nombre.get() == "" or entry_id.get() == "" or entry_empresa.get() == "" or entry_telefono.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para editar el registro.")
                ventana.focus()

            else:
                auxPro = pro.Proveedor()
                auxPro.set_proveedor_id(int(entry_id.get()))
                auxPro.set_nombre(entry_nombre.get())
                auxPro.set_empresa(entry_empresa.get())
                auxPro.set_telefono(entry_telefono.get())
                edicion = app.dbp.editarProveedor(auxPro)
                if edicion:
                    messagebox.showinfo("Edición exitosa", "Se han editado correctamente los datos del proveedor.")
                    buttonCancelar_clicked()
                    ventana.focus()
                    
                else:
                    messagebox.showerror("Edición fallida", "No ha sido posible editar los datos del proveedor.")
                    ventana.focus()
                
        except Exception as e:
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
            print(e)

    def buttonCancelar_clicked():
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_id_buscar.delete(0, END)
        entry_nombre.delete(0, END)
        entry_empresa.delete(0, END)
        entry_telefono.delete(0, END)

        #if app.userLogged.getPerfil() == "Administrador" or app.userLogged.getPerfil() == "Auxiliar":
        #    btn_nuevo.config(state="normal")
        #else:
        #    btn_nuevo.config(state="disabled")

        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        
    def ventanaEliminar():
        auxPro = pro.Proveedor()
        auxPro.set_proveedor_id(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar el proveedor con ID {auxPro.get_proveedor_id()}?")
        if confirmation:
            if app.dbp.eliminarProveedor(auxPro.get_proveedor_id()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente el proveedor con ID {auxPro.get_proveedor_id()}.")
                buttonCancelar_clicked()
                ventana.focus()
                
            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible elimiar el articulo.")
                ventana.focus()
                
        else:
            ventana.focus()

def ventanaArticulos(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=600, height=600, bg="black")
    ventana.title("Articulos")
    
    valoresTabla = {}
    valoresQuitados = []
    valoresAgregados = []
    
    
    isAdmin = app.userLogged.getPerfil() == "Administrador"
    provsProvIDs = app.dbp.dictProvIDs()
    articsArtIDs = app.dba.dictArtIDs()
    
    
    provs = []
    provs_ids = []
    for prov in provsProvIDs:
        provs.append(prov[0])
        provs_ids.append(int(prov[1]))
        
    artsIds = {}
    for articulo in articsArtIDs:
        artsIds[int(articulo[1])] = articulo[0]

    #vehMatriculas = []
    #valoresMatriculas = app.dbv.vehMatriculas(app.userLogged.getID(), True)
    #for valor in valoresMatriculas:
    #    vehMatriculas.append(valor[0])

    label_id_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
    label_id_buscar.place(x=30, y=10)
    entry_id_buscar = tk.Entry(ventana, width=30)
    entry_id_buscar.place(x=180, y=10)
    btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
    btn_id_buscar.place(x=370, y=10)
    
    label_id = tk.Label(ventana, text="ID:", bg="black", fg="white")
    label_id.place(x=30, y=50)
    entry_id = tk.Entry(ventana, state="disabled")
    entry_id.place(x=115, y=50)
    
    label_descripcion = tk.Label(ventana, text="Descripcion:", bg="black", fg="white")
    label_descripcion.place(x=30, y=80)
    entry_descripcion = tk.Entry(ventana, width=30)
    entry_descripcion.place(x=115, y=80)

    label_precio_uni = tk.Label(ventana, text="Precio Unitario:", bg="black", fg="white")
    label_precio_uni.place(x=30, y=110)
    entry_precio_uni = tk.Entry(ventana, width=30)
    entry_precio_uni.place(x=115, y=110)
    
    label_precio_venta = tk.Label(ventana, text="Precio Venta:", bg="black", fg="white")
    label_precio_venta.place(x=30, y=140)
    entry_precio_venta = tk.Entry(ventana, width=30)
    entry_precio_venta.place(x=115, y=140)

    label_proveedor = tk.Label(ventana, text="Proveedor:", bg="black", fg="white")
    label_proveedor.place(x=30, y=170)
    combo_proveedor = ttk.Combobox(ventana, values=provs, width=30)
    combo_proveedor.place(x=115, y=170)

    label_existencias = tk.Label(ventana, text="Existencias:", bg="black", fg="white")
    label_existencias.place(x=30, y=200)
    entry_existencias = tk.Entry(ventana, width=30)
    entry_existencias.place(x=115, y=200)
    
    frame_botones1 = tk.Frame(ventana, bg="black")
    frame_botones1.place(x=30, y=270)

    columnas = ["Índice", "Proveedor ID", "Articulo ID", "Existencias"]
    
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
    for columna in columnas:
        tabla.heading(columna, text=columna)
        tabla.column(columna, width=10, stretch=tk.YES)

    tabla.place(x=30, y=300, width=500, height=150)

    frame_botones2 = tk.Frame(ventana, bg="black")
    frame_botones2.place(x=30, y=500)
    
    btn_agregar = tk.Button(frame_botones1, text="Agregar", state="disabled", command=lambda: buttonAgregar_clicked())
    btn_quitar = tk.Button(frame_botones1, text="Quitar", state="disabled", command=lambda: buttonQuitar_clicked(tabla.selection()))
    
    btn_nuevo = tk.Button(frame_botones2, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
    btn_guardar = tk.Button(frame_botones2, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
    btn_cancelar = tk.Button(frame_botones2, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
    btn_editar = tk.Button(frame_botones2, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
    btn_remover = tk.Button(frame_botones2, text="Remover", state="disabled", command=lambda: ventanaEliminarArticulo())
    
    btn_agregar.pack(side="right", padx=5)
    btn_quitar.pack(side="right", padx=5)
    btn_nuevo.pack(side="left", padx=5)
    btn_guardar.pack(side="left", padx=5)
    btn_cancelar.pack(side="left", padx=5)
    btn_editar.pack(side="left", padx=5)
    btn_remover.pack(side="left", padx=5)

    btn_nuevo.config(state="normal")
    
    def buttonAgregar_clicked():
        
        if entry_id.get() == "" or entry_descripcion.get() == "" or entry_precio_uni.get() == "" or entry_precio_venta.get() == "" or combo_proveedor.get() == "" or entry_existencias.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para agregar el registro.")
            ventana.focus()
        elif not (combo_proveedor.get() in provs):
            messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
            ventana.focus()
        else:
                
            try:
                existencias_a_poner = int(entry_existencias.get())
                precio_uni_a_poner = float(entry_precio_venta.get())
                precio_ven_a_poner = float(entry_precio_uni.get())
                maxDetalleId = app.dba.maxSQL("det_id", "det_articulo")[0]
                
                if len(getIdsFromTabla()) == 0:
                    if not maxDetalleId:
                        aux_detalle_art_id = 1
                    else:
                        aux_detalle_art_id = maxDetalleId + 1
                else:
                    if not maxDetalleId:
                        aux_detalle_art_id = max(getIdsFromTabla()) + 1
                    else:
                        aux_detalle_art_id = max(int(maxDetalleId), max(getIdsFromTabla())) + 1
                
            except Exception as e:
                messagebox.showerror("Cantidad inválida", "Favor de ingresar un número entero para la cantidad.")
                print(e)
                ventana.focus
                return
            
            if int(entry_existencias.get()) <= 0:
                messagebox.showerror("Cantidad inválida", "Favor de ingresar un número entero positivo para la cantidad.")
                ventana.focus()
                return

            tabla.insert('', 'end', values=(aux_detalle_art_id, provs_ids[provs.index(combo_proveedor.get())], entry_id.get(), existencias_a_poner))
            valoresAgregados.append([aux_detalle_art_id, provs_ids[provs.index(combo_proveedor.get())], entry_id.get(), entry_existencias.get()])

            valorInt = []
            for i in tabla.item(tabla.get_children()[len(tabla.get_children())-1], "values"):
                valorInt.append(int(i))
            
            valoresTabla[tabla.get_children()[len(tabla.get_children())-1]] = valorInt
            #print(valoresTabla)

    def buttonQuitar_clicked(seleccion: ttk.Treeview.selection):

        if not seleccion:
            messagebox.showerror("Sin selección", "No hay ningún elemento de la tabla seleccionado.")
            return
        
        valores = tabla.item(seleccion[0], "values")
        #idArt = int(valores[2])
        #cantPieza = int(valores[3])
        #nuevaCantidad = int(app.dbp.getCantidadPieza(idArt)[0]) + cantPieza
        valores = list(valores)
        
        valoresTabla.pop(seleccion[0])
        valoresQuitados.append(valores)
        print(valoresQuitados)

        for i in range(len(valores)):
            valores[i] = int(valores[i])

        #valoresQuitados.append(valores)
        tabla.delete(seleccion[0])

    def buttonBuscar_clicked():
        try:
            art_ = art.Articulo()
            art_.set_id(entry_id_buscar.get())
            auxArt = app.dba.buscarArticulo(art_, [app.userLogged.getID(), app.userLogged.getPerfil()])
            if auxArt:

                valoresTabla.clear()

                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.insert(0, auxArt.get_id())
                entry_id.config(state="disabled")
                combo_proveedor.delete(0, END)
                entry_descripcion.delete(0, END)
                entry_descripcion.insert(0, auxArt.get_descripcion())
                entry_precio_uni.delete(0, END)
                entry_precio_uni.insert(0, auxArt.get_precio_unitario())
                entry_precio_venta.delete(0, END)
                entry_precio_venta.insert(0, auxArt.get_precio_venta())
                entry_existencias.delete(0, END)

                if app.userLogged.getPerfil()=="Administrador":
                    btn_agregar.config(state="normal")
                    btn_quitar.config(state="normal")
                    btn_editar.config(state="normal")
                    btn_remover.config(state="normal")

                btn_cancelar.config(state="normal")

                detalles_articulo = app.dba.detallesArt(auxArt.get_id())

                for detalle in detalles_articulo:
                    tabla.insert('', 'end', values=detalle)
                    indiceTabla = tabla.get_children()[len(tabla.get_children())-1]
                    valores = tabla.item(tabla.get_children()[len(tabla.get_children())-1], "values")
                    valoresTabla[indiceTabla] = valores
                    
                print(valoresTabla)

            else:
                messagebox.showerror("Articulo no encontrado", "El articulo no se encuentra registrada en la DB.")
                ventana.focus()
        except Exception as e:
            messagebox.showerror("Valor no válido", "Favor de ingresar un ID válido.")
            print(e)
            ventana.focus()

    def buttonGuardar_clicked():
        art_ = art.Articulo()
        art_.set_id(int(entry_id.get()))
        art_.set_descripcion(entry_descripcion.get())
        art_.set_precio_unitario(float(entry_precio_uni.get()))
        art_.set_precio_venta(float(entry_precio_venta.get()))

        
        elementosTabla = tabla.get_children()
        valoresGuardadoTabla = []
        for elemento in elementosTabla:
            valor = tabla.item(elemento, "values")
            valorInt = []
            for columna in valor:
                columnaInt = int(columna)
                valorInt.append(columnaInt)
            valoresGuardadoTabla.append(valorInt)

        
        if entry_id.get() == "" or entry_descripcion.get() == "" or entry_precio_uni.get() == "" or entry_precio_venta.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
            ventana.focus()

        elif len(elementosTabla) == 0:
            messagebox.showerror("Reparacion sin detalles", "Favor de ingresar detalles del articulo (proveedor y existencias).")
            ventana.focus()
        
        else:
            auxArticulo = art.Articulo()
            auxArticulo.set_id(int(entry_id.get()))
            auxArticulo.set_descripcion(entry_descripcion.get())
            auxArticulo.set_precio_unitario(float(entry_precio_uni.get()))
            auxArticulo.set_precio_venta(float(entry_precio_venta.get()))
            try:
                app.dba.guardarArticulo(auxArticulo)
                ventana.focus()

                for valor in valoresGuardadoTabla:
                    artId = valor[2]
                    artCant = valor[3]
                    #pizCantActual = int(app.dbp.getCantidadPieza(pizId)[0])
                    #app.dbp.actualizarCantPieza(pizId, pizCantActual-pizCant)
                    app.dba.guardarDetalleArticulo(valor)

                        
                messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente el articulo con el ID {auxArticulo.get_id()}.")
                
                valoresTabla.clear()
                print(valoresTabla)
                valoresAgregados.clear()
                valoresQuitados.clear()
                tabla.delete(*tabla.get_children())
                entry_id_buscar.delete(0, END)
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.config(state="disabled")
                combo_proveedor.delete(0, END)
                entry_descripcion.delete(0, END)
                entry_precio_uni.delete(0, END)
                entry_precio_venta.delete(0, END)
                entry_existencias.delete(0, END)
                btn_nuevo.config(state="normal")
                btn_cancelar.config(state="disabled")
                btn_editar.config(state="disabled")
                btn_remover.config(state="disabled")
                btn_guardar.config(state="disabled")
                btn_agregar.config(state="disabled")
                btn_quitar.config(state="disabled")
                
            except Exception as e:
                messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                print(e)

    def buttonNuevo_clicked():

        valoresTabla.clear()
        print(valoresTabla)
        valoresAgregados.clear()
        valoresQuitados.clear()
        
        maxFolio = app.dba.maxSQL("articulo_id", "articulos")[0]
        if not maxFolio:
            newFolio = 1
        else:
            newFolio = maxFolio + 1
        
        entry_id_buscar.delete(0, END)
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.insert(0, newFolio)
        entry_id.config(state="disabled")
        entry_descripcion.delete(0, END)
        entry_precio_uni.delete(0, END)
        entry_precio_venta.delete(0, END)
        combo_proveedor.delete(0, END)
        entry_existencias.delete(0, END)

        tabla.delete(*tabla.get_children())

        btn_guardar.config(state="normal")
        btn_cancelar.config(state="normal")
        btn_agregar.config(state="normal")
        btn_quitar.config(state="normal")
        
    def buttonEditar_clicked():
        art_ = art.Articulo()
        art_.set_id(int(entry_id.get()))

        #if not app.dbr.buscarReparacionMatricula(rep_, [app.userLogged.getID(), app.userLogged.getPerfil()]):
        elementosTabla = tabla.get_children()

        
        if entry_descripcion.get() == "" or entry_precio_uni.get() == "" or entry_precio_venta.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
            ventana.focus()

        elif len(elementosTabla) == 0:
            messagebox.showerror("Artiuclo sin detalles", "Favor de ingresar detalles del articulo.")
            ventana.focus()
        
        else:
            auxArticulo= art.Articulo()
            auxArticulo.set_id(int(entry_id.get()))
            auxArticulo.set_descripcion(entry_descripcion.get())
            auxArticulo.set_precio_unitario(int(entry_precio_uni.get()))
            auxArticulo.set_precio_venta(int(entry_precio_venta.get()))
            try:
                app.dba.editarArticulo(auxArticulo)
                ventana.focus()

                for valor in valoresAgregados:
                    app.dba.guardarDetalleArticulo(valor)

                for valor in valoresQuitados:
                    app.dba.eliminarDetalleArticulo(valor[0])

                messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente el articulo con el ID {auxArticulo.get_id()}.")
                
                valoresTabla.clear()
                print(valoresTabla)
                valoresAgregados.clear()
                valoresQuitados.clear()
                tabla.delete(*tabla.get_children())
                entry_id_buscar.delete(0, END)
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.config(state="disabled")
                combo_proveedor.delete(0, END)
                entry_descripcion.delete(0, END)
                entry_existencias.delete(0, END)
                entry_precio_uni.delete(0, END)
                entry_precio_venta.delete(0, END)
                btn_nuevo.config(state="normal")
                btn_cancelar.config(state="disabled")
                btn_editar.config(state="disabled")
                btn_remover.config(state="disabled")
                btn_guardar.config(state="disabled")
                btn_agregar.config(state="disabled")
                btn_quitar.config(state="disabled")
                
            except Exception as e:
                messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                print(e)

        #else:
        #    messagebox.showerror("Folio existente con otra matricula", "El folio que se intenta guardar ya está guardado con otra matricula.")

    def buttonCancelar_clicked():

        valoresTabla.clear()
        print(valoresTabla)
        valoresAgregados.clear()
        valoresQuitados.clear()

        tabla.delete(*tabla.get_children())

        entry_id_buscar.delete(0, END)
        entry_id.config(state="normal")
        entry_id.delete(0, END)
        entry_id.config(state="disabled")
        entry_precio_uni.delete(0, END)
        entry_precio_venta.delete(0, END)
        combo_proveedor.delete(0, END)
        entry_existencias.delete(0, END)
        entry_descripcion.delete(0, END)

        btn_nuevo.config(state="normal")
        btn_cancelar.config(state="disabled")
        btn_editar.config(state="disabled")
        btn_remover.config(state="disabled")
        btn_guardar.config(state="disabled")
        btn_agregar.config(state="disabled")
        btn_quitar.config(state="disabled")

    def getIdsFromTabla():
        elementos = tabla.get_children()
        idsList = []
        for elemento in elementos:
            valores = tabla.item(elemento, "values")
            idsList.append(int(valores[0]))
        return idsList

    def ventanaEliminarArticulo():
        auxArt = art.Articulo()
        auxArt.set_id(int(entry_id.get()))
        
        confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar el articulo con id {auxArt.get_id()} y todos sus detalles?")
        if confirmation:
            if app.dba.eliminarArticulo(auxArt.get_id()):
                messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente el articulo con ID {auxArt.get_id()}.")
                ventana.focus()

                valoresTabla.clear()

                valoresAgregados.clear()
                valoresQuitados.clear()

                tabla.delete(*tabla.get_children())

                entry_id_buscar.delete(0, END)
                entry_id.config(state="normal")
                entry_id.delete(0, END)
                entry_id.config(state="disabled")
                combo_proveedor.delete(0, END)
                entry_descripcion.delete(0, END)
                entry_existencias.delete(0, END)
                entry_precio_uni.delete(0, END)
                entry_precio_venta.delete(0, END)

                btn_nuevo.config(state="normal")
                btn_cancelar.config(state="disabled")
                btn_editar.config(state="disabled")
                btn_remover.config(state="disabled")
                btn_guardar.config(state="disabled")
                btn_agregar.config(state="disabled")
                btn_quitar.config(state="disabled")

            else:
                messagebox.showerror("Eliminación fallida", "No ha sido posible eliminar la reparación.")
                ventana.focus()
        else:
            ventana.focus()

def ventanaSeleccionarProveedor(app: App):
    ventana = tk.Toplevel()
    ventana.config(width=500, height=100, bg="black")
    ventana.title("Selecciona proveedor")
    
    provsProvIDs = app.dbp.dictProvIDs()
    
    proveedores = []
    proveedores_ids = []
    for prov in provsProvIDs:
        proveedores.append(prov[0])
        proveedores_ids.append(int(prov[1]))
    
    label_seleccion = tk.Label(ventana, text="Proveedor:", bg="black", fg="white")
    label_seleccion.place(x=30, y=10)
    combo_seleccion = ttk.Combobox(ventana, values=proveedores, width=30)
    combo_seleccion.place(x=115, y=10)
    
    btn_seleccionar = tk.Button(ventana, text="Buscar", command=lambda: seleccion(), width=10)
    btn_seleccionar.place(x=355, y=10)
    
    def seleccion():
        if (combo_seleccion.get() == "") or (not combo_seleccion.get() in proveedores):
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
            ventana.focus()
        else:
            id_proveedor = proveedores_ids[proveedores.index(combo_seleccion.get())]
            proveedor_pasar = [int(id_proveedor), combo_seleccion.get()]
            ventana.destroy()
            ventanaCompras(proveedor_pasar)

    def ventanaCompras(proveedor: list):
        ventana = tk.Toplevel()
        ventana.config(width=600, height=600, bg="black")
        ventana.title("Compras")
        
        valoresTabla = {}
        valoresQuitados = []
        valoresAgregados = []
        
        
        isAdmin = app.userLogged.getPerfil() == "Administrador"
        #provsProvIDs = app.dbp.dictProvIDs()
        articsArtIDs = app.dba.dictArtIDsFromProveedor(proveedor[0])
        
        
        #provs = []
        #provs_ids = []
        #for prov in provsProvIDs:
        #    provs.append(prov[0])
        #    provs_ids.append(int(prov[1]))
            
        arts = []
        arts_ids = []
        for i in articsArtIDs:
            arts.append(i[0])
            arts_ids.append(int(i[1]))

        #vehMatriculas = []
        #valoresMatriculas = app.dbv.vehMatriculas(app.userLogged.getID(), True)
        #for valor in valoresMatriculas:
        #    vehMatriculas.append(valor[0])

        label_folio_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
        label_folio_buscar.place(x=30, y=10)
        entry_folio_buscar = tk.Entry(ventana, width=30)
        entry_folio_buscar.place(x=180, y=10)
        btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
        btn_id_buscar.place(x=370, y=10)
        
        
        label_folio = tk.Label(ventana, text="Folio:", bg="black", fg="white")
        label_folio.place(x=30, y=50)
        entry_folio = tk.Entry(ventana, state="disabled")
        entry_folio.place(x=115, y=50)
        
        label_fecha = tk.Label(ventana, text="Fecha:", bg="black", fg="white")
        label_fecha.place(x=30, y=80)
        entry_fecha = tk.Entry(ventana, width=30)
        entry_fecha.place(x=115, y=80)

        label_proveedor = tk.Label(ventana, text="Proveedor:", bg="black", fg="white")
        label_proveedor.place(x=30, y=110)
        combo_proveedor = tk.Entry(ventana, width=30, state="disabled")
        combo_proveedor.place(x=115, y=110)
        
        label_cantidad = tk.Label(ventana, text="Cantidad:", bg="black", fg="white")
        label_cantidad.place(x=30, y=140)
        entry_cantidad = tk.Entry(ventana, width=30)
        entry_cantidad.place(x=115, y=140)

        label_articulo = tk.Label(ventana, text="Articulo:", bg="black", fg="white")
        label_articulo.place(x=30, y=170)
        combo_articulo = ttk.Combobox(ventana, values=arts, width=30)
        combo_articulo.place(x=115, y=170)
        
        frame_botones1 = tk.Frame(ventana, bg="black")
        frame_botones1.place(x=30, y=270)

        columnas = ["Índice", "Folio", "Cantidad", "Articulo ID"]
        
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
        for columna in columnas:
            tabla.heading(columna, text=columna)
            tabla.column(columna, width=10, stretch=tk.YES)

        tabla.place(x=30, y=300, width=500, height=150)

        frame_botones2 = tk.Frame(ventana, bg="black")
        frame_botones2.place(x=30, y=500)
        
        btn_agregar = tk.Button(frame_botones1, text="Agregar", state="disabled", command=lambda: buttonAgregar_clicked())
        btn_quitar = tk.Button(frame_botones1, text="Quitar", state="disabled", command=lambda: buttonQuitar_clicked(tabla.selection()))
        
        btn_nuevo = tk.Button(frame_botones2, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
        btn_guardar = tk.Button(frame_botones2, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
        btn_cancelar = tk.Button(frame_botones2, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
        btn_editar = tk.Button(frame_botones2, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
        btn_remover = tk.Button(frame_botones2, text="Remover", state="disabled", command=lambda: ventanaEliminarCompra())
        
        btn_agregar.pack(side="right", padx=5)
        btn_quitar.pack(side="right", padx=5)
        btn_nuevo.pack(side="left", padx=5)
        btn_guardar.pack(side="left", padx=5)
        btn_cancelar.pack(side="left", padx=5)
        btn_editar.pack(side="left", padx=5)
        btn_remover.pack(side="left", padx=5)
        
        def buttonAgregar_clicked():
            
            cantidad_art_aux = int(entry_cantidad.get())
            id_art_aux = arts_ids[arts.index(combo_articulo.get())]
            
            current_storage = app.dba.getCantidadArticulo(id_art_aux, proveedor[0])[0]
            articles_in_table = sum(int(tabla.item(item, "values")[2]) for item in tabla.get_children() if int(tabla.item(item, "values")[3]) == id_art_aux)

            if cantidad_art_aux > (current_storage - articles_in_table):
                messagebox.showerror("Cantidad insuficiente", "No hay suficientes existencias del artículo seleccionado.")
                return
            
            if entry_folio.get() == "" or entry_fecha.get() == "" or entry_cantidad.get() == "" or combo_articulo.get() == "" or combo_proveedor.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para agregar el registro.")
                ventana.focus()
            elif not (combo_articulo.get() in arts):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                ventana.focus()
            else:
                try:
                    existencias_a_poner = int(entry_cantidad.get())
                    maxDetalleId = app.dbcom.maxSQL("det_id", "det_compra")[0]
                    
                    if len(getIdsFromTabla()) == 0:
                        if not maxDetalleId:
                            aux_detalle_com_id = 1
                        else:
                            aux_detalle_com_id = maxDetalleId + 1
                    else:
                        if not maxDetalleId:
                            aux_detalle_com_id = max(getIdsFromTabla()) + 1
                        else:
                            aux_detalle_com_id = max(int(maxDetalleId), max(getIdsFromTabla())) + 1
                    
                except Exception as e:
                    messagebox.showerror("Cantidad inválida", "Favor de ingresar un número entero para la cantidad.")
                    print(e)
                    ventana.focus
                    return
                
                if int(entry_cantidad.get()) <= 0:
                    messagebox.showerror("Cantidad inválida", "Favor de ingresar un número entero positivo para la cantidad.")
                    ventana.focus()
                    return
                
                #if

                tabla.insert('', 'end', values=(aux_detalle_com_id, entry_folio.get(), existencias_a_poner, arts_ids[arts.index(combo_articulo.get())]))
                valoresAgregados.append([aux_detalle_com_id, entry_folio.get(), existencias_a_poner, arts_ids[arts.index(combo_articulo.get())]])

                valorInt = []
                for i in tabla.item(tabla.get_children()[len(tabla.get_children())-1], "values"):
                    valorInt.append(int(i))
                
                valoresTabla[tabla.get_children()[len(tabla.get_children())-1]] = valorInt
                #print(valoresTabla)

        def buttonQuitar_clicked(seleccion: ttk.Treeview.selection):

            if not seleccion:
                messagebox.showerror("Sin selección", "No hay ningún elemento de la tabla seleccionado.")
                return
            
            valores = tabla.item(seleccion[0], "values")
            #idArt = int(valores[2])
            #cantPieza = int(valores[3])
            #nuevaCantidad = int(app.dbp.getCantidadPieza(idArt)[0]) + cantPieza
            valores = list(valores)
            
            valoresTabla.pop(seleccion[0])
            valoresQuitados.append(valores)
            print(valoresQuitados)

            for i in range(len(valores)):
                valores[i] = int(valores[i])

            #valoresQuitados.append(valores)
            tabla.delete(seleccion[0])

        def buttonBuscar_clicked():
            try:
                com_ = com.Compra()
                com_.set_folio(entry_folio_buscar.get())
                auxCom = app.dbcom.buscarCompra(com_, [app.userLogged.getID(), app.userLogged.getPerfil()])
                if auxCom:
                    valoresTabla.clear()
                    proveedoraux1 = pro.Proveedor()
                    proveedoraux1.set_proveedor_id(auxCom.get_proveedor_id())
                    proveedoraux2 = app.dbp.buscarProveedor(proveedoraux1)
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.insert(0, auxCom.get_folio())
                    entry_folio.config(state="disabled")
                    combo_proveedor.delete(0, END)
                    combo_proveedor.config(state="normal")
                    combo_proveedor.delete(0, END)
                    combo_proveedor.insert(0, proveedoraux2.get_nombre())
                    combo_proveedor.config(state="disabled")
                    entry_fecha.delete(0, END)
                    entry_fecha.insert(0, auxCom.get_fecha())

                    
                    btn_nuevo.config(state="disabled")
                    btn_agregar.config(state="normal")
                    btn_quitar.config(state="normal")
                    btn_editar.config(state="normal")
                    btn_remover.config(state="normal")
                    btn_cancelar.config(state="normal")

                    detalles_compra = app.dbcom.detallesCom(auxCom.get_folio())

                    for detalle in detalles_compra:
                        tabla.insert('', 'end', values=detalle)
                        indiceTabla = tabla.get_children()[len(tabla.get_children())-1]
                        valores = tabla.item(tabla.get_children()[len(tabla.get_children())-1], "values")
                        valoresTabla[indiceTabla] = valores
                        
                    print(valoresTabla)

                else:
                    messagebox.showerror("Compra no encontrada", "La copmpra no se encuentra registrada en la DB.")
                    ventana.focus()
            except Exception as e:
                messagebox.showerror("Valor no válido", "Favor de ingresar un ID válido.")
                print(e)
                ventana.focus()

        def buttonGuardar_clicked():
            com_ = com.Compra()
            com_.set_folio(int(entry_folio.get()))
            com_.set_fecha(entry_fecha.get())
            com_.set_proveedor_id(proveedor[0])
            
            elementosTabla = tabla.get_children()
            valoresGuardadoTabla = []
            for elemento in elementosTabla:
                valor = tabla.item(elemento, "values")
                valorInt = []
                for columna in valor:
                    columnaInt = int(columna)
                    valorInt.append(columnaInt)
                valoresGuardadoTabla.append(valorInt)

            
            if entry_folio.get() == "" or entry_fecha.get() == "" or combo_proveedor.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif len(elementosTabla) == 0:
                messagebox.showerror("Compra sin detalles", "Favor de ingresar detalles de la compra.")
                ventana.focus()
                
            #elif :
                
            
            else:
                auxCompra = com.Compra()
                auxCompra.set_folio(int(entry_folio.get()))
                auxCompra.set_fecha(entry_fecha.get())
                auxCompra.set_proveedor_id(proveedor[0])
                try:
                    app.dbcom.guardarCompra(auxCompra)
                    ventana.focus()

                    for valor in valoresGuardadoTabla:
                        artId = valor[3]
                        artCant = valor[2]
                        artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual-artCant)
                        app.dba.actualizarCantArticulo2(artId, artCantActual2+artCant)
                        app.dbcom.guardarDetalleCompra(valor)

                            
                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente la compra con el folio {auxCompra.get_folio()}.")
                    
                    valoresTabla.clear()
                    print(valoresTabla)
                    valoresAgregados.clear()
                    valoresQuitados.clear()
                    tabla.delete(*tabla.get_children())
                    entry_folio_buscar.delete(0, END)
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.config(state="disabled")
                    combo_proveedor.delete(0, END)
                    entry_fecha.delete(0, END)
                    entry_cantidad.delete(0, END)
                    btn_nuevo.config(state="normal")
                    btn_cancelar.config(state="disabled")
                    btn_editar.config(state="disabled")
                    btn_remover.config(state="disabled")
                    btn_guardar.config(state="disabled")
                    btn_agregar.config(state="disabled")
                    btn_quitar.config(state="disabled")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)

        def buttonNuevo_clicked():

            valoresTabla.clear()
            print(valoresTabla)
            valoresAgregados.clear()
            valoresQuitados.clear()
            
            maxFolio = app.dbcom.maxSQL("folio", "compras")[0]
            if not maxFolio:
                newFolio = 1
            else:
                newFolio = maxFolio + 1
            
            entry_folio_buscar.delete(0, END)
            entry_folio.config(state="normal")
            entry_folio.delete(0, END)
            entry_folio.insert(0, newFolio)
            entry_folio.config(state="disabled")
            entry_cantidad.delete(0, END)
            entry_fecha.delete(0, END)
            combo_articulo.delete(0, END)
            combo_proveedor.config(state="normal")
            combo_proveedor.delete(0, END)
            combo_proveedor.insert(0, proveedor[1])
            combo_proveedor.config(state="disabled")

            tabla.delete(*tabla.get_children())

            btn_guardar.config(state="normal")
            btn_cancelar.config(state="normal")
            btn_agregar.config(state="normal")
            btn_quitar.config(state="normal")
            
        def buttonEditar_clicked():
            com_ = com.Compra()
            com_.set_folio(int(entry_folio.get()))

            #if not app.dbr.buscarReparacionMatricula(rep_, [app.userLogged.getID(), app.userLogged.getPerfil()]):
            elementosTabla = tabla.get_children()

            if entry_fecha.get() == "" or combo_proveedor.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif len(elementosTabla) == 0:
                messagebox.showerror("Compra sin detalles", "Favor de ingresar detalles de la compra.")
                ventana.focus()
            
            else:
                auxCompra = com.Compra()
                auxCompra.set_folio(int(entry_folio.get()))
                auxCompra.set_fecha(entry_fecha.get())
                auxCompra.set_proveedor_id(int(proveedores_ids[proveedores.index(combo_proveedor.get())]))
                try:
                    app.dbcom.editarCompra(auxCompra)
                    ventana.focus()

                    for valor in valoresAgregados:
                        artId = valor[3]
                        artCant = valor[2]
                        artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual-artCant)
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        app.dba.actualizarCantArticulo2(artId, artCantActual2+artCant)
                        
                        app.dbcom.guardarDetalleCompra(valor)

                    for valor in valoresQuitados:
                        artId = valor[3]
                        artCant = valor[2]
                        artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual+artCant)
                        app.dbcom.eliminarDetalleCompra(valor[0])
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        app.dba.actualizarCantArticulo2(artId, artCantActual2-artCant)

                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente la compra con el folio {auxCompra.get_folio()}.")
                    
                    valoresTabla.clear()
                    print(valoresTabla)
                    valoresAgregados.clear()
                    valoresQuitados.clear()

                    tabla.delete(*tabla.get_children())

                    entry_folio_buscar.delete(0, END)
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.config(state="disabled")
                    entry_cantidad.delete(0, END)
                    entry_fecha.delete(0, END)
                    combo_proveedor.config(state="normal")
                    combo_proveedor.delete(0, END)
                    combo_proveedor.config(state="disabled")
                    combo_articulo.delete(0, END)

                    btn_nuevo.config(state="normal")
                    btn_cancelar.config(state="disabled")
                    btn_editar.config(state="disabled")
                    btn_remover.config(state="disabled")
                    btn_guardar.config(state="disabled")
                    btn_agregar.config(state="disabled")
                    btn_quitar.config(state="disabled")
                    
                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)

            #else:
            #    messagebox.showerror("Folio existente con otra matricula", "El folio que se intenta guardar ya está guardado con otra matricula.")

        def buttonCancelar_clicked():

            valoresTabla.clear()
            print(valoresTabla)
            valoresAgregados.clear()
            valoresQuitados.clear()

            tabla.delete(*tabla.get_children())

            entry_folio_buscar.delete(0, END)
            entry_folio.config(state="normal")
            entry_folio.delete(0, END)
            entry_folio.config(state="disabled")
            entry_cantidad.delete(0, END)
            entry_fecha.delete(0, END)
            combo_proveedor.config(state="normal")
            combo_proveedor.delete(0, END)
            combo_proveedor.config(state="disabled")
            combo_articulo.delete(0, END)

            btn_nuevo.config(state="normal")
            btn_cancelar.config(state="disabled")
            btn_editar.config(state="disabled")
            btn_remover.config(state="disabled")
            btn_guardar.config(state="disabled")
            btn_agregar.config(state="disabled")
            btn_quitar.config(state="disabled")

        def getIdsFromTabla():
            elementos = tabla.get_children()
            idsList = []
            for elemento in elementos:
                valores = tabla.item(elemento, "values")
                idsList.append(int(valores[0]))
            return idsList

        def ventanaEliminarCompra():
            auxCom = com.Compra()
            auxCom.set_folio(int(entry_folio.get()))
            
            confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar la compra con folio {auxCom.get_folio()} y todos sus detalles?")
            if confirmation:
                if app.dbcom.eliminarCompra(auxCom.get_folio()):
                    messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente la compra con folio {auxCom.get_folio()}.")
                    
                    for valor in valoresTabla:
                        valor2 = valoresTabla[valor]
                        print(valor2)
                        artId = int(valor2[3])
                        artCant = int(valor2[2])
                        artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual+artCant)
                        app.dba.actualizarCantArticulo2(artId, artCantActual2-artCant)
                    
                    ventana.focus()

                    valoresTabla.clear()

                    valoresAgregados.clear()
                    valoresQuitados.clear()
                    tabla.delete(*tabla.get_children())
                    entry_folio_buscar.delete(0, END)
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.config(state="disabled")
                    entry_cantidad.delete(0, END)
                    entry_fecha.delete(0, END)
                    combo_proveedor.config(state="normal")
                    combo_proveedor.delete(0, END)
                    combo_proveedor.config(state="disabled")
                    combo_articulo.delete(0, END)

                    btn_nuevo.config(state="normal")
                    btn_cancelar.config(state="disabled")
                    btn_editar.config(state="disabled")
                    btn_remover.config(state="disabled")
                    btn_guardar.config(state="disabled")
                    btn_agregar.config(state="disabled")
                    btn_quitar.config(state="disabled")

                else:
                    messagebox.showerror("Eliminación fallida", "No ha sido posible eliminar la compra.")
                    ventana.focus()
            else:
                ventana.focus()

def ventanaVentas(app: App):
        ventana = tk.Toplevel()
        ventana.config(width=600, height=600, bg="black")
        ventana.title("Ventas")
        
        valoresTabla = {}
        valoresQuitados = []
        valoresAgregados = []

        #isAdmin = app.userLogged.getPerfil() == "Administrador"
        #provsProvIDs = app.dbp.dictProvIDs()
        #provs = []
        #provs_ids = []
        #for prov in provsProvIDs:
        #    provs.append(prov[0])
        #    provs_ids.append(int(prov[1]))
        
        clientesCliIDs = app.dbc.dictClientesId()
        clientes = []
        clientes_ids = []
        for i in clientesCliIDs:
            clientes.append(i[0])
            clientes_ids.append(int(i[1]))
        
        articsArtIDs = app.dba.dictArtIDs()
        arts = []
        arts_ids = []
        for i in articsArtIDs:
            arts.append(i[0])
            arts_ids.append(int(i[1]))

        label_folio_buscar = tk.Label(ventana, text="Ingrese ID a buscar:", bg="black", fg="white")
        label_folio_buscar.place(x=30, y=10)
        entry_folio_buscar = tk.Entry(ventana, width=30)
        entry_folio_buscar.place(x=180, y=10)
        btn_id_buscar = tk.Button(ventana, text="Buscar", command=lambda: buttonBuscar_clicked(), width=10)
        btn_id_buscar.place(x=370, y=10)
        
        label_folio = tk.Label(ventana, text="Folio:", bg="black", fg="white")
        label_folio.place(x=30, y=50)
        entry_folio = tk.Entry(ventana, state="disabled")
        entry_folio.place(x=115, y=50)
        
        label_fecha = tk.Label(ventana, text="Fecha:", bg="black", fg="white")
        label_fecha.place(x=30, y=80)
        entry_fecha = tk.Entry(ventana, width=30)
        entry_fecha.place(x=115, y=80)

        label_cliente = tk.Label(ventana, text="Cliente:", bg="black", fg="white")
        label_cliente.place(x=30, y=110)
        combo_cliente = ttk.Combobox(ventana, values=clientes, width=30)
        combo_cliente.place(x=115, y=110)
        
        label_articulo = tk.Label(ventana, text="Articulo:", bg="black", fg="white")
        label_articulo.place(x=30, y=140)
        combo_articulo = ttk.Combobox(ventana, values=arts, width=30)
        combo_articulo.place(x=115, y=140)
        
        label_cantidad = tk.Label(ventana, text="Cantidad:", bg="black", fg="white")
        label_cantidad.place(x=30, y=170)
        entry_cantidad = tk.Entry(ventana, width=30)
        entry_cantidad.place(x=115, y=170)
        
        frame_botones1 = tk.Frame(ventana, bg="black")
        frame_botones1.place(x=30, y=270)

        columnas = ["Índice", "Folio", "Cantidad", "Articulo ID"]
        
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
        for columna in columnas:
            tabla.heading(columna, text=columna)
            tabla.column(columna, width=10, stretch=tk.YES)

        tabla.place(x=30, y=300, width=500, height=150)

        frame_botones2 = tk.Frame(ventana, bg="black")
        frame_botones2.place(x=30, y=500)
        
        btn_agregar = tk.Button(frame_botones1, text="Agregar", state="disabled", command=lambda: buttonAgregar_clicked())
        btn_quitar = tk.Button(frame_botones1, text="Quitar", state="disabled", command=lambda: buttonQuitar_clicked(tabla.selection()))
        
        btn_nuevo = tk.Button(frame_botones2, text="Nuevo", state="normal", command=lambda: buttonNuevo_clicked())
        btn_guardar = tk.Button(frame_botones2, text="Guardar", state="disabled", command=lambda: buttonGuardar_clicked())
        btn_cancelar = tk.Button(frame_botones2, text="Cancelar", state="disabled", command=lambda: buttonCancelar_clicked())
        btn_editar = tk.Button(frame_botones2, text="Editar", state="disabled", command=lambda: buttonEditar_clicked())
        btn_remover = tk.Button(frame_botones2, text="Remover", state="disabled", command=lambda: ventanaEliminarCompra())
        
        btn_agregar.pack(side="right", padx=5)
        btn_quitar.pack(side="right", padx=5)
        btn_nuevo.pack(side="left", padx=5)
        btn_guardar.pack(side="left", padx=5)
        btn_cancelar.pack(side="left", padx=5)
        btn_editar.pack(side="left", padx=5)
        btn_remover.pack(side="left", padx=5)
        
        def buttonAgregar_clicked():
            
            cantidad_art_aux = int(entry_cantidad.get())
            id_art_aux = arts_ids[arts.index(combo_articulo.get())]
            
            current_storage = app.dba.getCantidadArticulo2(id_art_aux)[0]
            articles_in_table = sum(int(tabla.item(item, "values")[2]) for item in tabla.get_children() if int(tabla.item(item, "values")[3]) == id_art_aux)

            if entry_folio.get() == "" or entry_fecha.get() == "" or combo_cliente.get() == "" or combo_articulo.get() == "" or entry_cantidad.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para agregar el registro.")
                ventana.focus()
            elif not (combo_articulo.get() in arts) or not (combo_cliente.get() in clientes):
                messagebox.showerror("Valores inválidos", "Favor de ingresar valores adecuados.")
                ventana.focus()
            if cantidad_art_aux > (current_storage - articles_in_table):
                messagebox.showerror("Cantidad insuficiente", "No hay suficientes existencias del artículo seleccionado.")
                ventana.focus()
            else:
                try:
                    existencias_a_poner = int(entry_cantidad.get())
                    maxDetalleId = app.dbcom.maxSQL("det_id", "det_venta")[0]
                    
                    if len(getIdsFromTabla()) == 0:
                        if not maxDetalleId:
                            aux_detalle_com_id = 1
                        else:
                            aux_detalle_com_id = maxDetalleId + 1
                    else:
                        if not maxDetalleId:
                            aux_detalle_com_id = max(getIdsFromTabla()) + 1
                        else:
                            aux_detalle_com_id = max(int(maxDetalleId), max(getIdsFromTabla())) + 1
                    
                except Exception as e:
                    messagebox.showerror("Cantidad inválida", "Favor de ingresar un número entero para la cantidad.")
                    print(e)
                    ventana.focus
                    return
                
                if int(entry_cantidad.get()) <= 0:
                    messagebox.showerror("Cantidad inválida", "Favor de ingresar un número entero positivo para la cantidad.")
                    ventana.focus()
                    return
                
                articuloIdsTemp1 = getArticulosIdsFromTabla()
                if arts_ids[arts.index(combo_articulo.get())] in articuloIdsTemp1:
                    for key, value in valoresTabla.items():
                        if value[3] == arts_ids[arts.index(combo_articulo.get())]:
                            existencias_a_poner += int(value[2])
                            print(key)
                            valoresTabla.pop(key)
                            tabla.delete(key)
                            break

                tabla.insert('', 'end', values=(aux_detalle_com_id, entry_folio.get(), existencias_a_poner, arts_ids[arts.index(combo_articulo.get())]))
                valoresAgregados.append([aux_detalle_com_id, entry_folio.get(), existencias_a_poner, arts_ids[arts.index(combo_articulo.get())]])

                valorInt = []
                for i in tabla.item(tabla.get_children()[len(tabla.get_children())-1], "values"):
                    valorInt.append(int(i))
                
                valoresTabla[tabla.get_children()[len(tabla.get_children())-1]] = valorInt
                #print(valoresTabla)

        def buttonQuitar_clicked(seleccion: ttk.Treeview.selection):

            if not seleccion:
                messagebox.showerror("Sin selección", "No hay ningún elemento de la tabla seleccionado.")
                return
            
            valores = tabla.item(seleccion[0], "values")
            #idArt = int(valores[2])
            #cantPieza = int(valores[3])
            #nuevaCantidad = int(app.dbp.getCantidadPieza(idArt)[0]) + cantPieza
            valores = list(valores)
            
            valoresTabla.pop(seleccion[0])
            valoresQuitados.append(valores)
            print(valoresQuitados)

            for i in range(len(valores)):
                valores[i] = int(valores[i])

            #valoresQuitados.append(valores)
            tabla.delete(seleccion[0])

        def buttonBuscar_clicked():

            valoresTabla.clear()
            valoresAgregados.clear()
            valoresQuitados.clear()

            tabla.delete(*tabla.get_children())

            #entry_folio_buscar.delete(0, END)
            entry_folio.config(state="normal")
            entry_folio.delete(0, END)
            entry_folio.config(state="disabled")
            entry_cantidad.delete(0, END)
            entry_fecha.delete(0, END)
            combo_articulo.delete(0, END)
            combo_cliente.delete(0, END)

            btn_nuevo.config(state="normal")
            btn_cancelar.config(state="disabled")
            btn_editar.config(state="disabled")
            btn_remover.config(state="disabled")
            btn_guardar.config(state="disabled")
            btn_agregar.config(state="disabled")
            btn_quitar.config(state="disabled")

            try:
                ven_ = ven.Venta()
                ven_.set_folio(entry_folio_buscar.get())
                auxVen = app.dbv.buscarVenta(ven_, [app.userLogged.getID(), app.userLogged.getPerfil()])
                if auxVen:
                    valoresTabla.clear()
                    clientaux = cli.Cliente()
                    clientaux.setID(auxVen.get_cliente_id())
                    clienteaux2 = app.dbc.buscarCliente(clientaux, [app.userLogged.getID(), app.userLogged.getPerfil()])
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.insert(0, auxVen.get_folio())
                    entry_folio.config(state="disabled")
                    combo_cliente.delete(0, END)
                    combo_cliente.insert(0, clienteaux2.getNombre())
                    entry_fecha.delete(0, END)
                    entry_fecha.insert(0, auxVen.get_fecha())

                    btn_nuevo.config(state="disabled")
                    btn_agregar.config(state="normal")
                    btn_quitar.config(state="normal")
                    btn_editar.config(state="normal")
                    btn_remover.config(state="normal")
                    btn_cancelar.config(state="normal")

                    detalles_venta = app.dbv.detallesVenta(auxVen.get_folio())

                    for detalle in detalles_venta:
                        tabla.insert('', 'end', values=detalle)
                        indiceTabla = tabla.get_children()[len(tabla.get_children())-1]
                        valores = tabla.item(tabla.get_children()[len(tabla.get_children())-1], "values")
                        valoresTabla[indiceTabla] = valores

                    print(valoresTabla)

                else:
                    messagebox.showerror("Venta no encontrada", "La venta no se encuentra registrada en la DB.")
                    ventana.focus()
            except Exception as e:
                messagebox.showerror("Valor no válido", "Favor de ingresar un ID válido.")
                print(e)
                ventana.focus()

        def buttonGuardar_clicked():
            ven_ = ven.Venta()
            ven_.set_folio(int(entry_folio.get()))
            ven_.set_fecha(entry_fecha.get())
            ven_.set_cliente_id(int(clientes_ids[clientes.index(combo_cliente.get())]))

            elementosTabla = tabla.get_children()
            valoresGuardadoTabla = []
            idsArticulos = []
            
            for elemento in elementosTabla:
                valor = tabla.item(elemento, "values")
                valorInt = []
                i = 0
                for columna in valor:
                    i += 1
                    columnaInt = int(columna)
                    valorInt.append(columnaInt)
                    if i == 4:
                        idsArticulos.append(columnaInt)
                valoresGuardadoTabla.append(valorInt)
                
            #for valorAux3 in valoresGuardadoTabla:
                

            if entry_folio.get() == "" or entry_fecha.get() == "" or combo_cliente.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif len(elementosTabla) == 0:
                messagebox.showerror("Compra sin detalles", "Favor de ingresar detalles de la compra.")
                ventana.focus()
                
                

            else:
                auxVenta = ven.Venta()
                auxVenta.set_folio(int(entry_folio.get()))
                auxVenta.set_fecha(entry_fecha.get())
                auxVenta.set_cliente_id(int(clientes_ids[clientes.index(combo_cliente.get())]))

                subtotal = 0

                for valor in valoresGuardadoTabla:
                    precio_venta_art = (app.dba.getPrecioVenta(valor[3])[0][0]) * valor[2]
                    subtotal += precio_venta_art

                ventana2 = tk.Toplevel()
                ventana2.config(width=300, height=300, bg="black")
                ventana2.title("Venta - Confirmación")

                iva = subtotal * .16
                total_a_pagar = subtotal + iva
                puntos_cliente = app.dbc.getPuntos(auxVenta.get_cliente_id())[0][0]
                puntos_a_obtener = int(total_a_pagar/10)

                text_subtotal = "Subtotal: " + str(subtotal)
                text_iva = "IVA: " + str(iva)
                text_total = "Total: " + str(total_a_pagar)

                label_subtotal = tk.Label(ventana2, text=text_subtotal, bg="black", fg="white")
                label_subtotal.place(x=30, y=10)
                label_iva = tk.Label(ventana2, text=text_iva, bg="black", fg="white")
                label_iva.place(x=30, y=40)
                label_total_a_pagar = tk.Label(ventana2, text=text_total, bg="black", fg="white")
                label_total_a_pagar.place(x=30, y=70)

                btn_comprar = tk.Button(ventana2, text="Comprar", command=lambda: buttonComprar(), width=10)
                btn_comprar.place(x=30, y=100)

                if puntos_cliente > 0:
                        confirmation = messagebox.askyesno("¿Desea usar puntos?", f"¿Desea usar los {puntos_cliente} puntos con los que cuenta el cliente para pagar?")
                        if confirmation:
                            total_a_pagar -= puntos_cliente
                            app.dbc.actualizarPuntos(auxVenta.get_cliente_id(), 0)
                            messagebox.showinfo("¡Puntos usados!", f"Su nueva cantidad a pagar serán ${total_a_pagar}.")
                            text_total = "Total: " + str(total_a_pagar)
                            label_total_a_pagar.config(text=text_total, fg="orange")
                            ventana2.focus()

                def buttonComprar():
                    #try:
                        app.dbv.guardarVenta(auxVenta)
                        ventana2.focus()

                        for valor in valoresTabla:
                            valor2 = valoresTabla[valor]
                            print(valor2)
                            artId = int(valor2[3])
                            artCant = int(valor2[2])
                            #artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                            artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                            #app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual+artCant)
                            print(artId)
                            print(artCant)
                            app.dba.actualizarCantArticulo2(artId, artCantActual2-artCant)

                            
                            app.dbv.guardarDetalleVenta(valor2)

                        app.dbc.actualizarPuntos(auxVenta.get_cliente_id(), puntos_a_obtener)
                        messagebox.showinfo("Registro exitoso", f"Se ha registrado correctamente la venta con el folio {auxVenta.get_folio()}. Por esta compra, ha obtenido {puntos_a_obtener}")
                        ventana2.destroy()
                        ventana.focus()
                        
                        valoresTabla.clear()
                        print(valoresTabla)
                        valoresAgregados.clear()
                        valoresQuitados.clear()
                        tabla.delete(*tabla.get_children())
                        entry_folio_buscar.delete(0, END)
                        entry_folio.config(state="normal")
                        entry_folio.delete(0, END)
                        entry_folio.config(state="disabled")
                        entry_cantidad.delete(0, END)
                        entry_fecha.delete(0, END)
                        combo_articulo.delete(0, END)
                        combo_cliente.delete(0, END)

                        btn_nuevo.config(state="normal")
                        btn_cancelar.config(state="disabled")
                        btn_editar.config(state="disabled")
                        btn_remover.config(state="disabled")
                        btn_guardar.config(state="disabled")
                        btn_agregar.config(state="disabled")
                        btn_quitar.config(state="disabled")
                        
                        return


                    #except Exception as e:
                    #    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    #    print(e)

        def buttonNuevo_clicked():
            valoresTabla.clear()
            print(valoresTabla)
            valoresAgregados.clear()
            valoresQuitados.clear()

            maxFolio = app.dbv.maxSQL("folio", "ventas")[0]
            if not maxFolio:
                newFolio = 1
            else:
                newFolio = maxFolio + 1

            entry_folio_buscar.delete(0, END)
            entry_folio.config(state="normal")
            entry_folio.delete(0, END)
            entry_folio.insert(0, newFolio)
            entry_folio.config(state="disabled")
            entry_cantidad.delete(0, END)
            entry_fecha.delete(0, END)
            combo_articulo.delete(0, END)
            combo_cliente.delete(0, END)

            tabla.delete(*tabla.get_children())

            btn_guardar.config(state="normal")
            btn_cancelar.config(state="normal")
            btn_agregar.config(state="normal")
            btn_quitar.config(state="normal")

        def buttonEditar_clicked():
            ven_ = ven.Venta()
            ven_.set_folio(int(entry_folio.get()))

            #if not app.dbr.buscarReparacionMatricula(rep_, [app.userLogged.getID(), app.userLogged.getPerfil()]):
            elementosTabla = tabla.get_children()

            if entry_fecha.get() == "" or combo_cliente.get() == "":
                messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
                ventana.focus()

            elif len(elementosTabla) == 0:
                messagebox.showerror("Compra sin detalles", "Favor de ingresar detalles de la venta.")
                ventana.focus()

            else:
                auxVen = ven.Venta()
                auxVen.set_folio(int(entry_folio.get()))
                auxVen.set_fecha(entry_fecha.get())
                auxVen.set_cliente_id(int(clientes_ids[clientes.index(combo_cliente.get())]))
                try:
                    app.dbv.editarVenta(auxVen)
                    ventana.focus()

                    for valor in valoresAgregados:
                        artId = valor[3]
                        artCant = valor[2]
                        #artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        #app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual-artCant)
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        app.dba.actualizarCantArticulo2(artId, artCantActual2-artCant)

                    for valor in valoresQuitados:
                        artId = valor[3]
                        artCant = valor[2]
                        #artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        #app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual-artCant)
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        app.dba.actualizarCantArticulo2(artId, artCantActual2+artCant)
                        
                        app.dbcom.guardarDetalleCompra(valor)

                    messagebox.showinfo("Registro exitoso", f"Se ha guardado correctamente la venta con el folio {auxVen.get_folio()}.")

                    valoresTabla.clear()
                    valoresAgregados.clear()
                    valoresQuitados.clear()

                    tabla.delete(*tabla.get_children())

                    entry_folio_buscar.delete(0, END)
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.config(state="disabled")
                    entry_cantidad.delete(0, END)
                    entry_fecha.delete(0, END)
                    combo_articulo.delete(0, END)
                    combo_cliente.delete(0, END)

                    btn_nuevo.config(state="normal")
                    btn_cancelar.config(state="disabled")
                    btn_editar.config(state="disabled")
                    btn_remover.config(state="disabled")
                    btn_guardar.config(state="disabled")
                    btn_agregar.config(state="disabled")
                    btn_quitar.config(state="disabled")

                except Exception as e:
                    messagebox.showerror("Error", "Hubo un error al intentar ingresar el registro. Revisa tus datos.")
                    print(e)

            #else:
            #    messagebox.showerror("Folio existente con otra matricula", "El folio que se intenta guardar ya está guardado con otra matricula.")

        def buttonCancelar_clicked():

            valoresTabla.clear()
            valoresAgregados.clear()
            valoresQuitados.clear()

            tabla.delete(*tabla.get_children())

            entry_folio_buscar.delete(0, END)
            entry_folio.config(state="normal")
            entry_folio.delete(0, END)
            entry_folio.config(state="disabled")
            entry_cantidad.delete(0, END)
            entry_fecha.delete(0, END)
            combo_articulo.delete(0, END)
            combo_cliente.delete(0, END)

            btn_nuevo.config(state="normal")
            btn_cancelar.config(state="disabled")
            btn_editar.config(state="disabled")
            btn_remover.config(state="disabled")
            btn_guardar.config(state="disabled")
            btn_agregar.config(state="disabled")
            btn_quitar.config(state="disabled")

        def getIdsFromTabla():
            elementos = tabla.get_children()
            idsList = []
            for elemento in elementos:
                valores = tabla.item(elemento, "values")
                idsList.append(int(valores[0]))
            return idsList

        def getArticulosIdsFromTabla():
            elementos = tabla.get_children()
            idsList = []
            for elemento in elementos:
                valores = tabla.item(elemento, "values")
                idsList.append(int(valores[3]))
            return idsList

        def ventanaEliminarCompra():
            auxVen = ven.Venta()
            auxVen.set_folio(int(entry_folio.get()))
            
            confirmation = messagebox.askyesno("¿Desea continuar?", f"¿Desea eliminar la venta con folio {auxVen.get_folio()} y todos sus detalles?")
            if confirmation:
                if app.dbv.eliminarVenta(auxVen.get_folio()):
                    messagebox.showinfo("Eliminación exitosa", f"Se ha eliminado satisfactoriamente la venta con folio {auxVen.get_folio()}.")
                    
                    for valor in valoresTabla:
                        valor2 = valoresTabla[valor]
                        print(valor2)
                        artId = int(valor2[3])
                        artCant = int(valor2[2])
                        #artCantActual = int(app.dba.getCantidadArticulo(artId, proveedor[0])[0])
                        artCantActual2 = int(app.dba.getCantidadArticulo2(artId,)[0])
                        #app.dba.actualizarCantArticulo(proveedor[0], artId, artCantActual+artCant)
                        app.dba.actualizarCantArticulo2(artId, artCantActual2+artCant)
                    
                    ventana.focus()

                    valoresTabla.clear()

                    valoresAgregados.clear()
                    valoresQuitados.clear()
                    tabla.delete(*tabla.get_children())
                    entry_folio_buscar.delete(0, END)
                    entry_folio.config(state="normal")
                    entry_folio.delete(0, END)
                    entry_folio.config(state="disabled")
                    entry_cantidad.delete(0, END)
                    entry_fecha.delete(0, END)
                    combo_articulo.delete(0, END)
                    combo_cliente.delete(0, END)

                    btn_nuevo.config(state="normal")
                    btn_cancelar.config(state="disabled")
                    btn_editar.config(state="disabled")
                    btn_remover.config(state="disabled")
                    btn_guardar.config(state="disabled")
                    btn_agregar.config(state="disabled")
                    btn_quitar.config(state="disabled")

                else:
                    messagebox.showerror("Eliminación fallida", "No ha sido posible eliminar la venta.")
                    ventana.focus()
            else:
                ventana.focus()

login=Login()
login.mainloop()