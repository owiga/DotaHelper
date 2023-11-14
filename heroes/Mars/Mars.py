from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class Mars(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/Mars/ui/Mars.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet(""" background-image: url(data/background/backgroundHero.png);
                                      background-repeat: no-repeat;""")
        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)
        self.label.setStyleSheet("""width: 255px;
                                          background-image: url(heroes/Mars/Mars.png);
                                          height: 140px;
                                          border-radius: 15px  """)
        self.label_7.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/Pugna.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_6.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/EarthSpirit.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/LoneDruid.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/QueenOfPain.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/PhantomLancer.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.Talents.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/Tree.png);
                                                  height: 140px;
                                                  border-radius: 35px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill1.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/SpearOfMars.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/GodRebuke.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/Bulwark.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/ArenaOfBlood.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100)""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/Mars/Skill1Info.png);
                                                 border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/Mars/Skill2Info.png);
                                                         border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/Mars/Skill3Info.png);
                                                                 border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/Mars/Skill4Info.png);
                                                                         border-radius: 15px;
                                                                        background-repeat: no-repeat;
                                                                        border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/Mars/Talants.png);
                                                                                         border-radius: 15px;
                                                                                        background-repeat: no-repeat;
                                                                                        border: 2px solid black""")

        self.label_10.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/BuildMars.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_9.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Mars/SkiilsInfoMars.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.buttonGroup.buttonClicked.connect(self.run)
        self.LabelHero = {
            "Skill1": self.Skill1Info,
            "Skill2": self.Skill2Info,
            "Skill3": self.Skill3Info,
            "Skill4": self.Skill4Info,
            "Talents": self.TalentsInfo
        }

        self.label_11.setStyleSheet("""width: 255px;
                                                    background-color: rgb(50, 50, 50);
                                                    height: 140px;
                                                    border-radius: 15px;
                                                    color: white; """)

        self.label_11.setText("""    Марс, первый сын небес, всю свою долгую жизнь провёл в нескончаемой войне и видел, 
    как под стягами его древнего имени ведутся бесчисленные боевые кампании. Войны ради завоеваний 
    и ради мести. Справедливые и беспричинные... Всегда жестокие. Подобно своему отцу, Марс 
    подчинялся низменным инстинктам - с куда более варварскими намерениями, чем у Зевса, - и 
    приносил Другим неописуемые страдания. """)

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()
