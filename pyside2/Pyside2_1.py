from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(640,400)
    window.setWindowTitle("FIrst Qt Program")

    label = QLabel('Hello Qt',window)
    label.move(110,80)

    window.show()
    app.exec_()
