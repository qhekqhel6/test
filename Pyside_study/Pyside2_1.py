from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(200,300)
    window.setWindowTitle("FIrst Qt Program")

    label = QLabel('Hello Qt',window)
    label.move(80,100)

    label = QLabel('Bye Qt',window)
    label.move(80,200)
    window.show()
    app.exec_()
