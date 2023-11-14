import sys
import sqlite3

from heroes.DarkWillow import DarkWillow
from heroes.AncientApparition import AncientApparition
from heroes.VengefulSpirit import VengefulSpirit
from heroes.SpiritBreaker import SpiritBreaker
from heroes.Axe import Axe
from heroes.Mars import Mars
from heroes.LegionCommander import LegionCommander
from heroes.SkywrathMage import SkywrathMage
from heroes.Techies import Techies
from heroes.BountyHunter import BountyHunter
from heroes.Slardar import Slardar
from heroes.Bristleback import Bristleback
from welcome import Welcome
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pixmap = QPixmap('data/background/background.png')
        self.img1 = QLabel(self)
        self.img1.resize(QSize(1550, 700))
        self.img1.setPixmap(self.pixmap.scaled(QSize(1550, 700), Qt.IgnoreAspectRatio))
        uic.loadUi('ui/main.ui', self)

        self.BackGroundBtn.clicked.connect(self.changeBackGround)
        self.connection = sqlite3.connect("database/heroes.sqlite")
        self.cursor = self.connection.cursor()
        self.heroes = {
            "DarkWillow": 'DarkWillow.DarkWillow()',
            "AncientApparition": 'AncientApparition.AncientApparition()',
            "VengefulSpirit": 'VengefulSpirit.VengefulSpirit()',
            "SpiritBreaker": 'SpiritBreaker.SpiritBreaker()',
            "Axe": 'Axe.Axe()',
            "Mars": 'Mars.Mars()',
            "LegionCommander": 'LegionCommander.LegionCommander()',
            "SkywrathMage": 'SkywrathMage.SkywrathMage()',
            "Techies": 'Techies.Techies()',
            "BountyHunter": 'BountyHunter.BountyHunter()',
            "Bristleback": 'Bristleback.Bristleback()',
            "Slardar": 'Slardar.Slardar()'
        }

        self.heroesButtons = {
            "Dark Willow": self.DarkWillow,
            "Ancient Apparition": self.AncientApparition,
            "Vengeful Spirit": self.VengefulSpirit,
            "Spirit Breaker": self.SpiritBreaker,
            "Axe": self.Axe,
            "Mars": self.Mars,
            "LegionCommander": self.LegionCommander,
            "SkywrathMage": self.SkywrathMage,
            "Techies": self.Techies,
            "Slardar": self.Slardar,
            "Bristleback": self.Bristleback,
            "BountyHunter": self.BountyHunter
        }

        self.setWindowTitle("DotaHelper")
        self.img = QPixmap("data/tj/TeamJidkie.jpg")
        self.img.scaled(QSize(451, 381))
        self.label.setPixmap(self.img)
        self.window = None
        self.window1 = None
        self.setFixedSize(1550, 700)
        self.initUI()

    def initUI(self):
        self.BackGroundBtn.setStyleSheet("""background-image: url(data/tj/btn.png);
                                            border-radius: 10px;
                                            color:white;""")

        self.SearchButton.setStyleSheet("""
                QPushButton { color: white;
                              background: rgb(77, 77, 77);
                              border-radius: 10px;
                              border: 1px solid rgba(255, 255, 255, 50);
                              }
                QPushButton:hover { border: 2px solid rgba(255, 255, 255, 125);
                                    }
                """)
        self.Search.setStyleSheet("""
                QLineEdit { background: rgb(77, 77, 77);
                            border-radius: 10px;
                            color: white;
                            border: 1px solid rgba(255, 255, 255, 50);
                           }
                QLineEdit:hover { border: 2px solid rgba(255, 255, 255, 100); } 
                QLineEdit:focus { border: 2px solid rgba(255, 255, 255, 255); } 
            """)
        self.DarkWillow.setStyleSheet("""width: 256px;
                                         height: 143px;
                                         background-image: url(heroes/DarkWillow/DarkWillow.png);
                                         background-size: contain;
                                         border-radius: 8px;
                                         color: rgba(0, 0, 0, 0);
                                         """)

        self.AncientApparition.setStyleSheet("""width: 256px;
                                                height: 146px;
                                                background-image: url(heroes/AncientApparition/AncientApparition.png);
                                                background-size: contain;
                                                border-radius: 8px;
                                                color: rgba(0, 0, 0, 0);
                                                """)

        self.VengefulSpirit.setStyleSheet("""width: 256px;
                                             height: 146px;
                                             background-image: url(heroes/VengefulSpirit/VengefulSpirit.png);
                                             background-size: contain;
                                             border-radius: 8px;
                                             color: rgba(0, 0, 0, 0);
                                             """)

        self.SpiritBreaker.setStyleSheet("""width: 256px;
                                            height: 146px;
                                            background-image: url(heroes/SpiritBreaker/SpiritBreaker.png);
                                            background-size: contain;
                                            border-radius: 8px;
                                            color: rgba(0, 0, 0, 0);
                                            """)

        self.Axe.setStyleSheet("""width: 256px;
                                  height: 143px;
                                  background-image: url(heroes/Axe/Axe.png);
                                  background-size: contain;
                                  border-radius: 8px;
                                  color: rgba(0, 0, 0, 0);
                                  """)

        self.Mars.setStyleSheet("""QPushButton { width: 256px;
                                                 height: 143px;
                                                 background-image: url(heroes/Mars/Mars.png);
                                                 background-size: contain;
                                                 border-radius: 8px;
                                                 color: rgba(0, 0, 0, 0);
                                                 }""")

        self.LegionCommander.setStyleSheet("""width: 256px;
                                              height: 143px;
                                              background-image: url(heroes/LegionCommander/LegionCommander.png);
                                              background-size: contain;
                                              border-radius: 8px;
                                              color: rgba(0, 0, 0, 0);
                                              """)

        self.SkywrathMage.setStyleSheet("""width: 256px;
                                           height: 143px;
                                           background-image: url(heroes/SkywrathMage/SkywrathMage.png);
                                           background-size: contain;
                                           border-radius: 8px;
                                           color: rgba(0, 0, 0, 0);
                                           """)

        self.Techies.setStyleSheet("""width: 256px;
                                      height: 143px;
                                      background-image: url(heroes/Techies/Techies.png);
                                      background-size: contain;
                                      border-radius: 8px;
                                      color: rgba(0, 0, 0, 0);
                                      """)
        self.BountyHunter.setStyleSheet("""width: 256px;
                                           height: 143px;
                                           background-image: url(heroes/BountyHunter/BountyHunter.png);
                                           background-size: contain;
                                           border-radius: 8px;
                                           color: rgba(0, 0, 0, 0);
                                           """)

        self.Bristleback.setStyleSheet("""width: 256px;
                                          height: 143px;
                                          background-image: url(heroes/Bristleback/Bristleback.png);
                                          background-size: contain;
                                          border-radius: 8px;
                                          color: rgba(0, 0, 0, 0);
                                          """)

        self.Slardar.setStyleSheet("""width: 256px;
                                      height: 146px;
                                      background-image: url(heroes/Slardar/Slardar.png);
                                      background-size: contain;
                                      border-radius: 8px;
                                      color: rgba(0, 0, 0, 0);
                                      """)

        self.buttonGroup.buttonClicked.connect(self.run)
        self.SearchButton.clicked.connect(self.search)
        self.window1 = Welcome()
        self.window1.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.window1.setWindowTitle('Приветствие')
        self.window1.show()

    def run(self, arg):
        name = arg.text()
        if name in list(self.heroes.keys()):
            if self.window is None:
                self.window = eval(self.heroes.get(name))
                self.window.setWindowTitle(name)
                self.window.show()
            else:
                self.window.close()
                self.window = eval(self.heroes.get(name))
                self.window.setWindowTitle(name)
                self.window.show()

    def search(self):
        if self.Search.text() == '':
            for hero, button in self.heroesButtons.items():
                button.show()
            return

        result = self.cursor.execute("""SELECT t1.name, t1.altname, t1.button, t2.name AS 'attribute', t3.type AS
                                        'typeAttack'
                                        FROM heroes t1
                                        JOIN attributes t2 ON t1.attribute = t2.id
                                        JOIN typeAttack t3 ON t1.typeAttack = t3.id;
                                        """).fetchall()

        for x in result:
            find = x[0].replace(' ', '').lower() + ' ' + x[1].lower() + ' ' + x[3].lower() + ' ' + x[4].lower()
            find.split()
            if self.Search.text().lower() in find:
                eval(x[2]).show()
            elif self.Search.text().lower() not in find:
                eval(x[2]).hide()

    def changeBackGround(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Картинка (*.jpeg);;Все файлы (*)')[0]
        if fname != '':
            self.pixmap = QPixmap(fname)
            self.img1.setPixmap(self.pixmap.scaled(QSize(1550, 700), Qt.IgnoreAspectRatio))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.search()

    def closeEvent(self, **kwargs):
        self.window.close()
        self.window1.close()
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
