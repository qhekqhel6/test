import sys
from PySide2.QtGui import QPainter, QColor, QPixmap, QIcon
from PySide2.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QMainWindow, QApplication, QGraphicsView, QGraphicsRectItem, QLabel, QPushButton, QGridLayout, QWidget
from PySide2.QtCore import Qt, QTimer, QPoint, QRectF
from PySide2.QtGui import QPainter, QBrush, QColor

class main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('My PySide2 Game')

class GameView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        pixmap = QPixmap('probe_project/probe_1-removebg.png')
        self.image_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.image_item)


if __name__ == '__main__':
    app = QApplication()
        
    # 이미지 로드
    background = QPixmap('probe_project/background.PNG')
    center = QPixmap('probe_project/center-removebg.png')
    probe = QPixmap('probe_project/probe_1-removebg.png')
    probe_2 = QPixmap('probe_project/probe_2-removebg.png')
    probe_3 = QPixmap('probe_project/probe_3-removebg.png')
    probe_4 = QPixmap('probe_project/probe_4-removebg.png') 

    
    # 이미지를 아이콘으로 변환
    
    icon1 = QIcon(center)
    icon2 = QIcon(probe)
    icon3 = QIcon(probe_2)
    icon4 = QIcon(probe_3)
    icon5 = QIcon(probe_4)

    # 버튼 생성 및 아이콘 설정
    
    btn1 = QPushButton()
    btn1.setIcon(icon1)
    btn2 = QPushButton()
    btn2.setIcon(icon2)
    btn3 = QPushButton()
    btn3.setIcon(icon3)
    btn4 = QPushButton()
    btn4.setIcon(icon4)
    btn5 = QPushButton()
    btn5.setIcon(icon5)

    # 버튼 보여주기
    #btn1.show()
    #btn2.show()

    # 이미지 위젯 생성

    label1 = QLabel()
    label1.setPixmap(center)
    label1.setFixedSize(center.size())

    label2 = QLabel()
    label2.setPixmap(probe)
    label2.setFixedSize(probe.size())

    label3 = QLabel()
    label3.setPixmap(probe_2)
    label3.setFixedSize(probe_2.size())
    
    label4 = QLabel()
    label4.setPixmap(probe_3)
    label4.setFixedSize(probe_3.size())

    label5 = QLabel()
    label5.setPixmap(probe_4)
    label5.setFixedSize(probe_4.size())

    # 그리드 레이아웃 생성
    grid = QGridLayout()
    #grid.addWidget(label, 1, 1)
    grid.addWidget(label2, 0, 0)
    grid.addWidget(label1, 1, 1)
    grid.addWidget(label3, 0, 2)
    grid.addWidget(label4, 2, 0)
    grid.addWidget(label5, 2, 2)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left or event.key() == Qt.Key_A:        # 왼쪽으로 이동하는 코드 작성
            self.moveBy(-10, 0)        
        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_D:     # 오른쪽으로 이동하는 코드 작성
            self.moveBy(10, 0)
        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_W:        # 위쪽으로 이동하는 코드 작성
            self.moveBy(0, -10)
        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_S:      # 아래쪽으로 이동하는 코드 작성
            self.moveBy(0, 10)
        
    def mousePressEvent(self, event):
        self.last_pos = event.pos()
    
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


    # 위젯 생성 및 레이아웃 설정
    widget = QWidget()
    widget.setLayout(grid)
    
    # 윈도우에 위젯 추가
    widget.show()

    # 윈도우에 이미지 위젯 추가
    label1.show()
    label2.show()

    app.exec_()

    #sys.exit(app.exec_())





