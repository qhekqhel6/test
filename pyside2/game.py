import sys
from PySide2.QtWidgets import QApplication, QMainWindow

class main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('My PySide2 Game')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_Window()
    window.show()
    sys.exit(app.exec_())