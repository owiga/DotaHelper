from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class LegionCommander(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/LegionCommander/ui/LegionCommander.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet(""" background-image: url(data/background/backgroundHero.png);
                                      background-repeat: no-repeat;""")
        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)
        self.label.setStyleSheet("""width: 255px;
                                          background-image: url(heroes/LegionCommander/LegionCommander.png);
                                          height: 140px;
                                          border-radius: 15px  """)
        self.label_7.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/Io.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_6.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/Abaddon.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/reMars.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/OutworldDestroyer.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/Medusa.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.Talents.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/Tree.png);
                                                  height: 140px;
                                                  border-radius: 35px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill1.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/OverwhelmingOdds.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/PressTheAttack.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/MomentOfCourage.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/Duel.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                                  color: rgba(0, 0, 0, 0);""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/LegionCommander/Skill1Info.png);
                                                 border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/LegionCommander/Skill2Info.png);
                                                         border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/LegionCommander/Skill3Info.png);
                                                                 border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/LegionCommander/Skill4Info.png);
                                                                         border-radius: 15px;
                                                                        background-repeat: no-repeat;
                                                                        border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/LegionCommander/Talants.png);
                                                                                         border-radius: 15px;
                                                                                        background-repeat: no-repeat;
                                                                                        border: 2px solid black""")

        self.buttonGroup.buttonClicked.connect(self.run)
        self.LabelHero = {
            "Skill1": self.Skill1Info,
            "Skill2": self.Skill2Info,
            "Skill3": self.Skill3Info,
            "Skill4": self.Skill4Info,
            "Talents": self.TalentsInfo
        }

        self.label_10.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/BuildLegionCommander.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_9.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/LegionCommander/SkiilInfoLC.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_11.setStyleSheet("""width: 255px;
                                                    background-color: rgb(50, 50, 50);
                                                    height: 140px;
                                                    border-radius: 15px;
                                                    color: white; """)
        self.label_11.setText("""Они пришли без предупреждения. Внутри городских стен Стоунхолла вдруг раздался ужасный грохот, 
и из неизведанной тьмы явились бесчисленные твари, несущие пламя и разруху, убивающие и 
захватывающие матерей и сыновей во имя тёмных целей. Из бывшей когда-то могучей армии 
Стоунхолла лишь Бронзовый легион под руководством главнокомандующей Тресдин находился рядом и 
смог ответить на зов помощи. Въехав в город, они начали пробиваться через окровавленные переулки и 
пылающие рынки, прорубая свой путь к источнику внезапного вторжения - пространственному расколу 
на главной площади, на краю которого бушевал лидер Орды бездны.""")

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()