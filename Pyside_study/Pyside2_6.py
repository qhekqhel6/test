#from PySide2.QtWidgets import QWidget
#from PySide2.QtGui import QPalette, QPainter, QPen, QBrush, QFont
#from PySide2.QtCore import Qt, QRect
#
##Signal = ('move')
#
#class MyWidget(QWidget):
#    mousePositionChanged = Signal(str)   # mousePositonChanged(str)
#    def __init__(self,parent=None):
#        QWidget.__init__(self,parent)
#        self.setMouseTracking(True)
#        ...
#    def mouseMoveEvent(self,event):    # QMouseEvent event
#        pos = "({},{})".format(event.x(),event.y())
#        self.mousePositionChanged.emit(pos)
#
#    app.exec_()