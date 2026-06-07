import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self): 
        """ Инициализация GUI интерфейса """
        self.setGeometry(350,  100, 600, 400)
        self.setWindowTitle("Опрос удовлетворенности")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """ Настрока GUI интерфейса """
        header = QLabel("Опрос удовлетворенности", self)
        header.setStyleSheet("font-size: 24px; font-family: Arial; border: 1px solid black")
        header.setAlignment(Qt.AlignmentFlag.AlignTop)
        sub_header = QLabel("Выберите вариант", self)
        sub_header.setStyleSheet("font-size: 20px; font-family: Arial; border: 1px solid greem")
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(header)
        main_v_box.addWidget(sub_header)

        radio_group = QButtonGroup(self)
        radio_values = ["Отлично", "Норм", "Плохо"]
        for value in radio_values: 
            radio_button = QRadioButton(value, self)
            radio_group.addButton(radio_button)
            main_v_box.addWidget(radio_button)
        radio_group.buttonClicked.connect(self.getValue)
        submit_button = QPushButton("Отправить", self)
        submit_button.setFixedWidth(130)
        main_v_box.addWidget(submit_button)
        self.setLayout(main_v_box)

    def getValue(self, button):
        print(button.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())