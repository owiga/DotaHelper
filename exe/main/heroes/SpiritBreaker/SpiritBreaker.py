from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class SpiritBreaker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/SpiritBreaker/ui/hero.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet("background-image: url(data/background/backgroundHero.png)")
        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)
        self.label.setStyleSheet("""width: 255px;
                                          background-image: url(heroes/SpiritBreaker/SpiritBreaker.png);
                                          height: 140px;
                                          border-radius: 15px  """)
        self.label_7.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/Clockwerk.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_6.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/Tiny.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/reMars.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/EmberSpirit.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/Morphling.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.Talant.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/Tree.png);
                                                  height: 140px;
                                                  border-radius: 35px;
                                                  color: rgba(0, 0, 0, 0);
                                                  border: 1px solid rgba(255, 255, 255, 100)""")
        self.Skill1.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/ChargeOfDarkness.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: rgba(0, 0, 0, 0);
                                                  border: 1px solid rgba(255, 255, 255, 100)""")
        self.Skill2.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/Bulldoze.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: rgba(0, 0, 0, 0);
                                                  border: 1px solid rgba(255, 255, 255, 100)""")
        self.Skill3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/GreaterBash.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: rgba(0, 0, 0, 0);
                                                  border: 1px solid rgba(255, 255, 255, 100)""")
        self.Skill4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/NetherStrike.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: rgba(0, 0, 0, 0);
                                                  border: 1px solid rgba(255, 255, 255, 100)""")
        self.Skill5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/PlanarPocket.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: rgba(0, 0, 0, 0);
                                                  border: 1px solid rgba(255, 255, 255, 100)""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/SpiritBreaker/Skill1Info.png);
                                                 border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/SpiritBreaker/Skill2Info.png);
                                                         border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/SpiritBreaker/Skill3Info.png);
                                                                 border-radius: 15px;
                                                                        border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/SpiritBreaker/Skill4Info.png);
                                                                         border-radius: 15px;
                                                                        background-repeat: no-repeat;
                                                                        border: 2px solid black""")

        self.Skill5Info.hide()
        self.Skill5Info.setStyleSheet("""background-image: url(heroes/SpiritBreaker/Skill5Info.png);
                                                                                 border-radius: 15px;
                                                                                background-repeat: no-repeat;
                                                                                border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/SpiritBreaker/Talant.png);
                                                                                         border-radius: 15px;
                                                                                        background-repeat: no-repeat;
                                                                                        border: 2px solid black""")

        self.label_10.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/BuildBara.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_9.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/SpiritBreaker/SkillsBuild.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_11.setStyleSheet("""width: 255px;
                                                    background-color: rgb(50, 50, 50);
                                                    height: 140px;
                                                    border-radius: 15px;
                                                    color: white; """)
        self.label_11.setText("""    Баратрум - гордое и могущественное существо, яростный первичный разум. В мир материи он пришёл, 
    чтоб участвовать в событиях, отзвуки которых донесутся до его родной первичной вселенной. Сам 
    собрал своё тело Баратрум, и послужит оно ему как в нашем мире, так и за его пределами. Его
    бренная оболочка черпает силы из нашей вселенной, объединяет она формы быка и обезьяны: 
    рога, копыта и лапы воплощают его силу, скорость и ловкость. Кольцо в носу напоминает Баратруму, 
    что служит он тайному господину и что мир, где трудится он, - лишь тень настоящего бытия.""")

        self.buttonGroup.buttonClicked.connect(self.run)
        self.LabelHero = {
            "Skill1": self.Skill1Info,
            "Skill2": self.Skill2Info,
            "Skill3": self.Skill3Info,
            "Skill4": self.Skill4Info,
            "Skill5": self.Skill5Info,
            "Talents": self.TalentsInfo
        }

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()