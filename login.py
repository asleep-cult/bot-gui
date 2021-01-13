from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QWidget,
    QStackedLayout,
)

from PyQt5.QtCore import (
    QRect,
    Qt
)


class LoginScreen(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        backgroundLayout = QStackedLayout(self)
        background = QWidget(self)
        background.setStyleSheet(
            'background-image: url(assets/background.jpg);'
        )
        backgroundLayout.addWidget(background)

        boxLayout = QStackedLayout()
        box = QWidget()
        box.setStyleSheet(
            'background-color: #2C2F33;'
        )
        boxLayout.addWidget(box)
        backgroundLayout.addChildLayout(boxLayout)

        innerBoxLayout = QStackedLayout()
        welcome = QLabel('HIIIIIIIIIIIIIIIII')
        welcome.setStyleSheet(
            'color: #FFFFFF;'
        )
        innerBoxLayout.addWidget(welcome)
        boxLayout.addChildLayout(innerBoxLayout)
