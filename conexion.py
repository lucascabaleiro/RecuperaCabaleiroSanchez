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
            print('Conexión incorrecta')
            return False;
        else:
            print('Conexion correcta')
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
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Trastero insertado')
            msg.exec()
            #var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarTrasteros(self)
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
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Trastero dado de baja')
            msg.exec()
            #var.ui.tableTrasteros.clear()
            conexion.Conexion.mostrarTrasteros(self)
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
            query.prepare('select Id_trastero, M2, Precio, Alquilado, FechaBaja from trasteros where Alquilado = "no" and FechaBaja IS NULL')
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
        print("aaaa")
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
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(query.lastError().text())
            msg.exec()