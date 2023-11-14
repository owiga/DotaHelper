from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class AncientApparition(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/AncientApparition/ui/hero.ui', self)
        self.setStyleSheet("background-image: url(data/background/backgroundHero.png)")
        self.Picture.setStyleSheet("""background-image: url(heroes/AncientApparition/AncientApparition.png);
                                      background-repeat: no-repeat;
                                      width: 255px;
                                      height: 140px;
                                      border-radius: 15px;""")
        self.setFixedSize(1000, 700)
        self.Talant.setStyleSheet("""background-image: url(heroes/Talents.png);
                                    border-radius: 35px;
                                    color: rgba(0, 0, 0, 0);""")
        self.Hero1.setStyleSheet("""background-image: url(heroes/PhantomLancer/rePhantomLancer.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero2.setStyleSheet("""background-image: url(heroes/StormSpirit/reStormSpirit.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero3.setStyleSheet("""background-image: url(heroes/Brewmaster/reBrewmaster.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero4.setStyleSheet("""background-image: url(heroes/ShadowDemon/reShadowDemon.png);
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
        self.Skill1.setStyleSheet("""background-image: url(heroes/AncientApparition/ColdFeet.png);
                                  border-radius: 15px;
                                  border: 1px solid rgba(255, 255, 255, 100);    
                                  color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""background-image: url(heroes/AncientApparition/IceVortex.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""background-image: url(heroes/AncientApparition/ChillingTouch.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""background-image: url(heroes/AncientApparition/IceBlast.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/AncientApparition/Skill1Info.png);
                                         border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/AncientApparition/Skill2Info.png);
                                                 border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/AncientApparition/Skill3Info.png);
                                                         border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/AncientApparition/Skill4Info.png);
                                                                 border-radius: 15px;
                                                                background-repeat: no-repeat;
                                                                border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/AncientApparition/Talants.png);
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

        self.Items.setStyleSheet("""width: 255px;
                                    background-image: url(heroes/AncientApparition/Items.png);
                                    height: 140px;
                                    border-radius: 15px;""")

        self.label_9.setStyleSheet("""width: 255px;
                                        background-image: url(heroes/AncientApparition/SkillBuilds.png);
                                        height: 140px;
                                        border-radius: 15px;
                                        """)

        self.Lore.setText("""         Древний дух Калдр - образ, скрытый за пределами времени. Он возник из холодной, бесконечной
        пустоты, что предшествует вселенной и ждет её конца. Калдр был, Калдр есть, Калдр будет...
        И та его мощь, что мы видим в нашем мире, — лишь слабое увядшее эхо настоящего, вечного Калдра.
        Говорят, что чем древнее космос и чем ближе его конец, тем страшнее будет могущество Калдра,
        и иссякающая вечность принесёт духу молодость и силу. И тогда его ледяная хватка остановит всё
        сущее, и образ его начнёт источать ужасающее сияние; и он больше не будет всего лишь духом.""")
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
