from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton
#import RenderArea_rc

class Label(QLabel):
    def __init__(self, text, option=0):
        if option == 0:
            QLabel.__init__(self, "especially "+text)
        if option == 1:
            QLabel.__init__(self, "esly "+text)
        if option == 2:
            QLabel.__init__(self, "ey "+text)


app = QApplication([])
widget = QWidget()
btns = []
btns.append(QPushButton("Test 3"))
btns.append(QPushButton("Test 4"))
h_layout = QHBoxLayout(widget)
h_layout.addWidget(QLabel("Test 1"))
n_f = [2, 3, 4, 5]
n_o = [0, 1, 2, 0]
for f, o in zip(n_f, n_o):
    h_layout.addWidget(Label(f"Test {f}", o))
# h_layout.addWidget(Label("Test 3", 1))
# h_layout.addWidget(Label("Test 4", 2))
# h_layout.addWidget(Label("Test 5", 0))
h_layout.addWidget(btns[0])
h_layout.addWidget(btns[1])
widget.show()
app.exec_()
