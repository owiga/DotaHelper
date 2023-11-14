from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Techies(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/Techies/ui/Techies.ui', self)
        self.setStyleSheet("background-image: url(data/background/backgroundHero.png)")
        self.Picture.setStyleSheet("""background-image: url(heroes/Techies/Techies.png);
                                      background-repeat: no-repeat;
                                      width: 255px;
                                      height: 140px;
                                      border-radius: 15px;""")
        self.setFixedSize(1000, 700)
        self.Talant.setStyleSheet("""background-image: url(heroes/Talents.png);
                                    border-radius: 35px;
                                    color: rgba(0, 0, 0, 0);""")
        self.Hero1.setStyleSheet("""background-image: url(heroes/AntiMage/reAntiMage.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero2.setStyleSheet("""background-image: url(heroes/TemplarAssassin/reTemplarAssassin.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero3.setStyleSheet("""background-image: url(heroes/NightStalker/reNightStalker.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero4.setStyleSheet("""background-image: url(heroes/Abaddon/reAbaddon.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero5.setStyleSheet("""background-image: url(heroes/Oracle/reOracle.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Skill1.setStyleSheet("""background-image: url(heroes/Techies/StickBomb.png);
                                  border-radius: 15px;
                                  border: 1px solid rgba(255, 255, 255, 100);    
                                  color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""background-image: url(heroes/Techies/ReactiveTazer.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""background-image: url(heroes/Techies/BlastOff.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""background-image: url(heroes/Techies/MinefieldSign.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill5.setStyleSheet("""background-image: url(heroes/Techies/ProximityMines.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/Techies/Skill1Info.png);
                                         border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/Techies/Skill2Info.png);
                                                 border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/Techies/Skill3Info.png);
                                                         border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/Techies/Skill4Info.png);
                                                                 border-radius: 15px;
                                                                background-repeat: no-repeat;
                                                                border: 2px solid black""")

        self.Skill5Info.hide()
        self.Skill5Info.setStyleSheet("""background-image: url(heroes/Techies/Skill5Info.png);
                                                                         border-radius: 15px;
                                                                        background-repeat: no-repeat;
                                                                        border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/Techies/Talants.png);
                                                                                 border-radius: 15px;
                                                                                background-repeat: no-repeat;
                                                                                border: 2px solid black""")

        self.buttonGroup.buttonClicked.connect(self.run)
        self.LabelHero = {
            "Skill1": self.Skill1Info,
            "Skill2": self.Skill2Info,
            "Skill3": self.Skill3Info,
            "Skill4": self.Skill4Info,
            "Skill5": self.Skill5Info,
            "Talents": self.TalentsInfo
        }

        self.Items.setStyleSheet("""width: 255px;
                                    background-image: url(heroes/Techies/Items.png);
                                    height: 140px;
                                    border-radius: 15px;""")

        self.label_9.setStyleSheet("""width: 255px;
                                        background-image: url(heroes/Techies/SkillBuild.png);
                                        height: 140px;
                                        border-radius: 15px;
                                        """)

        self.Lore.setText("""  За всю историю Устричной бухты никого не ненавидели так, как подрывников Techies.
  Но - вот незадача - Устричной бухты больше нет. Как и города Тотерина. И даже Охотограда. Вообще,  если бы
  кто-нибудь следил за похождениями подрывников, он бы заметил, что там, где появляются Тесhіеѕ, 
  исчезают города. Им было интересно только одно: а как можно сделать взрыв ещё сильнее?""")

        self.Lore.setStyleSheet("""color: White;
                                    width: 255px;
                                    background-color: rgb(50, 50, 50);
                                    height: 140px;
                                    border-radius: 15px;""")

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()
