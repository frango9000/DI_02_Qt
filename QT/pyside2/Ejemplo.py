import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt


class Aplication (QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.saludo = ["hola", "ola", "hello", "alo", "salut", "ciao"]
        boton = QPushButton ("Pulsame")
        self.etiqueta = QLabel ("Hola")
        self.etiqueta.setAlignment(Qt.AlignCenter)
        cajaV = QVBoxLayout()
        cajaV.addWidget(self.etiqueta)
        cajaV.addWidget(boton)
        self.setLayout(cajaV)
        boton.clicked.connect(self.on_button_clicked)


    def on_button_clicked (self):
        self.etiqueta.setText(random.choice(self.saludo))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Aplication()
    application.resize(400,300)
    application.show()
    sys.exit(app.exec_())