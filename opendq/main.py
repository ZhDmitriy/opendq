import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self): 
        """ Инициализация GUI интерфейса """
        self.setGeometry(350,  100, 1200, 900)
        self.setWindowTitle("opendq")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """ Настрока GUI интерфейса """
        self.counter = 0 
        label = QLabel("Счетчик: ", self)
        label.move(100, 100)
        self.label_counter = QLabel(str(self.counter), self)
        self.label_counter.move(180, 100)
        self.label_counter.setFixedWidth(30)
        button = QPushButton("Увеличить", self)
        button.move(100, 140)
        button.clicked.connect(self.incCounter)

        self.counter_input = QLineEdit(self)
        self.counter_input.move(100, 180)
        save_button = QPushButton("Сохранить", self)
        save_button.move(100, 220)
        save_button.clicked.connect(self.saveCounter)

    def saveCounter(self): 
        new_value = self.counter_input.text()
        self.label_counter.setText(new_value)
        self.counter = int(new_value)

    def incCounter(self):
        self.counter += 1
        self.label_counter.setText(str(self.counter))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())