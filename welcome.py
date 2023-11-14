from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(""" background-image: url(data/background/backgroundHero.png);
                                              background-repeat: no-repeat;""")
        uic.loadUi('ui/welcome.ui', self)
        with open('about.txt', mode='r', encoding='utf8') as welcometext:
            text = [x for x in welcometext]
            self.label.setText(' '.join(text))





