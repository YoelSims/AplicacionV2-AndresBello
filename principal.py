import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interfaz import *
from iconosNegros_rc import *
from iconosBlancos_rc import *
from imagenesGeneral_rc import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        ###########################
        # Mostrar Ventana
        ##########################
        self.show()

# Ejecutar Aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())