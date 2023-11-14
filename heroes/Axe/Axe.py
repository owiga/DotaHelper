from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class Axe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/Axe/ui/axe.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet(""" background-image: url(data/background/backgroundHero.png);
                                      background-repeat: no-repeat;""")
        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)
        self.label.setStyleSheet("""width: 255px;
                                          background-image: url(heroes/Axe/Axe.png);
                                          height: 140px;
                                          border-radius: 15px  """)
        self.label_7.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/Io.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_6.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/Abaddon.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/Timbersaw.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/Necrophos.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/Luna.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.Talents.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/Tree.png);
                                                  height: 140px;
                                                  border-radius: 35px;
                                                  border: 1px solid rgba(255, 255, 255, 100)""")
        self.Skill1.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/BerserkerCall.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/BattleHunger.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/CoumterHelix.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/CullingBlade.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);
                                                  color: rgba(0, 0, 0, 0);""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/Axe/Skill1Info.png);
                                                         border-radius: 15px;
                                                                                border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/Axe/Skill2Info.png);
                                                                 border-radius: 15px;
                                                                                border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/Axe/Skill3Info.png);
                                                                         border-radius: 15px;
                                                                                border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/Axe/Skill4Info.png);
                                                                                 border-radius: 15px;
                                                                                background-repeat: no-repeat;
                                                                                border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/Axe/Talants.png);
                                                                                                 border-radius: 15px;
                                                                                                background-repeat: no-repeat;
                                                                                                border: 2px solid black""")

        self.label_10.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/BuildAxe.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_9.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/Axe/SkiilInfoAxe.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_11.setStyleSheet("""width: 255px;
                                                    background-color: rgb(50, 50, 50);
                                                    height: 140px;
                                                    border-radius: 15px;
                                                    color: white; """)

        self.buttonGroup.buttonClicked.connect(self.run)
        self.LabelHero = {
            "Skill1": self.Skill1Info,
            "Skill2": self.Skill2Info,
            "Skill3": self.Skill3Info,
            "Skill4": self.Skill4Info,
            "Talents": self.TalentsInfo
        }

        self.label_11.setText("""Ещё будучи рядовым бугаем в армии Красного тумана, Могул-хан положил глаз на генеральский титул. Битву за битвой он 
самыми кровавыми способами доказывал собственное превосходство. Облегчало подъём в чинах и то, что без тени сомнения 
он мог обезглавить старшего по званию. В семилетней кампании на Тысячеболотье Могул-хан отличился в кровопролитных 
бойнях, и звезда его славы засияла еще ярче, но число соратников неизменно сокращалось. В ночь безоговорочной победы
он провозгласил себя генералом Красного тумана, присвоив себе заодно и титул верховного военачальника. Однако теперь в 
его отряде не значилось ни одного воина. Множество бойцов было повержено врагом, но и от его топора погибло достаточно. 
Стоит ли говорить, что большинство солдат теперь ни за что не переманить под его знамена? Но Могул-хана это совсем не 
смущает, ведь он знает: один в поле воин. """)

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()
