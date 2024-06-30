from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QLabel
from PyQt6.QtGui import QFont
from nuevo_cliente import Ui_NuevoCliente
from borrar_cliente import Ui_BorrarCliente
import random
from datetime import datetime, timedelta
import sqlite3

fecha_actual = datetime.now()

class VerificationWindow(QtWidgets.QDialog):
    id_correct_signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Verificación de ID")
        self.setGeometry(300, 300, 300, 100)
        
        self.layout = QtWidgets.QVBoxLayout()

        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setPlaceholderText("Ingrese la ID del cliente")
        self.layout.addWidget(self.id_input)

        self.verify_button = QtWidgets.QPushButton("Verificar ID", self)
        self.verify_button.clicked.connect(self.verify_id)
        self.layout.addWidget(self.verify_button)

        self.result_label = QtWidgets.QLabel("", self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def clear_result_label(self):
        self.result_label.setText("")

    def verify_id(self):

        self.clear_result_label()

        conn = sqlite3.connect('DataBaseGym.db')
        cursor = conn.cursor()

        id_cliente = self.id_input.text()

        cursor.execute("SELECT ID FROM Clientes WHERE ID = ?", (id_cliente,))
        result = cursor.fetchone()

        if result is None:
            self.result_label.setText("ID incorrecta")
        else:
            self.result_label.setText("ID correcta")
            self.id_correct_signal.emit(id_cliente)

        self.id_input.clear()

        conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GYM FORCE")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_bienvenida = QLabel("CLIENTES ACTIVOS", self.centralwidget)
        self.label_bienvenida.setFont(QtGui.QFont('Arial', 24))
        self.label_bienvenida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bienvenida.setGeometry(200, 50, 400, 50)

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 160, 645, 301))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)


        self.boton_agregar_cliente = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_agregar_cliente.setGeometry(QtCore.QRect(250, 535, 100, 30))
        self.boton_agregar_cliente.setObjectName("agregar_cliente")
        self.boton_agregar_cliente.setText("Agregar Cliente")

        self.boton_borrar_cliente = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_borrar_cliente.setGeometry(QtCore.QRect(450, 535, 100, 30))
        self.boton_borrar_cliente.setObjectName("borrar_cliente")
        self.boton_borrar_cliente.setText("Borrar Cliente")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.boton_agregar_cliente.clicked.connect(self.abrir_agregar_cliente)
        self.boton_borrar_cliente.clicked.connect(self.abrir_borrar_cliente)

        self.load_data_from_database()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GYM FORCE"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Inscripcion"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Vencimiento"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ESTADO"))

    def abrir_agregar_cliente(self):
        self.secondary_window = QtWidgets.QMainWindow()
        self.ui = Ui_NuevoCliente()
        self.ui.setupUi(self.secondary_window)
        self.ui.submit_button.clicked.connect(self.add_data_to_table)
        self.secondary_window.show()

    def abrir_borrar_cliente(self):
        self.delete_window = QtWidgets.QMainWindow()
        self.ui = Ui_BorrarCliente()
        self.ui.setupUi(self.delete_window)
        self.ui.delete_button.clicked.connect(self.delete_data_from_table)
        self.delete_window.show()

    def add_data_to_table(self):

        conn = sqlite3.connect('DataBaseGym.db')
        cursor = conn.cursor()



        id_cliente = random.randint(1000, 9999)
        while True:
            cursor.execute("SELECT ID FROM Clientes WHERE ID = ?", (id_cliente,))
            result = cursor.fetchone()
            if result is None:
                break
        nombre = self.ui.nombre_input.text()
        apellido = self.ui.apellido_input.text()
        inscripcion = fecha_actual.strftime("%d/%m/%y")
        fecha_vencimiento = fecha_actual + timedelta(days=30)
        vencimiento = fecha_vencimiento.strftime("%d/%m/%y")

        cursor.execute('INSERT INTO Clientes (ID, Nombre, Apellido, Inscripcion, vencimiento) VALUES (?, ?, ?, ?, ?)', (id_cliente, nombre, apellido, inscripcion, vencimiento))

        conn.commit()
        conn.close()

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(id_cliente)))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(nombre))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(apellido))
        self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(inscripcion))
        self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(vencimiento))

        estado_item = QtWidgets.QTableWidgetItem()
        if fecha_actual >= datetime.strptime(inscripcion, "%d/%m/%y") and fecha_actual <= datetime.strptime(vencimiento, "%d/%m/%y"):
            estado_item.setBackground(QtGui.QColor(0, 255, 0))  # Verde
            estado_item.setText("ACTIVO")
        else:
            estado_item.setBackground(QtGui.QColor(255, 0, 0))  # Rojo
            estado_item.setText("INACTIVO")

        self.tableWidget.setItem(row_position, 5, estado_item)

        self.secondary_window.close()

    def delete_data_from_table(self):
        
        conn = sqlite3.connect('DataBaseGym.db')
        cursor = conn.cursor()

        id_cliente = self.ui.id_input.text()

        cursor.execute('DELETE FROM CLientes WHERE ID = ?', (id_cliente,))

        conn.commit()
        conn.close()

        # Eliminar fila de la tabla
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0).text() == str(id_cliente):
                self.tableWidget.removeRow(row)
                break

        self.delete_window.close()

    def load_data_from_database(self):
        conn = sqlite3.connect('DataBaseGym.db')
        cursor = conn.cursor()

        cursor.execute('SELECT ID, Nombre, Apellido, Inscripcion, Vencimiento FROM Clientes')

        rows = cursor.fetchall()

        conn.close()

        self.tableWidget.setRowCount(len(rows))

        for row_index, row_data in enumerate(rows):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)


                if col_index == 4:
                    vencimiento = datetime.strptime(data, "%d/%m/%y")
                    inscripcion = datetime.strptime(row_data[3], "%d/%m/%y")
                    fecha_actual = datetime.now()

                    estado_item = QtWidgets.QTableWidgetItem()
                    if fecha_actual >= inscripcion and fecha_actual <= vencimiento:
                        estado_item.setBackground(QtGui.QColor(0, 255, 0))  # Verde
                        estado_item.setText('ACTIVO')
                    else:
                        estado_item.setBackground(QtGui.QColor(255, 0, 0))  # Rojo
                        estado_item.setText('INACTIVO')

                    self.tableWidget.setItem(row_index, 5, estado_item)

    def show_success_message(self, id_cliente):

        conn = sqlite3.connect('DataBaseGym.db')
        cursor = conn.cursor()

        consulta_nombre = 'SELECT Nombre FROM Clientes WHERE ID = ?'

        cursor.execute(consulta_nombre, (id_cliente, ))
        resultado = cursor.fetchone()
        conn.close()


        nombre_cliente = resultado[0]
        success_message = f"El ID {id_cliente} ({nombre_cliente}) ha ingresado al gimnasio"
        QtWidgets.QMessageBox.information(self.centralwidget, "Ingreso Exitoso", success_message, QtWidgets.QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # verification_window = VerificationWindow()
    # verification_window.show()

    verification_window = VerificationWindow()

    def on_id_correct(id_cliente):
        ui.show_success_message(id_cliente)

    verification_window.id_correct_signal.connect(on_id_correct)

    verification_window.exec()

    sys.exit(app.exec())
