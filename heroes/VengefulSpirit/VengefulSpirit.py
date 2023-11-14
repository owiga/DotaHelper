from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class VengefulSpirit(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/VengefulSpirit/ui/hero.ui', self)
        self.setStyleSheet("background-image: url(data/background/backgroundHero.png)")
        self.Picture.setStyleSheet("""background-image: url(heroes/VengefulSpirit/VengefulSpirit.png);
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
        self.Hero2.setStyleSheet("""background-image: url(heroes/EmberSpirit/reEmberSpirit.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero3.setStyleSheet("""background-image: url(heroes/BeastMaster/reBeastmaster.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero4.setStyleSheet("""background-image: url(heroes/Rubick/reRubick.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Hero5.setStyleSheet("""background-image: url(heroes/WinterWyvern/reWinterWyvern.png);
                                    border-radius: 15px;
                                    color: white ;
                                    border: 1px solid rgba(255, 255, 255,60);
                                    width: 255px;
                                    height: 140px;""")
        self.Skill1.setStyleSheet("""background-image: url(heroes/VengefulSpirit/MagicMissile.png);
                                  border-radius: 15px;
                                  border: 1px solid rgba(255, 255, 255, 100);    
                                  color: rgba(0, 0, 0, 0);""")
        self.Skill2.setStyleSheet("""background-image: url(heroes/VengefulSpirit/WaveOfTerror.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill3.setStyleSheet("""background-image: url(heroes/VengefulSpirit/VengeanceAura.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")
        self.Skill4.setStyleSheet("""background-image: url(heroes/VengefulSpirit/NetherSwap.png);
                                          border-radius: 15px;
                                          border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/VengefulSpirit/Skill1Info.png);
                                         border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/VengefulSpirit/Skill2Info.png);
                                                 border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/VengefulSpirit/Skill3Info.png);
                                                         border-radius: 15px;
                                                                border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/VengefulSpirit/Skill4Info.png);
                                                                 border-radius: 15px;
                                                                background-repeat: no-repeat;
                                                                border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/VengefulSpirit/Talants.png);
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
                                    background-image: url(heroes/VengefulSpirit/Items.png);
                                    height: 140px;
                                    border-radius: 15px;""")

        self.label_9.setStyleSheet("""width: 255px;
                                        background-image: url(heroes/VengefulSpirit/SkillBuild.png);
                                        height: 140px;
                                        border-radius: 15px;
                                        """)

        self.Lore.setText("""        Даже самые сдержанные cкайрасы — это раздражительные от природы создания, готовые отомстить
        за самое мелкое оскорбление. Но Шенделезара — это месть во плоти. Некогда гордая и свирепая скайраска, Шенделезара
        должна была унаследовать Жуткое гнездо, но предательство сестры лишило её законного права. Попавшись в 
        расставленные убийцей сети, Шенделезара смогла выбраться, лишь пожертвовав своими крыльями и испытав
        страшное унижение: ей пришлось ковылять пешком. Она знала, что без крыльев cкайрасы никогда не примут её правление
        и что на самом высоком насесте Жуткого гнезда, до которого можно лишь долететь, её сестра была в безопасности.
        Не желая жить бескрылой калекой и жаждя мести больше, чем власти, павшая принцесса заключила
        сделку с богиней Скриок: она пожертвовала своё истерзанное тело и обрела форму вечного духа, живущего местью и
        обладающего жуткой мощью в материальном мире. Она добьётся отмщения — даже если крыльев ей уже не вернуть.""")

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
