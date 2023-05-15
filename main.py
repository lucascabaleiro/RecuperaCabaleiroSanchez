import conexion
from PyQt6 import QtWidgets
import sys

import informes
import var

import events
from ventanamain import *
from events import *
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_Main()
        var.ui.setupUi(self)
        var.ui.btnAlta.clicked.connect(events.btn_instertar)
        var.ui.btnBaja.clicked.connect(events.btn_baja)
        var.ui.btnModif.clicked.connect(events.btn_modif)
        conexion.Conexion.mostrarTrasteros(self)
        var.ui.rbtTodos.clicked.connect(conexion.Conexion.mostrarTrasteros)
        var.ui.rbtLibres.clicked.connect(conexion.Conexion.mostrarTrasteros)
        var.ui.tableTrasteros.clicked.connect(conexion.Conexion.cargarTrastero)
        var.ui.btnLimpiar.triggered.connect(events.limpiar)
        var.ui.btnSalir.triggered.connect(events.salir)
        var.ui.actionSalir.triggered.connect(events.salir)
        var.ui.actionListado_Trasteros.triggered.connect(informes.Informes.listTrasteros)

if __name__ == '__main__':
    conexion.Conexion.db_connect('bdrecupera.db')
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())