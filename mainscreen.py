import sys
from login import LoginScreen
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self, client):
        self.client = client
        self.app = QApplication(sys.argv)
        super().__init__()

        self.setStyleSheet(
            'background-color: #2C2F33;'
        )

        self.setWindowTitle('Discord')
        self.setCentralWidget(LoginScreen())

    def start(self):
        self.showMaximized()
        self.app.exec_()
