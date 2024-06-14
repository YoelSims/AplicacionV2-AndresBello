import os
import sys
from interfaz import *

class ventanaPrincipal(QMainWindow):
    def _init_(self, parent=None):
        QMainWindows.__init__(self)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        ###########################
        # Mostrar Ventana
        ##########################
        self.show()

#Ejecutar Aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #######
    windows = ventanaPrincipal()
    windows.show()
    sys.exit(app.exec_())