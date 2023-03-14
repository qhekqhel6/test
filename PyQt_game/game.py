from PyQt5.QtCore import Qt, QSizeF, QObject, pyqtSignal, QRectF
from PyQt5.QtGui import QPainter, QFont, QFontMetrics, QBrush, QColor
from unit import Unit, Enemy, My
from threading import Thread
import time
import random
 
class Game(QObject):
 
    update_widget = pyqtSignal(QRectF)
    game_over = pyqtSignal()
 
    def __init__(self, w):        
        super().__init__()
        self.parent = w
        self.rect = QRectF(w.rect())
        self.bRun = False
 
        # 적군 저장 리스트
        self.e = []
        # 점수
        self.score = 0
        # FontMetrics
        self.font = QFont('arial', 15);        
 
        # 시그널 처리
        self.update_widget.connect(self.parent.redraw)
        self.game_over.connect(self.parent.gameOver)
 
    def startGame(self):
        cpt = self.rect.center()
        size = QSizeF(30,30)
        self.my = My(QRectF(cpt, size), QColor(0,255,0))
        self.bRun = True
        self.t = Thread(target=self.threadFunc)
        self.t.start()
 
    def endGame(self):
        self.bRun = False
 
    def isStart(self):
        return self.bRun    
 
    def keyPressed(self, key):        
        self.my.keyUpdate(key, True)        
 
    def keyReleased(self, key):
        self.my.keyUpdate(key, False)
 
    def draw(self, qp):
        self.rect = QRectF(self.parent.rect())
        # 게임 시작 전
        if self.bRun==False:
            font = QFont('arial', 20)
            qp.setFont(font)
            qp.drawText(self.rect, Qt.AlignCenter, 'Press any key to start!')
        else:
            # 주인공, 지뢰 그리기
            b = QBrush(self.my.color)
            qp.setBrush(b)            
            qp.setFont(self.font)
            qp.drawRect(self.my.rect)
            if self.my.bMine:
                b = QBrush(self.my.mine.color)
                qp.setBrush(b)
                qp.drawEllipse(self.my.mine.rect)            
 
            # 적군 그리기
            for e in self.e:
                b = QBrush(e.color)
                qp.setBrush(b)
                qp.drawRect(e.rect)
 
            # 쿨타임, 점수, 체력
            qp.drawText(self.rect, Qt.AlignTop|Qt.AlignRight, f'Cool:{self.my.mine_cool}')
            qp.drawText(self.rect, Qt.AlignTop|Qt.AlignLeft, f'Score:{self.score}')
            qp.drawText(self.my.rect, Qt.AlignCenter, str(self.my.hp))
 
 
    def createEnemy(self):
        r = random.randint(1, 100)
        if r>=1 and r<=10: # 10%확률로 생성
            dir = random.randint(0,3)
            size = 20
            if dir == 0: # from left
                x = self.rect.left()-size
                y = random.randint(self.rect.top(), self.rect.bottom()-size)
            elif dir == 1: # from top
                x = random.randint(self.rect.left(), self.rect.right()-size)
                y = self.rect.top()-size
            elif dir == 2: # from right
                x = self.rect.right()
                y = random.randint(self.rect.top(), self.rect.bottom()-size)
            else: # from bottom
                x = random.randint(self.rect.left(), self.rect.right()-size)
                y = self.rect.bottom()
 
            rect = QRectF(x, y, size, size)
 
            # 적 종류 0:적, 1:모든적 삭제, 2:필요시 구현
            r = random.randint(1,100)
            if(r==1): # 1%
                type = 1
                color = QColor(200, 127, 39)
            else:
                type = 0
                color = QColor(255, 0, 0)
             
            self.e.append( Enemy(dir, type, rect, color ) )
 
    def moveEnemy(self):
        for e in self.e:
            e.moveUpdate()
            # 적군이 화면 밖으로 나갔는지
            if self.rect.intersects(e.rect) == False:
                e.isDead = True
            # 적군이 나와 충돌했는지
            elif self.my.rect.intersects(e.rect):
                if e.type==0:
                    e.isDead = True
                    self.my.hp -= 1
                else:
                    self.e.clear()
                    self.update_widget.emit(self.rect)
                    break
            # 적군이 나의 지뢰와 충돌했는지
            elif self.my.bMine and self.my.mine.rect.intersects(e.rect):
                e.isDead = True
                self.my.bMine = False
                self.update_widget.emit(self.my.mine.rect)        
 
    def update(self):
        # 화면갱신 (아군)
        self.update_widget.emit(self.my.rect)
        # 화면갱신 (점수, 쿨타임)
        fm = QFontMetrics(self.font)
        rect = fm.boundingRect(self.rect.toAlignedRect(), Qt.AlignTop|Qt.AlignRight, f'Cool:{self.my.mine_cool}')
        self.update_widget.emit(QRectF(rect))
        rect = fm.boundingRect(self.rect.toAlignedRect(), Qt.AlignTop|Qt.AlignLeft, f'Score:{self.score}')
        self.update_widget.emit(QRectF(rect))
 
        # 화면 갱신 (지뢰)
        if self.my.bMine:
            self.update_widget.emit(self.my.mine.rect)                
        # 화면 갱신 (적군)
        for e in self.e:
            self.update_widget.emit(e.rect)
 
        # 적군 삭제 (충돌 or 화면밖)
        before = len(self.e)
        self.e = [e for e in self.e if not e.isDead]
        after = len(self.e)
        self.score += before-after
         
 
    def threadFunc(self):
        while self.bRun:
            # 주인공 이동
            self.my.moveUpdate()
 
            #  적군 생성, 추가
            self.createEnemy()
 
            # 적군 이동
            self.moveEnemy()
 
            # 화면 갱신 (주인공)
            self.update()
 
            # 지뢰 쿨타임
            if self.my.mine_cool>0:
                self.my.mine_cool-=1
 
            # 게임종료
            if self.my.hp<=0:                
                self.game_over.emit()
                break
 
            time.sleep(0.01)