from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor
 
class Unit:
    def __init__(self, r=QRectF(), c=QColor()):
        self.rect = r
        self.color = c
 
class Enemy(Unit):
    def __init__(self, dir=0, type=0, r=QRectF(), c=QColor()):
        super().__init__(r, c)
        # 적 방향 0:Left, 1:Up, 2:Right, 3:Down
        self.dir = dir
        # 적 종류 0:적, 1:모든적 삭제, 2:필요시 구현
        self.type = type
        self.isDead = False
 
    def moveUpdate(self, spd=2.0):
        if self.dir == 0:
            self.rect.adjust(spd, 0, spd, 0)
        elif self.dir == 1:
            self.rect.adjust(0, spd, 0, spd)
        elif self.dir == 2:
            self.rect.adjust(-spd, 0, -spd, 0)
        else:
            self.rect.adjust(0, -spd, 0, -spd)
 
class My(Unit):
    def __init__(self, r=QRectF(), c=QColor()):
        super().__init__(r, c)
        # 주인공 방향 0:Left, 1:Up, 2:Right, 3:Down
        self.dir = [False for _ in range(4)]
        self.hp = 10
        #지뢰 쿨타임, 지뢰
        self.bMine = False
        self.mine_cool = 0
        self.mine = Unit()
 
    def keyUpdate(self, key, isPress=True):
        if key == Qt.Key_Left:
            self.dir[0] = isPress
        if key == Qt.Key_Up:
            self.dir[1] = isPress
        if key == Qt.Key_Right:
            self.dir[2] = isPress
        if key == Qt.Key_Down:
            self.dir[3] = isPress
 
        if key == Qt.Key_Space and self.bMine==False and self.mine_cool==0:
            self.bMine = not self.bMine
            self.mine_cool = 300 # 3초
            size = self.rect.width()*3
            cpt = self.rect.center()
            x = cpt.x()-size/2
            y = cpt.y()-size/2
            self.mine = Unit( QRectF(x, y, size, size), QColor(128,128,128,128) )
 
    def moveUpdate(self, spd = 2.0):
        if self.dir[0]: # left
            self.rect.adjust(-spd, 0, -spd, 0)
        if self.dir[1]: # up
            self.rect.adjust(0, -spd, 0, -spd)
        if self.dir[2]: # right
            self.rect.adjust(spd, 0, spd, 0)
        if self.dir[3]: # down
            self.rect.adjust(0, spd, 0, spd)