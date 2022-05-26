import sys
from PySide2.QtWidgets import QMainWindow, QApplication

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
