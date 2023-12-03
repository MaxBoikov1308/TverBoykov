import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from towers import Towers


class Title(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUi()
        self.n = 6

    def InitUi(self):
        self.setWindowTitle("Main menu")
        self.setGeometry(300, 300, 800, 600)

        # creating of button to set Towers.n
        self.btn_number = QPushButton("Your blocks: 6", self)
        self.btn_number.resize(200, 50)
        self.btn_number.move(240, 120)
        self.btn_number.clicked.connect(self.choose_number)

        # creating of button to start the game
        self.btn_start = QPushButton("Start", self)
        self.btn_start.resize(50, 50)
        self.btn_start.move(450, 120)
        self.btn_start.clicked.connect(self.action)

    def choose_number(self):
        self.n, ok_pressed = QInputDialog.getInt(self, "Choose number of blocks", "3-15", 6, 3, 15, 1)
        if ok_pressed:
            self.btn_number.setText("Your blocks: " + str(self.n))
    
    def action(self):
        self.towers = Towers(self.n, [], [], [])
        self.towers.show()


# start the app
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Title()
	window.show()
	sys.exit(app.exec())
     