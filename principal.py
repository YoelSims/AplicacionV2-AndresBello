#import os
import sys
from interfaz import *
########################################################################
# Importacion de Modulos Personalizados Widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################
from _icons_rc import *
from iconosNegros_rc import *
from iconosBlancos_rc import *
from imagenesGeneral_rc import *
#Importacion de Funciones
from Funciones.funcionesgeneral import *
from BaseDatos.basededatos import init_db

settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        ########################################################################
        # Aplicando Estilos JSON
        loadJsonStyle(self, self.ui)
        ###########################
        # Mostrar Ventana
        self.show()
       
        QAppSettings.updateAppSettings(self)
        
        # Iniciar Base de Datos y Generar Tablas
        init_db()
        #Llamando las Funciones
        self.app_functions = AppFunctions(self.ui)
        #Botones Funciones Principales
        self.ui.actualizarBoton.clicked.connect(self.app_functions.add_user)
        self.ui.eliminarBoton.clicked.connect(self.app_functions.delete_user)
        self.ui.editarBoton.clicked.connect(self.app_functions.update_user)

        # Mostrar tablas inicialmente
        self.app_functions.display_users()
        
        ##############
        #Actualizar Tema
        ##############
        ## Expandir Menu Central Botones
        self.ui.ajustesBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        self.ui.acercaDeBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        self.ui.ayudaBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        ##############
        ## Expandir Menu Derecho Botones
        self.ui.masBoton.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        self.ui.perfilBoton.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        self.ui.botonMenuEliminar.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        #################
        ### Cerrar Menu Central Botones
        self.ui.cerrarMenuCentro.clicked.connect(lambda: self.ui.menuCentroContenedor.collapseMenu())
        #################
        ### Cerrar Menu Derecho
        self.ui.cerrarMenuDerecho.clicked.connect(lambda: self.ui.menuContenedorDerecho.collapseMenu())
        #################
        ### Cerrar Notificacion
        self.ui.cerrarNotificacion.clicked.connect(lambda: self.ui.emergenteNotificacionContenedor.collapseMenu())
        
# Ejecutar Aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
