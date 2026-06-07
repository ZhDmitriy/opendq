import sys 

from PyQt6.QtCore import * 
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import * 

from PyQt6.QtCore import QDate, QTime, QDateTime, Qt


print(QDate.currentDate())
print(QDateTime.currentDateTime())

# Код приложения

def selectedOrNot(button):
    if button.text() == "First":
        if button.isChecked() == True: 
            print("First is selected")
        else: 
            print("First is deselected")
    else: 
        if button.isChecked() == True: 
            print("Second is selected")
        else: 
            print("Second is deselected")

# Инициализация приложения
app = QApplication(sys.argv)
w = QWidget()

# Создания лояута
box = QHBoxLayout()
button1 = QCheckBox("First")
button2 = QCheckBox("Second")

# Добавляем сигнал 
button1.stateChanged.connect(lambda: selectedOrNot(button1))
button2.toggled.connect(lambda: selectedOrNot(button2))

# Добавляем кнопки на лояут 
box.addWidget(button1)
box.addWidget(button2)

# Добавляем в приложение 
w.setLayout(box)

w.show()
sys.exit(app.exec())