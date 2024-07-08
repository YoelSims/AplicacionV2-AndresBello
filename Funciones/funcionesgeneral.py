from PySide2.QtWidgets import QTableWidgetItem
from Modelos.modelo import Usuarios
from BaseDatos.basededatos import SessionLocal
from sqlalchemy import *

class AppFunctions:
    def __init__(self, ui):
        self.ui = ui

    def get_all_users(self):
        with SessionLocal() as session:
            return session.query(Usuarios).all()
        
    def add_user(self):
        with SessionLocal() as session:
            cedula = self.ui.cedula.text()
            nombre = self.ui.nombre.text()
            apellido = self.ui.apellido.text()
            telefono = self.ui.telefono.text()
            correo = self.ui.correo.text()

            nuevo_usuario = Usuarios(
                cedula=cedula,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                correo=correo
            )
            session.add(nuevo_usuario)
            session.commit()

        self.ui.cedula.setText("")
        self.ui.nombre.setText("")
        self.ui.apellido.setText("")
        self.ui.telefono.setText("")
        self.ui.correo.setText("")

        self.display_users()
    
    def delete_user(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            user_item = self.ui.tableWidget.item(selected_row, 0)
            if user_item:
                user_id = user_item.text()
                if user_id:
                    try:
                        with SessionLocal() as session:
                            user_to_delete = session.query(Usuarios).filter(Usuarios.id_usuario == user_id).first()
                            if user_to_delete:
                                session.delete(user_to_delete)
                                session.commit()
                                self.display_users()
                            else:
                                print(f"User with ID {user_id} not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print("Selected user ID is empty.")
            else:
                print("No user item found in the selected row.")
        else:
            print("No row selected.")

    def update_user(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            user_item = self.ui.tableWidget.item(selected_row, 0)
            if user_item:
                user_id = user_item.text()
                if user_id:
                    cedula = self.ui.cedulaEliminar.text()
                    nombre = self.ui.nombreActualizar.text()
                    apellido = self.ui.apellidoActualizar.text()
                    telefono = self.ui.telefonoActualizar.text()
                    correo = self.ui.correoActualizar.text()

                    try:
                        with SessionLocal() as session:
                            user_to_update = session.query(Usuarios).filter(Usuarios.id_usuario == user_id).first()
                            if user_to_update:
                                user_to_update.cedula = cedula
                                user_to_update.nombre = nombre
                                user_to_update.apellido = apellido
                                user_to_update.telefono = telefono
                                user_to_update.correo = correo
                                session.commit()
                                self.display_users()
                                print(f"User with ID {user_id} has been updated.")
                            else:
                                print(f"User with ID {user_id} not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print("Selected user ID is empty.")
            else:
                print("No user item found in the selected row.")
        else:
            print("No row selected.")
            
    def display_users(self):
        users = self.get_all_users()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(6)
        for row_number, user in enumerate(users):
            self.ui.tableWidget.insertRow(row_number)
            self.ui.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(user.id_usuario)))
            self.ui.tableWidget.setItem(row_number, 1, QTableWidgetItem(user.cedula))
            self.ui.tableWidget.setItem(row_number, 2, QTableWidgetItem(user.nombre))
            self.ui.tableWidget.setItem(row_number, 3, QTableWidgetItem(user.apellido))
            self.ui.tableWidget.setItem(row_number, 4, QTableWidgetItem(user.telefono))
            self.ui.tableWidget.setItem(row_number, 5, QTableWidgetItem(user.correo))