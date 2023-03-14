from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QWidget, QLabel, QHBoxLayout, QPushButton, QMainWindow
from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt, QPointF
from PySide2.QtGui import QVector3D, QQuaternion, QPainter, QRegion, QPixmap
from PySide2.QtUiTools import QUiLoader
import sys

loader = QUiLoader()
app = QApplication(sys.argv)
window = loader.load("probe1.ui", None)
window.show()
#class MainWindow(QMainWindow):
#
#    def __init__(self):
#        super(MainWindow, self).__init__()
#        self.title = "Micro probe"
#        self.setWindowTitle(self.title)
#
#        label = QLabel(self)
#        pixmap = QtGui.QPixmap('Users/NEXTRON/Desktop/project/probe1.png')
#        label.setPixmap(pixmap)
#        self.setCentralWidget(label)
#        self.resize(pixmap.width(), pixmap.height())
#

#w = MainWindow()
#w.show()
sys.exit(app.exec_())

#app = QApplication(sys.argv)
#widget = QWidget()

#img = QtGui.QImage('Users/NEXTRON/Desktop/PROJECT/probe1.png')
#pixmap = QtGui.QPixmap(img)
#lab = QLabel(pixmap)
#QLabel.setPixmap(lab)

#widget.show()
#app.exec_()