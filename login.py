from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QWidget,
    QStackedLayout
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

        boxLayout = QGridLayout()
        box = QWidget()
        box.setStyleSheet(
            'background-image: none;'
            'background-color: #2C2F33;'
        )
        boxLayout.addWidget(box)
        backgroundLayout.addChildLayout(boxLayout)
