import sqlite3

from PyQt6 import QtWidgets,QtSql,QtCore
import sys

import conexion
import var
from datetime import date
class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            return False;
        else:
            return True;

    def insertarTrastero(self):
        query = QtSql.QSqlQuery()
        query.prepare("insert into trasteros (M2, Precio, Alquilado) VALUES( :m2, :precio, :alquilado)")
        query.bindValue(":m2",var.ui.edtM2.text())
        query.bindValue(":precio",var.ui.edtPrecio.text())
        if var.ui.rbtSi.isChecked():
            query.bindValue(":alquilado","si")
        elif var.ui.rbtNo.isChecked():
            query.bindValue(":alquilado", "no")
        if query.exec():
            conexion.Conexion.mostrarTrasteros(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Trastero insertado')
            msg.exec()
            #var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarTrasteros(self)
            conexion.Conexion.cargarTrasteros(self)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()
    def bajaTrastero(self):
        fila = var.ui.tableTrasteros.currentRow()
        id = var.ui.tableTrasteros.item(fila,0).text()
        query = QtSql.QSqlQuery()
        query.prepare('update trasteros set FechaBaja = :fechabaja where Id_trastero=:id')
        query.bindValue(':fechabaja',str(date.today()))
        query.bindValue(':id', id)
        if query.exec():
            conexion.Conexion.mostrarTrasteros(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Trastero dado de baja')
            msg.exec()
            #var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarTrasteros(self)
            conexion.Conexion.cargarTrasteros(self)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()
    def mostrarTrasteros(self):
        if var.ui.rbtLibres.isChecked():
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select Id_trastero, M2, Precio, Alquilado, FechaBaja from trasteros where Alquilado = "no"  AND FechaBaja IS NULL')
            if query.exec():
                while query.next():
                    Id = query.value(0)
                    M2 = query.value(1)
                    Precio = query.value(2)
                    Alquilado = query.value(3)
                    FechaBaja = query.value(4)
                    var.ui.tableTrasteros.setRowCount(index + 1)
                    var.ui.tableTrasteros.setItem(index, 0, QtWidgets.QTableWidgetItem(str(Id)))
                    var.ui.tableTrasteros.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tableTrasteros.setItem(index, 1, QtWidgets.QTableWidgetItem(str(M2)))
                    var.ui.tableTrasteros.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tableTrasteros.setItem(index, 2, QtWidgets.QTableWidgetItem(str(Precio)))
                    var.ui.tableTrasteros.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
                    var.ui.tableTrasteros.setItem(index, 3, QtWidgets.QTableWidgetItem(str(Alquilado)))
                    var.ui.tableTrasteros.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tableTrasteros.setItem(index, 4, QtWidgets.QTableWidgetItem(str(FechaBaja)))
                    var.ui.tableTrasteros.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index += 1
        elif var.ui.rbtTodos.isChecked():
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select Id_trastero, M2, Precio, Alquilado, FechaBaja from trasteros')
            if query.exec():
                while query.next():
                    Id = query.value(0)
                    M2 = query.value(1)
                    Precio = query.value(2)
                    Alquilado = query.value(3)
                    FechaBaja = query.value(4)
                    var.ui.tableTrasteros.setRowCount(index + 1)
                    var.ui.tableTrasteros.setItem(index, 0, QtWidgets.QTableWidgetItem(str(Id)))
                    var.ui.tableTrasteros.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tableTrasteros.setItem(index, 1, QtWidgets.QTableWidgetItem(str(M2)))
                    var.ui.tableTrasteros.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tableTrasteros.setItem(index, 2, QtWidgets.QTableWidgetItem(str(Precio)))
                    var.ui.tableTrasteros.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
                    var.ui.tableTrasteros.setItem(index, 3, QtWidgets.QTableWidgetItem(str(Alquilado)))
                    var.ui.tableTrasteros.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tableTrasteros.setItem(index, 4, QtWidgets.QTableWidgetItem(str(FechaBaja)))
                    var.ui.tableTrasteros.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index += 1
    def cargarTrastero(self):
        fila = var.ui.tableTrasteros.currentRow()
        id = var.ui.tableTrasteros.item(fila, 0).text()
        m2 = var.ui.tableTrasteros.item(fila, 1).text()
        precio = var.ui.tableTrasteros.item(fila, 2).text()
        alquilado = var.ui.tableTrasteros.item(fila, 3).text()
        var.ui.edtM2.setText(m2)
        var.ui.edtPrecio.setText(precio)
        var.ui.lblid.setText(id)
        if alquilado == "si":
            var.ui.rbtSi.setChecked(True)
        elif alquilado =="no":
            var.ui.rbtNo.setChecked(True)
    def modificarTrastero(self):
        m2 = var.ui.edtM2.text()
        precio = var.ui.edtPrecio.text()
        id = var.ui.lblid.text()
        alquilado = "si"
        fila = var.ui.tableTrasteros.currentRow()
        if var.ui.rbtNo.isChecked():
            alquilado = "no"
        query = QtSql.QSqlQuery()
        query.prepare('update trasteros set M2 = :m2, Precio = :precio, Alquilado = :alquilado where Id_trastero=:id')
        query.bindValue(':m2', m2)
        query.bindValue(':id', id)
        query.bindValue(':precio',precio)
        query.bindValue(':alquilado',alquilado)
        if query.exec():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Trastero actualizado')
            msg.exec()
            #var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarTrasteros(self)
            conexion.Conexion.cargarTrasteros(self)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()
    def insertarCliente(self):
        query = QtSql.QSqlQuery()
        query.prepare("insert into clientes (Nombre, Telefono, Direccion) VALUES( :nombre, :telefono, :direccion)")
        query.bindValue(":nombre", var.ui.edtNombreCliente.text())
        query.bindValue(":telefono", var.ui.edtTelefonoCliente.text())
        query.bindValue(":direccion", var.ui.edtDireccionCliente.text())
        if query.exec():
            conexion.Conexion.cargarClientes(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Cliente insertado')
            msg.exec()
            # var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarClientes(self)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()

    def mostrarClientes(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare(
            'select Id_cliente, Nombre, Telefono, Direccion, FechaBaja from Clientes')
        if query.exec():
            while query.next():
                Id = query.value(0)
                Nombre = query.value(1)
                Telefono = query.value(2)
                Direccion = query.value(3)
                FechaBaja = query.value(4)
                var.ui.tableClientes.setRowCount(index + 1)
                var.ui.tableClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(Id)))
                var.ui.tableClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tableClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(Nombre)))
                var.ui.tableClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tableClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(Telefono)))
                var.ui.tableClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
                var.ui.tableClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(Direccion)))
                var.ui.tableClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tableClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(FechaBaja)))
                var.ui.tableClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
    def cargarCliente(self):
        fila = var.ui.tableClientes.currentRow()
        id = var.ui.tableClientes.item(fila, 0).text()
        nombre = var.ui.tableClientes.item(fila, 1).text()
        telefono = var.ui.tableClientes.item(fila, 2).text()
        direccion = var.ui.tableClientes.item(fila, 3).text()
        var.ui.edtNombreCliente.setText(nombre)
        var.ui.edtTelefonoCliente.setText(telefono)
        var.ui.edtDireccionCliente.setText(direccion)
        var.ui.lblid_cliente.setText(id)
    def bajaCliente(self):
        fila = var.ui.tableClientes.currentRow()
        id = var.ui.tableClientes.item(fila, 0).text()
        query = QtSql.QSqlQuery()
        query.prepare('update Clientes set FechaBaja = :fechabaja where Id_cliente=:id')
        query.bindValue(':fechabaja', str(date.today()))
        query.bindValue(':id', id)
        if query.exec():
            conexion.Conexion.cargarClientes(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Cliente dado de baja')
            msg.exec()
            # var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarClientes(self)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()
    def cargarTrasteros(self):
        var.ui.cmbTrasteros.clear()
        query = QtSql.QSqlQuery()
        query.prepare(
            'select Id_trastero from trasteros where Alquilado = "no" and FechaBaja IS NULL')
        if query.exec():
            while query.next():
                Id = query.value(0)
                var.ui.cmbTrasteros.addItem(str(Id))
    def cargarClientes(self):
        var.ui.cmbClientes.clear()
        query = QtSql.QSqlQuery()
        query.prepare(
            'select Id_cliente from Clientes where FechaBaja IS NULL')
        if query.exec():
            while query.next():
                Id = query.value(0)
                var.ui.cmbClientes.addItem(str(Id))
    def mostrarAlquileres(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare(
            'select Id_trastero, Cliente, FechaAlquiler, FechaAlquilerFinal from trasteros where Alquilado = "si" and FechaBaja IS NULL')
        if query.exec():
            while query.next():
                Id = query.value(0)
                Cliente = query.value(1)
                FechaAlquiler = query.value(2)
                FechaFinalAlquiler = query.value(3)
                var.ui.tableAlquileres.setRowCount(index + 1)
                var.ui.tableAlquileres.setItem(index, 1, QtWidgets.QTableWidgetItem(str(Id)))
                var.ui.tableAlquileres.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tableAlquileres.setItem(index, 0, QtWidgets.QTableWidgetItem(str(Cliente)))
                var.ui.tableAlquileres.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tableAlquileres.setItem(index, 2, QtWidgets.QTableWidgetItem(str(FechaAlquiler)))
                var.ui.tableAlquileres.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
                var.ui.tableAlquileres.setItem(index, 3, QtWidgets.QTableWidgetItem(str(FechaFinalAlquiler)))
                var.ui.tableAlquileres.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
                index += 1

    def alquilarTrastero(self):
        trastero = var.ui.cmbTrasteros.currentText()
        cliente = var.ui.cmbClientes.currentText()
        fecha = var.ui.edtFechaAlquiler.text()
        fechaFinal = var.ui.edtFechaAlquilerFinal.text()
        query = QtSql.QSqlQuery()
        query.prepare('update trasteros set Cliente = :cliente, FechaAlquiler = :fecha, FechaAlquilerFinal = :fechaFinal, Alquilado = "si" where Id_trastero=:id')
        query.bindValue(':cliente', cliente)
        query.bindValue(':id', trastero)
        query.bindValue(':fecha', fecha)
        query.bindValue(':fechaFinal',fechaFinal)
        if query.exec():
            conexion.Conexion.mostrarAlquileres(self)
            conexion.Conexion.cargarTrasteros(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Alquiler realizado')
            msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()
    def desalquilarTrastero(self):
        fila = var.ui.tableAlquileres.currentRow()
        id = var.ui.tableAlquileres.item(fila, 1).text()
        query = QtSql.QSqlQuery()
        query.prepare('update trasteros set Alquilado = "no" where Id_trastero=:id')
        query.bindValue(':id', id)
        if query.exec():
            conexion.Conexion.cargarTrasteros(self)
            conexion.Conexion.mostrarAlquileres(self)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Trastero liberado')
            msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()
    def cargarFecha(qDate):
        try:
            data = ('{0}-{1}-{2}'.format(qDate.year(),qDate.month(),qDate.day()))
            var.ui.edtFechaAlquiler.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error al cargar la fecha: %s ' % str(error))
    def cargarFecha2(qDate):
        try:
            data = ('{0}-{1}-{2}'.format(qDate.year(),qDate.month(),qDate.day()))
            var.ui.edtFechaAlquilerFinal.setText(str(data))
            var.dlgcalendar2.hide()
        except Exception as error:
            print('Error al cargar la fecha: %s ' % str(error))
