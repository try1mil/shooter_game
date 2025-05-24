#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QRadioButton, QApplication, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
my_win = QWidget() 
my_win.setWindowTitle('Memory Card')
my_win.resize(200, 300)
question = QLabel('Which nationality does not exist?')
btn = QPushButton('Answer')

RadioGroupBox = QGroupBox('Answer options')
rbtn1 = QRadioButton('Enets')
rbtn2 = QRadioButton('Smurfs')
rbtn3 = QRadioButton('Chulyms')
rbtn4 = QRadioButton('Aleuts')

line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()


line1.addWidget(rbtn1, alignement = Qt.AlignVcenter)
line1.addWidget(rbtn3, alignement = Qt.AlignVcenter)
line2.addWidget(rbtn2, alignement = Qt.AlignVcenter)
line2.AddWidget(rbtn4, alignement = Qt.AlignVcenter)
line3.AddLayout(line1)
line3.AddLayout(line2)
RadioGroupBox.setLayout(line3)

main_lay = QVBoxLayout()
main_lay.addWidget(question)
main_lay.addWidget(RadioGroupBox)
main_lay.addWidget(btn)

mw.setLayout(main_lay)
mw.show()
app.exec_()