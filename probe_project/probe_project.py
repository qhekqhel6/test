from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PySide2.QtCore import Qt, QPointF
from PySide2.QtGui import QVector3D, QQuaternion

class Camera:
    def __init__(self, pos, up, lookat):
        self.position = QVector3D(pos)
        self.up_vector = QVector3D(up)
        self.lookat_position = QVector3D(lookat)
        self.forward_vector = (self.lookat_position - self.position).normalized()
        self.right_vector = QVector3D.crossProduct(self.forward_vector, self.up_vector).normalized()
        self.up_vector = QVector3D.crossProduct(self.right_vector, self.forward_vector).normalized()
        self.speed = 0.1  # 이동 속도
        
    def move_forward(self):
        self.position += self.forward_vector * self.speed
        
    def move_backward(self):
        self.position -= self.forward_vector * self.speed
        
    def move_right(self):
        self.position += self.right_vector * self.speed
        
    def move_left(self):
        self.position -= self.right_vector * self.speed
        
    def move_up(self):
        self.position += self.up_vector * self.speed
        
    def move_down(self):
        self.position -= self.up_vector * self.speed
        
    def rotate(self, angle, axis):
        rot = QQuaternion.fromAxisAndAngle(axis, angle)
        self.forward_vector = rot.rotatedVector(self.forward_vector)
        self.up_vector = rot.rotatedVector(self.up_vector)
        self.right_vector = rot.rotatedVector(self.right_vector)
        self.lookat_position = self.position + self.forward_vector


class MyView(QGraphicsView):
    def __init__(self):
        super().__init__()

        # 그래픽 씬 생성
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # 뷰 설정
        self.setRenderHint(QPainter.Antialiasing)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # 마우스 클릭 이벤트 설정
        self.mousePressEvent = self.on_mouse_press

    def on_mouse_press(self, event):
        # 마우스 클릭한 위치의 좌표 가져오기
        pos = self.mapToScene(event.pos())
        x, y, z  = pos.x(), pos.y(), pos.z()

        # 탐침자 이동
        self.move_probe(x, y, z)

        # 포인트 추가
        item = QGraphicsEllipseItem(x-2, y-2, z-2, 4, 4, 4)
        self.scene.addItem(item)

    def move_probe(self, x, y, z):
        # TODO: 탐침자 이동 구현
        pass

    def move_probe(self, x, y):
        dx = x - self.probe.x()
        dy = y - self.probe.y()
        dz = z - self.probe.z()

        # 탐침자 이동
        self.probe.setX(x)
        self.probe.setY(y)
        self.probe.setY(z)

        # TODO: 탐침자 이동에 따른 작업 수행
        print(f"Probe moved by ({dx}, {dy}, {dz})")

        # 이동 거리 계산
        dist = math.sqrt(dx**2 + dy**2 + dz**2)

        # 이동 거리에 따른 작업 수행
        if dist > 0:
            print(f"Probe moved to ({x}, {y}, {z}), distance: {dist}")