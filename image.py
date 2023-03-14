import sys
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

window3 = loader.load("probe3.ui", None)

window3.show()

app.exec_()