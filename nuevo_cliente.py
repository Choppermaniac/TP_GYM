from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_NuevoCliente(object):
    def setupUi(self, VentanaNuevoCliente):
        VentanaNuevoCliente.setObjectName("VentanaNuevoCliente")
        VentanaNuevoCliente.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=VentanaNuevoCliente)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        self.nombre_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nombre_input.setPlaceholderText("Nombre")
        self.verticalLayout.addWidget(self.nombre_input)
        
        self.apellido_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.apellido_input.setPlaceholderText("Apellido")
        self.verticalLayout.addWidget(self.apellido_input)
        
        self.submit_button = QtWidgets.QPushButton("Agregar", parent=self.centralwidget)
        self.verticalLayout.addWidget(self.submit_button)
        
        VentanaNuevoCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaNuevoCliente)
        QtCore.QMetaObject.connectSlotsByName(VentanaNuevoCliente)

    def retranslateUi(self, VentanaNuevoCliente):
        _translate = QtCore.QCoreApplication.translate
        VentanaNuevoCliente.setWindowTitle(_translate("VentanaNuevoCliente", "Agregar Datos"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaNuevoCliente = QtWidgets.QMainWindow()
    ui = Ui_NuevoCliente()
    ui.setupUi(VentanaNuevoCliente)
    VentanaNuevoCliente.show()
    sys.exit(app.exec())
