import sys 

from PyQt6.QtCore import * 
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import * 

app = QApplication(sys.argv)
w = QWidget()

comboBox = QComboBox()

#comboBox.addItem("First")
comboBox.addItems(["Second", "Third", "Fourth"])


box = QHBoxLayout()
box.addWidget(comboBox)

w.setLayout(box)
w.show()
sys.exit(app.exec())
