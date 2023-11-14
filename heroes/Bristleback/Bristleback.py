from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class Bristleback(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/Bristleback/ui/Bristleback.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet(""" background-image: url(data/background/backgroundHero.png);
                               background-repeat: no-repeat;""")

        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)

        self.label.setStyleSheet("""width: 255px;
                                    background-image: url(heroes/Bristleback/Bristleback.png);
                                    height: 140px;
                                    border-radius: 15px  """)

        self.label_7.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/Hoodwink.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.label_6.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/Grimstroke.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.label_5.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/Slardar.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.label_4.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/OutworldDestroyer.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.label_3.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/AntiMage.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.Talents.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/Tree.png);
                                      height: 140px;
                                      border-radius: 35px;
                                      border: 1px solid rgba(255, 255, 255, 100);    
                                          color: rgba(0, 0, 0, 0);""")

        self.Skill1.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/ViscousNasalGoo.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      border: 1px solid rgba(255, 255, 255, 100);    
                                      color: rgba(0, 0, 0, 0);""")

        self.Skill2.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/QuillSpray.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      border: 1px solid rgba(255, 255, 255, 100);    
                                      color: rgba(0, 0, 0, 0);""")

        self.Skill3.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/BristlebackAbility.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      border: 1px solid rgba(255, 255, 255, 100);    
                                      color: rgba(0, 0, 0, 0);""")

        self.Skill4.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/Warpath.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      border: 1px solid rgba(255, 255, 255, 100);    
                                      color: rgba(0, 0, 0, 0);""")

        self.Skill5.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/Hairball.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      border: 1px solid rgba(255, 255, 255, 100);    
                                      color: rgba(0, 0, 0, 0);""")

        self.label_10.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/BuildBristleback.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.label_9.setStyleSheet("""width: 255px;
                                      background-image: url(heroes/Bristleback/SkillsInfo.png);
                                      height: 140px;
                                      border-radius: 15px;
                                      color: white;""")

        self.label_11.setStyleSheet("""width: 255px;
                                       background-color: rgb(50, 50, 50);
                                       height: 140px;
                                       border-radius: 15px;
                                       color: white; """)

        self.label_11.setText("""Ригварл никогда не уходил от драк и не поворачивался спиной к противнику, даже если тот 
был крупнее и сильнее его. Окрещённый пьяными толпами как Bristleback, он стал постоянным участником
подпольных боев, что проводились в тавернах на тракте между Сломом и Эльзе. Однажды умелого 
бойца заприметил один трактирщик, искавший вышибалу в бар. За скромную выпивку он стал собирать 
с посетителей плату, следить за порядком и время от времени ломать конечности особо несговорчивым 
клиентам (а одному членистоногому бедняге однажды сломал целых пять). Но все же Ригварлу 
довелось встретить бойца, равного себе.""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/Bristleback/Skill1Info.png);
                                         border-radius: 15px;
                                         border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/Bristleback/Skill2Info.png);
                                         border-radius: 15px;
                                         border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/Bristleback/Skill3Info.png);
                                         border-radius: 15px;
                                         border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/Bristleback/Skill4Info.png);
                                         border-radius: 15px;
                                         background-repeat: no-repeat;
                                         border: 2px solid black""")

        self.Skill5Info.hide()
        self.Skill5Info.setStyleSheet("""background-image: url(heroes/Bristleback/Skill5Info.png);
                                         border-radius: 15px;
                                         background-repeat: no-repeat;
                                         border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/Bristleback/Talants.png);
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

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()
