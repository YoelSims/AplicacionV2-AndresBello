 """dbfolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'BaseDatos/basedatos.db'))
        #Crear Base de Datos y Filas
        AppFunctions.main(dbfolder)
        #Mostrar Filas en la Tabla
        AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbfolder))
        #Agregar Nuevo Usuario
        self.ui.actualizarBoton.clicked.connect(lambda: AppFunctions.addUser(self, dbfolder))
        #self.ui.actualizarBoton.clicked.connect(lambda: self.add_user_action())"""
import os
import sys
import sqlite3
from sqlite3 import Error
from PySide2.QtWidgets import QTableWidgetItem

class AppFunctions():
    def __init__(self,arg):
        super(AppFunctions, self).__init__()
        self.arg=arg
        
    
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        
        return conn
    
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
    
    def main(dbFolder):
        create_user_table ="""  CREATE TABLE IF NOT EXISTS Users (
                                                USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                USER_NAME TEXT,
                                                USER_EMAIL TEXT,
                                                USER_PHONE TEXT,
                                                USER_CEDULA TEXT
                                        );
                                    """
        conn = AppFunctions.create_connection(dbFolder)
        
        #CrearTablas
        if conn is not None:
            AppFunctions.create_table(conn, create_user_table)
        else:
            print("Erro nosepuedecrearconexionconlabasededatos")
        
    #Obtener todos los usuarios
    def getAllUsers(dbfolder):
        conn = AppFunctions.create_connection(dbfolder)
        
        get_all_users = """
                            SELECT * FROM Users;
                        """
        try:
            c = conn.cursor()
            c.execute(get_all_users)
            #Devolver Las Tablas
            return c
        except Error as e:
            print(e)
        
    def addUser(self, dbfolder):
        #Crear Conexion Base de Datos
        conn = AppFunctions.create_connection(dbfolder)
        
        #Obtener Valores Ingresados
        nombre =  self.ui.nombre.text()
        apellido =  self.ui.apellido.text()
        cedula = self.ui.cedula.text()
        correo = self.ui.correo.text()
        
        #Insertar Datos Declaracion SQL
        insert_person_data_sql = f"""
        INSERT INTO Users (USER_NAME, USER_EMAIL, USER_PHONE, USER_CEDULA) VALUES ('{nombre}','{apellido}','{cedula}','{correo}');
        """
        #Ejecutar Codigo SQL
        if not conn.cursor().execute(insert_person_data_sql):
            print("No se inserto eso")
        else:
            conn.commit()
            #Limpiar el formulario
            self.ui.nombre.setText("")
            self.ui.apellido.setText("")
            self.ui.cedula.setText("")
            self.ui.correo.setText("")
            #Cargar el nuevo usuario mostrado en la tabla
            AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbfolder))
    
    #Mostrar Usuarios
    def displayUsers(self, rows):
        #Iterar a traves de las filas
        for row in rows:
            rowPosition = self.ui.tableWidget.rowCount()
            #Omitir las filas que ya fueron cargadas
            if rowPosition > row[0]:
                continue
            
            itemCount = 0
            
            #Crear nuevas filas en la tabla
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)
            
            #Agregar Valores a las filas para mostrar
            for item in row:
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))
                
                itemCount = itemCount+1
            rowPosition = rowPosition+1