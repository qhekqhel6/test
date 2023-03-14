from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QLabel

class DraggableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._mousePressPos = None
        self._mouseMovePos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mousePressPos = event.globalPos()
            self._mouseMovePos = self._mousePressPos - self.pos()

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            globalPos = event.globalPos()
            self.move(globalPos - self._mouseMovePos)

        super().mouseMoveEvent(event)

if __name__ == '__main__':
    app = QApplication()

    # 이미지 파일 로드
    pixmap = QPixmap('image.png')

    # 이미지 위젯 생성
    label = DraggableLabel()
    label.setPixmap(pixmap)
    label.setFixedSize(pixmap.size())

    # 윈도우에 이미지 위젯 추가
    label.show()

    app.exec_()
