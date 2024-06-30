from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QMessageBox)

from PyQt6.QtGui import QFont
import random
import sqlite3

conn = sqlite3.connect("DataBaseGym.db")
cursor = conn.cursor()

class RegistrarUsuarioView(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()
        
    def generar_formulario(self):
        self.setGeometry(100, 100, 390, 250)
        self.setWindowTitle('Registration Window')

        id_gym_label = QLabel(self)
        id_gym_label.setText('ID Gimnasio: ')
        id_gym_label.setFont(QFont('Arial', 10))
        id_gym_label.move(20,44)

        self.id_gym_input = QLineEdit(self)
        self.id_gym_input.resize(250, 24)
        self.id_gym_input.move(100, 40)

        nombre_instructor_label = QLabel(self)
        nombre_instructor_label.setText('Nombre:')
        nombre_instructor_label.setFont(QFont('Arial', 10))
        nombre_instructor_label.move(20,74)

        self.nombre_instructor_input = QLineEdit(self)
        self.nombre_instructor_input.resize(250, 24)
        self.nombre_instructor_input.move(100, 70)

        apellido_label = QLabel(self)
        apellido_label.setText('Apellido:')
        apellido_label.setFont(QFont('Arial', 10))
        apellido_label.move(20,104)

        self.apellido_input = QLineEdit(self)
        self.apellido_input.resize(250, 24)
        self.apellido_input.move(100, 100)

        create_button = QPushButton(self)
        create_button.setText('Crear')
        create_button.resize(150, 32)
        create_button.move(40, 170)
        create_button.clicked.connect(self.crear_usuario)

        cancel_button = QPushButton(self)
        cancel_button.setText('Cancelar')
        cancel_button.resize(150, 32)
        cancel_button.move(190, 170)
        cancel_button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        self.close()

    def crear_usuario(self):
        
        id_gym = self.id_gym_input.text()
        nombre = self.nombre_instructor_input.text()
        apellido = self.apellido_input.text()

        if nombre == '' or apellido == '' or id_gym == '':
            QMessageBox.warning(self, 'Error',
            'Por favor ingrese datos validos',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close,)
        elif id_gym != "2486":
            QMessageBox.warning(self, 'Error',
            'El numero ID de gimnasio no es valido',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close,)
        else: 
            numero_id = random.randint(1000,9999)
            consulta = (f"INSERT INTO Instructores (id, nombre, apellido) VALUES (?, ?, ?)")
            parametros = (numero_id, nombre, apellido)
            cursor.execute(consulta, parametros)
            conn.commit()
            QMessageBox.information(self, 'Creacion exitosa',
            'Usuario creado correctamente',
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Ok)
            self.close()
