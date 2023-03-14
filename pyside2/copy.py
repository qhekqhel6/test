from PySide2.QtCore import Qt, QRectF, QPointF
from PySide2.QtGui import QBrush, QKeyEvent, QPixmap, QPainter
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QApplication

class Player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__(QPixmap('probe_project/probe_1-removebg.png'))
        self.setPos(0, 0)
        self.width = self.boundingRect().width()
        self.height = self.boundingRect().height()
        
    def mouseDoubleClickEvent(self, event):
        self.setPos(event.scenePos() - QPointF(self.width/2, self.height/2))

    def mouseMoveEvent(self, event):
        new_pos = event.scenePos() - QPointF(self.width/2, self.height/2)
        if new_pos.x() < 0:
            new_pos.setX(0)
        elif new_pos.x() + self.width > 1280:
            new_pos.setX(1280 - self.width)
        if new_pos.y() < 0:
            new_pos.setY(0)
        elif new_pos.y() + self.height > 720:
            new_pos.setY(720 - self.height)
        self.setPos(new_pos)

class GameScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        bg = QPixmap('probe_project/background.PNG')
        bg = bg.scaled(1280, 720)
        self.setBackgroundBrush(QBrush(bg))
        self.setSceneRect(0, 0, 1280, 720)
        self.player = Player()
        self.addItem(self.player)
        
class GameView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(GameScene(self))
        self.setFixedSize(1280, 720)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

if __name__ == '__main__':
    app = QApplication([])
    view = GameView()
    view.show()
    app.exec_()
