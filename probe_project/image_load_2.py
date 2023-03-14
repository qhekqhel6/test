from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget

if __name__ == '__main__':
    app = QApplication()
    
    
    # 이미지 로드
    pixmap = QPixmap('probe_project/background.PNG')
    pixmap1 = QPixmap('probe_project/center-removebg.png')
    pixmap2 = QPixmap('probe_project/probe_1-removebg.png')
    pixmap3 = QPixmap('probe_project/probe_2-removebg.png')
    pixmap4 = QPixmap('probe_project/probe_3-removebg.png')
    pixmap5 = QPixmap('probe_project/probe_4-removebg.png') 

    # 이미지를 아이콘으로 변환
    
    icon1 = QIcon(pixmap1)
    icon2 = QIcon(pixmap2)
    icon3 = QIcon(pixmap3)
    icon4 = QIcon(pixmap4)
    icon5 = QIcon(pixmap5)

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
    label1.setPixmap(pixmap1)
    label1.setFixedSize(pixmap1.size())

    label2 = QLabel()
    label2.setPixmap(pixmap2)
    label2.setFixedSize(pixmap2.size())

    label3 = QLabel()
    label3.setPixmap(pixmap3)
    label3.setFixedSize(pixmap3.size())
    
    label4 = QLabel()
    label4.setPixmap(pixmap4)
    label4.setFixedSize(pixmap4.size())

    label5 = QLabel()
    label5.setPixmap(pixmap5)
    label5.setFixedSize(pixmap5.size())

    # 그리드 레이아웃 생성
    grid = QGridLayout()
    # grid.addWidget(label, 1, 1)
    grid.addWidget(label2, 0, 0)
    grid.addWidget(label1, 1, 1)
    grid.addWidget(label3, 0, 2)
    grid.addWidget(label4, 2, 0)
    grid.addWidget(label5, 2, 2)
    
    # 위젯 생성 및 레이아웃 설정
    widget = QWidget()
    widget.setLayout(grid)
    
    # 윈도우에 위젯 추가
    widget.show()

    # 윈도우에 이미지 위젯 추가
    label1.show()
    label2.show()

    app.exec_()