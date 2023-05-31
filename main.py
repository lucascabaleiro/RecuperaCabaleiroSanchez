import conexion
from PyQt6 import QtWidgets, QtSql
import sys

import informes
import var

import events
from ventanamain import *
from events import *
from dialogcalendar import *
import datetime
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_Main()
        var.dlgcalendar = DialogCalendar()
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
        var.ui.btnAltaCliente.clicked.connect(events.btnInsertarCliente)
        var.ui.tableClientes.clicked.connect(conexion.Conexion.cargarCliente)
        var.ui.btnBajaCliente.clicked.connect(events.btnBajaCliente)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listClientes)
        conexion.Conexion.mostrarClientes(self)
        events.cargarTrasteros(self)
        events.cargarClientes(self)
        conexion.Conexion.mostrarAlquileres(self)
        var.ui.btnCrearAlquiler.clicked.connect(events.btnAlquilarTrastero)
        var.ui.btnBajaAlquiler.clicked.connect(events.btnBajaAlquiler)
        var.ui.btnCalendar.clicked.connect(events.abrirCalendar)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_Dialog()
        var.dlgcalendar.setupUi(self)
        dia = datetime.datetime.now().day
        mes = datetime.datetime.now().month
        ano = datetime.datetime.now().year
        var.dlgcalendar.calendar.clicked.connect(conexion.Conexion.cargarFecha)


if __name__ == '__main__':
    conexion.Conexion.db_connect('bdrecupera.db')
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())