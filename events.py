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
def limpiar(self):
    var.ui.edtM2.setText('')
    var.ui.edtPrecio.setText('')
    var.ui.lblid.setText('')
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