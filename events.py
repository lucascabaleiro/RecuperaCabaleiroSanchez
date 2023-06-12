import os.path
import shutil
import zipfile

import conexion
import var
from PyQt6 import QtWidgets
import sys, xlwt
import datetime
from PyQt6 import QtWidgets,QtSql,QtCore
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
    var.ui.edtFechaAlquiler.setText('')
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
def btnBajaAlquiler(self):
    conexion.Conexion.desalquilarTrastero(self)
def abrirCalendar(self):
    try:
        var.dlgcalendar.show()
    except Exception as error:
        print('Error: %s ' % str(error))
def abrirCalendar2(self):
    try:
        var.dlgcalendar2.show()
    except Exception as error:
        print('Error: %s ' % str(error))
def crearBackup(self):
    try:
        fecha = datetime.datetime.today()
        fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
        copia = (str(fecha)+'_backup.zip')
        directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar copia',copia,'.zip')
        if var.dlgabrir.accept and filename != '':
            fichzip = zipfile.ZipFile(copia,'w')
            fichzip.write('bdrecupera.db',os.path.basename('bdrecupera.db'),zipfile.ZIP_DEFLATED)
            fichzip.close()
            shutil.move(str(copia),str(directorio))
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Copia de seguridad creada')
            msg.exec()
    except Exception as error:
        print('Error crear backup', error)
def restaurarBackup(self):
    try:
        filename = var.dlgabrir.getOpenFileName(None,'Restaurar Copia Seguridad','','*.zip;;All Files (*)')
        if var.dlgabrir.accept and filename != '':
            file = filename[0]
            with zipfile.ZipFile(str(file),'r') as bbdd:
                bbdd.extractall(pwd=None)
            bbdd.close()
        conexion.Conexion.db_connect('bdrecupera.db')
        conexion.Conexion.mostrarTrasteros(self)
        conexion.Conexion.mostrarAlquileres(self)
        conexion.Conexion.mostrarClientes(self)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Aviso')
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText('Copia de Seguridad Restaurada')
        msg.exec()
    except Exception as error:
        print('Error crear backup', error)
def exportarDatos(self):
    try:
        fecha = datetime.datetime.today()
        fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
        file = (str(fecha) + '_Datos.xls')
        directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Datos',
                                                            file, '.xls')
        wb = xlwt.Workbook()
        sheet1 = wb.add_sheet('Trasteros')
        sheet1.write(0, 0, 'Id_trastero')
        sheet1.write(0, 1, 'M2')
        sheet1.write(0, 2, 'Precio')
        sheet1.write(0, 3, 'Alquilado')
        sheet1.write(0, 4, 'FechaBaja')
        sheet1.write(0, 5, 'Cliente')
        sheet1.write(0, 6, 'FechaAlquiler')
        fila = 1
        query = QtSql.QSqlQuery()
        query.prepare('select * from trasteros order by Id_trastero')
        if query.exec():
            while query.next():
                sheet1.write(fila, 0, str(query.value(0)))
                sheet1.write(fila, 1, str(query.value(1)))
                sheet1.write(fila, 2, str(query.value(2)))
                sheet1.write(fila, 3, str(query.value(3)))
                sheet1.write(fila, 4, str(query.value(4)))
                sheet1.write(fila, 5, str(query.value(5)))
                sheet1.write(fila, 6, str(query.value(6)))
                fila += 1
        sheet2 = wb.add_sheet('Clientes')
        sheet2.write(0, 0, 'Id_cliente')
        sheet2.write(0, 1, 'Nombre')
        sheet2.write(0, 2, 'Telefono')
        sheet2.write(0, 3, 'Direccion')
        sheet2.write(0, 4, 'FechaBaja')
        fila = 1
        query1 = QtSql.QSqlQuery()
        query1.prepare('select * from Clientes order by Id_cliente')
        if query1.exec():
            while query1.next():
                sheet2.write(fila, 0, str(query1.value(0)))
                sheet2.write(fila, 1, str(query1.value(1)))
                sheet2.write(fila, 2, str(query1.value(2)))
                sheet2.write(fila, 3, str(query1.value(3)))
                sheet2.write(fila, 4, str(query1.value(4)))
                fila += 1
        wb.save(directorio)
        msg = QtWidgets.QMessageBox()
        msg.setModal(True)
        msg.setWindowTitle('Aviso')
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText('Exportación de Datos Realizada')
        msg.exec()
    except Exception as error:
        print('Error exportar datos', error)