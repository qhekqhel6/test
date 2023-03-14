import sys
from random import randint
from PySide2.QtCore import Qt, QTimer, QPoint, QRectF
from PySide2.QtGui import QPainter, QBrush, QColor
from PySide2.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem


class Player(QGraphicsRectItem):
    def __init__(self):
        super().__init__(-25, -25, 50, 50)
        self.setBrush(QBrush(QColor("green")))
        self.setFlag(QGraphicsRectItem.ItemIsFocusable)
        self.setFlag(QGraphicsRectItem.ItemIsMovable)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left or event.key() == Qt.Key_A:
            self.moveBy(-10, 0)
        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
            self.moveBy(10, 0)
        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
            self.moveBy(0, -10)
        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            self.moveBy(0, 10)
    
    def mousePressEvent(self, event):
        self.last_pos = event.pos()

    
#class Enemy(QGraphicsRectItem):
#    def __init__(self):
#        super().__init__(-25, -25, 50, 50)
#        self.setBrush(QBrush(QColor("red")))
#        self.setPos(randint(0, 600), randint(0, 400))

    def update(self):
        player = self.scene().player
        if self.collidesWithItem(player):
            self.scene().game_over()
        else:
            dx = player.x() - self.x()
            dy = player.y() - self.y()
            if dx > 0:
                self.moveBy(min(dx, 5), 0)
            else:
                self.moveBy(max(dx, -5), 0)
            if dy > 0:
                self.moveBy(0, min(dy, 5))
            else:
                self.moveBy(0, max(dy, -5))

class GameScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.addItem(self.player)
        #for _ in range(10):
            #self.addItem(Enemy())

class GameView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(GameScene())
        self.setRenderHint(QPainter.Antialiasing)
        #self.setFixedSize(640, 480)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QBrush(QColor("lightgray")))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GameView()
    view.show()

    timer = QTimer()
    timer.setInterval(16)
    timer.timeout.connect(view.scene().advance)
    timer.start()

    sys.exit(app.exec_())
