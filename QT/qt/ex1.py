
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                   QTextEdit, QGridLayout, QApplication, QPushButton)

class Interfaz(QWidget):
    def __init__(self):
        super().__init__()

        lblTitulo = QLabel("Titulo")
        lblAutor = QLabel("Autor")
        lblResumen = QLabel("Resumen")
        editTitulo = QLineEdit()
        editAutor = QLineEdit()
        editResumen = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(lblTitulo, 1, 0)
        grid.addWidget(lblAutor, 1, 1)
        grid.addWidget(lblResumen, 2, 0)
        grid.addWidget(editTitulo, 2, 1)
        grid.addWidget(editAutor, 3, 0)
        grid.addWidget(editResumen, 3, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Ejemplo de QGridLayout")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ejemplo = Interfaz()
    sys.exit(app.exec())
