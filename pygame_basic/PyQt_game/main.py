from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from game import *
import sys
 
# 4k monitor
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
 
class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Avoid Game (Ocean Coding School)')
        self.game = Game(self)
 
    def redraw(self, rect):
        # 영역 확대 (잔상 방지)
        gap = rect.width()*0.2
        rect.adjust(-gap, -gap, gap, gap)
        self.update(rect.toAlignedRect())
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.game.draw(qp)
        qp.end()
 
    def keyPressEvent(self, e):
        if self.game.isStart() == False:
            self.game.startGame()
            self.update()
        else:
            self.game.keyPressed(e.key())  
 
    def keyReleaseEvent(self, e):
        if self.game.isStart():
            self.game.keyReleased(e.key())
 
    def closeEvent(self, e):
        self.game.endGame()
 
    def gameOver(self):
        result = QMessageBox.information(self, 'Game Over', 'Retry(Yes) or Exit(No)', QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            del(self.game)
            self.game = Game(self)
        else:
            self.close()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())