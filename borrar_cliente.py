from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_BorrarCliente(object):
    def setupUi(self, VentanaBorrarCliente):
        VentanaBorrarCliente.setObjectName("VentanaBorrarCliente")
        VentanaBorrarCliente.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=VentanaBorrarCliente)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
    
        
        self.id_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_input.setPlaceholderText("Ingrese la ID del cliente a eliminar")
        self.id_input.setFixedWidth(400) 
        self.id_input.setFixedHeight(40)
        self.verticalLayout.addWidget(self.id_input)
        
        self.delete_button = QtWidgets.QPushButton("Eliminar Cliente", parent=self.centralwidget)
        self.delete_button.setFixedHeight(40)
        self.verticalLayout.addWidget(self.delete_button)
        
        VentanaBorrarCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaBorrarCliente)
        QtCore.QMetaObject.connectSlotsByName(VentanaBorrarCliente)

    def retranslateUi(self, VentanaBorrarCliente):
        _translate = QtCore.QCoreApplication.translate
        VentanaBorrarCliente.setWindowTitle(_translate("VentanaBorrarCliente", "Borrar Cliente"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaBorrarCliente = QtWidgets.QMainWindow()
    ui = Ui_BorrarCliente()
    ui.setupUi(VentanaBorrarCliente)
    VentanaBorrarCliente.show()
    sys.exit(app.exec())