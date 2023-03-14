import sys
from PySide2.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem
from PySide2.QtGui import QBrush, QColor, QPen
from PySide2.QtCore import Qt

# 맵과 캐릭터의 크기 및 색상 설정
BLOCK_SIZE = 50
MAP_COLOR = QBrush(QColor(255, 255, 255))
CHARACTER_COLOR = QBrush(QColor(255, 0, 0))

class GameWindow(QGraphicsView):
    def __init__(self, map_data):
        super().__init__()

        # 맵 데이터 초기화
        self.map_data = map_data
        self.map_width = len(self.map_data[0])
        self.map_height = len(self.map_data)

        # 씬 초기화
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setSceneRect(0, 0, self.map_width * BLOCK_SIZE, self.map_height * BLOCK_SIZE)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 맵 생성
        for y in range(self.map_height):
            for x in range(self.map_width):
                if self.map_data[y][x] == 1:
                    rect_item = QGraphicsRectItem(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    rect_item.setBrush(MAP_COLOR)
                    rect_item.setPen(QPen(Qt.NoPen))
                    self.scene.addItem(rect_item)

        # 캐릭터 생성
        self.character = QGraphicsEllipseItem(0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self.character.setBrush(CHARACTER_COLOR)
        self.character.setPen(QPen(Qt.NoPen))
        self.character.setPos(BLOCK_SIZE, BLOCK_SIZE)
        self.scene.addItem(self.character)

 # 키보드 이벤트 핸들러 등록
        self.keyPressEvent = self.handleKeyPressEvent

    def handleKeyPressEvent(self, event):
        # 키보드 이벤트 처리
        dx, dy = 0, 0
        if event.key() == Qt.Key_Left:
            dx = -BLOCK_SIZE
        elif event.key() == Qt.Key_Right:
            dx = BLOCK_SIZE
        elif event.key() == Qt.Key_Up:
            dy = -BLOCK_SIZE
        elif event.key() == Qt.Key_Down:
            dy = BLOCK_SIZE

        new_pos = self.character.pos() + QPointF(dx, dy)
        new_rect = self.character.rect().translated(dx, dy)
        if not self.isCollidingWithMap(new_rect):
            self.character.setPos(new_pos)

    def isCollidingWithMap(self, rect):
        # 맵과 충돌하는지 검사
        for y in range(self.map_height):
            for x in range(self.map_width):
                if self.map_data[y][x] == 1:
                    map_rect = QGraphicsRectItem(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    if rect.intersects(map_rect.rect()):
                        return True
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    map_data = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    game_window = GameWindow(map_data)
    game_window.show()
    sys.exit(app.exec_())