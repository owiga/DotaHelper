from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap


class image(QLabel):
    def __init__(self, im, im2):
        super().__init__()
        self.pix1 = QPixmap(im)
        self.pix2 = QPixmap(im2)
        self.h1 = self.pix1.height()
        self.w1 = self.pix1.width()

        self.h2 = self.pix2.height()
        self.w2 = self.pix2.width()

    def enterEvent(self, event):
        self.resize(self.w1, self.h1)

    def leaveEvent(self, event):
        self.resize(self.w2, self.h2)