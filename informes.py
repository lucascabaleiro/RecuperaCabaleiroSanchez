import os, var, shutil
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime
from dateutil import parser
import conexion
import informes


class Informes:
    def listClientes(self):
        try:
            name = datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '_listadoClientes.pdf'
            file = 'informes/' + name
            var.report = canvas.Canvas(file)
            titulo = 'LISTADO CLIENTES'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            items = ['ID', 'Nombre', 'Telefono', 'Direccion', 'FechaBaja']
            var.report.setFont('Helvetica-Bold', size= 10)
            var.report.drawString(65, 675, str(items[0]))
            var.report.drawString(130, 675, str(items[1]))
            var.report.drawString(270, 675, str(items[2]))
            var.report.drawString(370, 675, str(items[3]))
            var.report.drawString(460, 675, str(items[4]))
            var.report.line(50,670,525,670)
            query = QtSql.QSqlQuery()
            query.prepare('select Id_cliente, Nombre, Telefono, Direccion, FechaBaja '
                          'from Clientes order by Id_cliente')
            var.report.setFont('Helvetica', size = 9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(460,90, 'Página siguiente...')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(60, 675, str(items[0]))
                        var.report.drawString(130, 675, str(items[1]))
                        var.report.drawString(270, 675, str(items[2]))
                        var.report.drawString(370, 675, str(items[3]))
                        var.report.drawString(460, 675, str(items[4]))
                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 660
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i,j, str(query.value(0)))
                    var.report.drawString(i+70,j,str(query.value(1)))
                    var.report.drawString(i+215,j, str(query.value(2)))
                    var.report.drawString(i+325,j, str(query.value(3)))
                    var.report.drawString(i+410,j, str(query.value(4)))
                    j = j - 25
            var.report.save()
            rootPath = '.\\informes'
            os.startfile('%s\%s' % (rootPath, name))

        except Exception as error:
            print('Error informes estado clientes' %str(error))
    def listTrasteros(self):
        try:
            name = datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '_listadoTrasteros.pdf'
            file = 'informes/' + name
            var.report = canvas.Canvas(file)
            titulo = 'LISTADO TRASTEROS'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            items = ['ID', 'M2', 'Precio', 'Alquilado', 'FechaBaja']
            var.report.setFont('Helvetica-Bold', size= 10)
            var.report.drawString(65, 675, str(items[0]))
            var.report.drawString(130, 675, str(items[1]))
            var.report.drawString(270, 675, str(items[2]))
            var.report.drawString(370, 675, str(items[3]))
            var.report.drawString(460, 675, str(items[4]))
            var.report.line(50,670,525,670)
            query = QtSql.QSqlQuery()
            query.prepare('select Id_trastero, M2, Precio, Alquilado, FechaBaja '
                          'from trasteros order by Id_trastero')
            var.report.setFont('Helvetica', size = 9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(460,90, 'Página siguiente...')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(60, 675, str(items[0]))
                        var.report.drawString(130, 675, str(items[1]))
                        var.report.drawString(270, 675, str(items[2]))
                        var.report.drawString(370, 675, str(items[3]))
                        var.report.drawString(460, 675, str(items[4]))
                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 660
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i,j, str(query.value(0)))
                    var.report.drawString(i+70,j,str(query.value(1)))
                    var.report.drawString(i+215,j, str(query.value(2)))
                    var.report.drawString(i+325,j, str(query.value(3)))
                    var.report.drawString(i+410,j, str(query.value(4)))
                    j = j - 25
            var.report.save()
            rootPath = '.\\informes'
            os.startfile('%s\%s' % (rootPath, name))

        except Exception as error:
            print('Error informes estado clientes' %str(error))

    def listAutos(self):
        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHÍCULOS'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            items = ['Matrícula', 'DNI', 'Marca', 'Modelo', 'Motor']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(55, 675, str(items[0]))
            var.report.drawString(130, 675, str(items[1]))
            var.report.drawString(270, 675, str(items[2]))
            var.report.drawString(370, 675, str(items[3]))
            var.report.drawString(460, 675, str(items[4]))
            var.report.line(50, 670, 525, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select matricula, dnicli, marca, modelo, motor '
                          'from coches order by matricula')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(460, 90, 'Página siguiente...')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(55, 675, str(items[0]))
                        var.report.drawString(130, 675, str(items[1]))
                        var.report.drawString(270, 675, str(items[2]))
                        var.report.drawString(370, 675, str(items[3]))
                        var.report.drawString(460, 675, str(items[4]))
                        var.report.line(50, 670, 525, 670)
                        i = 60
                        j = 660
                    var.report.setFont('Helvetica', size=9)
                    dni = '*****' + str(query.value(1)[5:8]) + '*'
                    var.report.drawString(i, j, str(query.value(0)))
                    var.report.drawString(i + 70, j, str(dni))
                    var.report.drawString(i + 215, j, str(query.value(2)))
                    var.report.drawString(i + 320, j, str(query.value(3)))
                    var.report.drawString(i + 405, j, str(query.value(4)))
                    j = j - 25
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir((rootPath)):
                if file.endswith(('Autos.pdf')):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print('Error informes estado vehiculos' %str(error))
    def listAlquileres(self):
        try:
            name = datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '_listadoAlquileres.pdf'
            file = 'informes/' + name
            var.report = canvas.Canvas(file)
            titulo = 'LISTADO ALQUILERES'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            items = ['Trastero', 'Cliente','Fecha inicio', 'Fecha fin', 'Precio total']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(65, 675, str(items[0]))
            var.report.drawString(130, 675, str(items[1]))
            var.report.drawString(270, 675, str(items[2]))
            var.report.drawString(370, 675, str(items[3]))
            var.report.drawString(460, 675, str(items[4]))
            var.report.line(50, 670, 525, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select Id_trastero, Cliente, FechaAlquiler, FechaAlquilerFinal, Precio from trasteros where Alquilado = "si" and FechaBaja IS NULL')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(460, 90, 'Página siguiente...')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(60, 675, str(items[0]))
                        var.report.drawString(130, 675, str(items[1]))
                        var.report.drawString(270, 675, str(items[2]))
                        var.report.drawString(370, 675, str(items[3]))
                        var.report.drawString(460, 675, str(items[4]))
                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 660
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawString(i, j, str(query.value(0)))

                    query2 = QtSql.QSqlQuery()
                    query2.prepare('select Nombre from Clientes where Id_cliente = :id_cliente')
                    query2.bindValue(':id_cliente',str(query.value(1)))
                    nombre = ''
                    if query2.exec():
                        while query2.next():
                            nombre = query2.value(0)
                    var.report.drawString(i + 70, j, str(nombre))
                    var.report.drawString(i + 215, j, str(query.value(2)))
                    var.report.drawString(i + 325, j, str(query.value(3)))
                    diaInicial = parser.parse(query.value(2))
                    diaFinal = parser.parse(query.value(3))
                    dias = diaFinal - diaInicial
                    precio = dias.days * query.value(4)
                    var.report.drawString(i + 410, j, str(precio) + "€")
                    j = j - 25
            var.report.save()
            rootPath = '.\\informes'
            os.startfile('%s\%s' % (rootPath, name))

        except Exception as error:
            print('Error informes estado alquileres' % str(error))
    def pieInforme(titulo):
        try:
            var.report.line(50,50,525,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size = 7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)
    def topInforme(titulo):
        try:
            logo = '.\img\logo-taller.png'
            var.report.line(50,800,525,800)
            var.report.setFont('Helvetica-Bold', size = 14)
            var.report.drawString(55,785,'Trasteros Teis')
            var.report.drawString(240,695,titulo)
            var.report.line(50, 690, 525, 690)
            var.report.drawImage(logo,440,725,width=80, height= 45)
            var.report.setFont('Helvetica', size = 9)
            var.report.drawString(55,770,'CIF: A12345678')
            var.report.drawString(55,755,'Avda. Galicia - 101')
            var.report.drawString(55,740,'Vigo - 36216 - España')
            var.report.drawString(55,725,'Teléfono: 986 132 456')
            var.report.drawString(55,710,'e-mail: mistrasteros@mail.com')
        except Exception as error:
            print('Error en cabecera informe:', error)

    def factura(self):
        try:
            var.report = canvas.Canvas('informes/factura.pdf')
            titulo = 'FACTURA'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            cliente =  []
            dni = str(var.ui.lblDnifac.text())
            nfac = str(var.ui.lblNumfac.text())
            fechafac = str(var.ui.lblFechafac.text())
            if nfac == '':
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Debe seleccionar una factura')
                msg.exec()
            else:
                cliente = conexion.Conexion.oneCli(dni)
                var.report.setFont('Helvetica-Bold', size=9)
                var.report.drawString(55,680,'DATOS CLIENTE:')
                var.report.drawString(400, 660,'Nº Factura: ')
                var.report.drawString(400, 645, 'Fecha Factura: ')
                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 660, 'DNI/CIF: ' + str(dni))
                var.report.drawRightString(525,660, str(nfac))
                var.report.drawString(480, 645, str(fechafac))
                var.report.drawString(55, 645, 'Nombre: ' + str(cliente[0]))
                var.report.drawString(55, 630, 'Dirección: ' + str(cliente[2]))
                var.report.drawString(55, 615, 'Municipio: ' + str(cliente[4]))
                var.report.drawString(150, 615, 'Provincia: ' + str(cliente[3]))
                var.report.line(50, 600, 525, 600)
                var.report.drawString(55,585,'Idventa')
                var.report.drawString(120, 585, 'Servicio')
                var.report.drawString(260, 585, 'Precio/Unidad')
                var.report.drawString(365, 585, 'Unidades')
                var.report.drawString(490, 585, 'Subtotal')
                var.report.line(50, 580, 525, 580)
                query = QtSql.QSqlQuery()
                query.prepare('select idventa, codservicio, precio, unidades from ventas where codfact = :nfac')
                query.bindValue(':nfac', int(nfac))
                var.report.setFont('Helvetica', size=9)
                total = 0.00
                if query.exec():
                    i = 55
                    j = 565
                    while query.next():
                        subtotal = 0.00
                        if j<=80:
                            var.report.drawString(460, 90, 'Página siguiente...')
                            var.report.showPage()
                            Informes.topInforme(titulo)
                            Informes.pieInforme(titulo)
                            Informes.cabeceraFactura(self)
                            var.report.drawCentredString(i+10, j, str(query.value(0)))
                            var.report.drawString(i+60, j, str(conexion.Conexion.obtenerServicio(int(query.value(1)))))
                            var.report.drawCentredString(i+240, j, str(query.value(2)).replace('.',',') + ' €')
                            var.report.drawCentredString(i+330, j, str(query.value(3)).replace('.',','))
                            subtotal = round(query.value(2)*query.value(3),2)
                            var.report.drawRightString(i+470, j, str(subtotal).replace('.',',') + ' €')
                            total = subtotal + total
                            i = 55
                            j = 565
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        Informes.cabeceraFactura(self)
                        var.report.drawCentredString(i + 10, j, str(query.value(0)))
                        var.report.drawString(i + 60, j, str(conexion.Conexion.obtenerServicio(int(query.value(1)))))
                        var.report.drawCentredString(i + 240, j, str(query.value(2)).replace('.', ',') + ' €')
                        var.report.drawCentredString(i + 330, j, str(query.value(3)).replace('.', ','))
                        subtotal = round(query.value(2) * query.value(3), 2)
                        var.report.drawRightString(i + 470, j, str(subtotal).replace('.', ',') + ' €')
                        j = j - 15
                        total = subtotal + total
                        iva = total * 0.21
                total = iva + total
                var.report.setFont('Helvetica-Bold', size=10)
                var.report.line(350, 140, 540, 140)
                var.report.drawRightString(420, 130, ' IVA: ')
                var.report.drawRightString(530,130,str(round(iva,2)).replace('.',',') + ' €')
                var.report.drawRightString(420, 110, ' TOTAL: ')
                var.report.drawRightString(530, 110, str(round(total, 2)).replace('.', ',') + ' €')
                var.report.line(350, 100, 540, 100)
               #para abrir la factura
                var.report.save()
                rootPath = '.\\informes'
                for file in os.listdir((rootPath)):
                    if file.endswith(('factura.pdf')):
                        os.startfile('%s\%s' % (rootPath, file))

        except Exception as error:
            print('Error factura :', error)

    def cabeceraFactura(self):
        try:
            dni = str(var.ui.lblDnifac.text())
            nfac = str(var.ui.lblNumfac.text())
            fechafac = str(var.ui.lblFechafac.text())
            cliente = conexion.Conexion.oneCli(dni)
            var.report.setFont('Helvetica-Bold', size=9)
            var.report.drawString(55, 680, 'DATOS CLIENTE:')
            var.report.drawString(400, 660, 'Nº Factura: ')
            var.report.drawString(400, 645, 'Fecha Factura: ')
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(55, 660, 'DNI/CIF: ' + str(dni))
            var.report.drawRightString(525, 660, str(nfac))
            var.report.drawString(480, 645, str(fechafac))
            var.report.drawString(55, 645, 'Nombre: ' + str(cliente[0]))
            var.report.drawString(55, 630, 'Dirección: ' + str(cliente[2]))
            var.report.drawString(55, 615, 'Municipio: ' + str(cliente[4]))
            var.report.drawString(150, 615, 'Provincia: ' + str(cliente[3]))
            var.report.line(50, 600, 525, 600)
            var.report.drawString(55, 585, 'Idventa')
            var.report.drawString(120, 585, 'Servicio')
            var.report.drawString(260, 585, 'Precio/Unidad')
            var.report.drawString(365, 585, 'Unidades')
            var.report.drawString(490, 585, 'Subtotal')
            var.report.line(50, 580, 525, 580)
        except Exception as error:
            print(error)
