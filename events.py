import conexion
import var
from PyQt6 import QtWidgets
import sys
def btn_instertar(self):
    conexion.Conexion.insertarTrastero(self)
def btn_baja(self):
    conexion.Conexion.bajaTrastero(self)
def btn_modif(self):
    conexion.Conexion.modificarTrastero(self)
def btnInsertarCliente(self):
    conexion.Conexion.insertarCliente(self)
def btnBajaCliente(self):
    conexion.Conexion.bajaCliente(self)
def limpiar(self):
    var.ui.edtM2.setText('')
    var.ui.edtPrecio.setText('')
    var.ui.lblid.setText('')
    var.ui.lblid_cliente.setText('')
    var.ui.edtNombreCliente.setText('')
    var.ui.edtDireccionCliente.setText('')
    var.ui.edtTelefonoCliente.setText('')
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('Aviso')
    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
    msg.setText('Datos limpiados')
    msg.exec()
def salir(self):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('Aviso')
    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
    msg.setText('¿Desea salir?')
    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
    res = msg.exec()
    if res == QtWidgets.QMessageBox.StandardButton.Ok:
        sys.exit()
    else:
        msg.hide()
def cargarTrasteros(self):
    conexion.Conexion.cargarTrasteros(self)
def cargarClientes(self):
    conexion.Conexion.cargarClientes(self)
def btnAlquilarTrastero(self):
    conexion.Conexion.alquilarTrastero(self)