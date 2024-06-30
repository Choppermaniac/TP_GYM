from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt6 import QtWidgets
import sys

from PyQt6.QtGui import QFont

from registro import RegistrarUsuarioView
from main_window import Ui_MainWindow, VerificationWindow

import sqlite3

conn = sqlite3.connect("DataBaseGym.db")
cursor = conn.cursor()

class VentanaLogin(QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()

    def InicializarUI(self):
        self.setGeometry(100,100, 400,200)
        self.setWindowTitle('GYM FORCE')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText('ID de instructor:')
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(120, 50)

        login_button = QPushButton(self)
        login_button.setText('LOGIN')
        login_button.resize(320, 34)
        login_button.move(40, 100)
        login_button.clicked.connect(self.login)

        login_button.setStyleSheet("""

            QPushButton {
                font-family: Arial;
                font-weight: bold;
                font-size: 20px;
                letter-spacing: 5px;
                color: white;
                background-color: green;
                border-radius: 10px;
            }

        """)

        register_button = QPushButton(self)
        register_button.setText('REGISTRARSE')
        register_button.resize(320, 34)
        register_button.move(40, 140)
        register_button.clicked.connect(self.registrar_usuario)

        register_button.setStyleSheet("""

            QPushButton {
                font-family: Arial;
                font-weight: bold;
                font-size: 20px;
                letter-spacing: 3px;
                color: white;
                background-color: orange;
                border-radius: 10px;
            }
        """)

    def mostrar_contrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def login(self):
        
        id_ingresado = self.user_input.text()

        consulta = 'SELECT * FROM Instructores WHERE ID = ?'
        cursor.execute(consulta, (id_ingresado,))
        resultado = cursor.fetchone()

        if resultado is not None:
            QMessageBox.information(self, 'Inicio sesión',
                                    'Inicio de sesión exitoso',
                                    QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
            self.is_logged = True
            self.close()
            self.open_main_window()
        else:
            QMessageBox.warning(self, 'Error',
                                'ID de usuario no encontrado',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)


    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()

    def open_main_window(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()

        self.verification_window = VerificationWindow()
        self.verification_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    sys.exit(app.exec())