from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel


class Slardar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('heroes/Slardar/ui/Slardar.ui', self)
        self.setFixedSize(1000, 700)
        self.setStyleSheet("""background-image: url(data/background/backgroundHero.png);
                              background-repeat: no-repeat;""")

        self.label = QLabel(self)
        self.label.resize(255, 140)
        self.label.move(20, 20)

        self.label.setStyleSheet("""width: 255px;
                                    background-image: url(heroes/Slardar/Slardar.png);
                                    height: 140px;
                                    border-radius: 15px  """)

        self.label_7.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/Oracle.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.label_6.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/Phoenix.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.label_5.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/reMars.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.label_4.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/Meepo.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.label_3.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/PhantomLancer.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.Talant.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/Tree.png);
                                     height: 140px;
                                     border-radius: 35px;
                                     border: 1px solid rgba(255, 255, 255, 100);    
                                     color: rgba(0, 0, 0, 0);""")

        self.Skill1.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/GuardianSprint.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     border: 1px solid rgba(255, 255, 255, 100);    
                                     color: rgba(0, 0, 0, 0);""")

        self.Skill2.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/SlithereenCrush.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     border: 1px solid rgba(255, 255, 255, 100);    
                                     color: rgba(0, 0, 0, 0);""")

        self.Skill3.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/BashOfTheDeep.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     border: 1px solid rgba(255, 255, 255, 100);    
                                     color: rgba(0, 0, 0, 0);""")

        self.Skill4.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/CorrosiveHaze.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     border: 1px solid rgba(255, 255, 255, 100);    
                                     color: rgba(0, 0, 0, 0);""")

        self.label_10.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/BuildSlardar.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.label_9.setStyleSheet("""width: 255px;
                                     background-image: url(heroes/Slardar/SkiilsInfoSlardar.png);
                                     height: 140px;
                                     border-radius: 15px;
                                     color: white;""")

        self.label_11.setStyleSheet("""width: 255px;
                                       background-color: rgb(50, 50, 50);
                                       height: 140px;
                                       border-radius: 15px;
                                       color: white; """)

        self.label_11.setText("""  Слардар из рода змееногих, один изобитателей глубин, охраняет обширную сеть затонувших 
  городов и скрытых ими древних ценностей. Он стоит на страже потайных сокровищниц, скрытых в  
  бессветной пучине, и неусыпно охраняет их от подводных воров, посланных на морское дно алчными 
  магами с поверхности. Страж верен своей службе как никто, а за его молчаливостью скрыто знание
  всех тайных морских проходов. Несмотря на жгучий свет, он поднимается на мелководье,
  чтобы разведать, не сговаривается ли кто против моря, — а иногда и чтобы расправиться с 
  теми немногими, кто всё же обворовал затонувшую сокровищницу. Проведённое под огромным 
  давлением морской толщи время сделало из змееногого стража существо невероятной мощи.""")

        self.Skill1Info.hide()
        self.Skill1Info.setStyleSheet("""background-image: url(heroes/Slardar/Skill1Info.png);
                                         border-radius: 15px;
                                         border: 2px solid black""")

        self.Skill2Info.hide()
        self.Skill2Info.setStyleSheet("""background-image: url(heroes/Slardar/Skill2Info.png);
                                         border-radius: 15px;
                                         border: 2px solid black""")

        self.Skill3Info.hide()
        self.Skill3Info.setStyleSheet("""background-image: url(heroes/Slardar/Skill3Info.png);
                                         border-radius: 15px;
                                         border: 2px solid black""")

        self.Skill4Info.hide()
        self.Skill4Info.setStyleSheet("""background-image: url(heroes/Slardar/Skill4Info.png);
                                         border-radius: 15px;
                                         background-repeat: no-repeat;
                                         border: 2px solid black""")

        self.TalentsInfo.hide()
        self.TalentsInfo.setStyleSheet("""background-image: url(heroes/Slardar/Talants.png);
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

    def run(self, arg):
        skill2 = "self." + arg.text() + "Info"
        if eval(f"{skill2}.isHidden()"):
            for skill, label in self.LabelHero.items():
                label.hide()
            eval(f"{skill2}.show()")
        else:
            for skill, label in self.LabelHero.items():
                label.hide()
