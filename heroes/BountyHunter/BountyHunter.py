from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class BountyHunter(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/BountyHunter/ui/BountyHunter.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet("background-image: url(data/background/backgroundHero.png)")
        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)
        self.label.setStyleSheet("""width: 255px;
                                          background-image: url(heroes/BountyHunter/BountyHunter.png);
                                          height: 140px;
                                          border-radius: 15px  """)
        self.label_7.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Venomancer.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_6.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Rubick.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Slardar.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Broodmother.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/AntiMage.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.Talents.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Tree.png);
                                                  height: 140px;
                                                  border-radius: 35px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill1.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/ShurikenToss.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Jinada.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/WindWalk.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/Track.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill5.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/FriendlyShadow.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/BountyHunter/Skill1Info.png);
                                                         border-radius: 15px;
                                                                                border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/BountyHunter/Skill2Info.png);
                                                                 border-radius: 15px;
                                                                                border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/BountyHunter/Skill3Info.png);
                                                                         border-radius: 15px;
                                                                                border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/BountyHunter/Skill4Info.png);
                                                                                 border-radius: 15px;
                                                                                background-repeat: no-repeat;
                                                                                border: 2px solid black""")

        self.Skill5Info.hide()
        self.Skill5Info.setStyleSheet("""background-image: url(heroes/BountyHunter/Skill5Info.png);
                                                                                         border-radius: 15px;
                                                                                        background-repeat: no-repeat;
                                                                                        border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/BountyHunter/Talants.png);
                                                                                                 border-radius: 15px;
                                                                                                background-repeat: no-repeat;
                                                                                                border: 2px solid black""")

        self.label_10.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/BuildBH.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")
        self.label_9.setStyleSheet("""width: 255px;
                                                  background-image: url(heroes/BountyHunter/SkiilInfoBH.png);
                                                  height: 140px;
                                                  border-radius: 15px;
                                                  color: white;""")

        self.label_11.setStyleSheet("""width: 255px;
                                                    background-color: rgb(50, 50, 50);
                                                    height: 140px;
                                                    border-radius: 15px;
                                                    color: white; """)
        self.label_11.setText("""Жертвы рассказывают многое об охотнике за головами по имени Гондар - и никто не знает, что из этого  правда. Кто-то шепчет 
о том, что его бросили ещё котёнком, и ему пришлось научиться охоте, лишь чтобы выжить. Другие слышали, что война лишила 
беднягу семьи, и того взял под крыло великий охотник Сорук, который научил сироту обращаться с клинками и вместе с ним 
прочёсывал тёмные рощи, выходя на большую охоту. А некоторые считают, что Гондар был обычным уличным оборванцем, 
взращённым в гильдии карманников и воров, где он и научился скрываться и запутывать следы. Его жертвы собираются вокруг 
костров в диких землях и делятся слухами, всё больше страшась головореза: 
например, поговаривают, что это он выследил короля Гоффа - безумного тирана, годами скрывавшегося от правосудия, И в 
Доказательство принёс его голову и скипетр. И что он проник в лагерь повстанцев на Хайсите, схватил там 
легендарного вора по прозвищу Белый плащ и доставил его до суда.""")

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
