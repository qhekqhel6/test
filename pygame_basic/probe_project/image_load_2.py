from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget

if __name__ == '__main__':
    app = QApplication()
    
    # 이미지 로드
    pixmap = QPixmap('pygame_basic/probe_project/center.png')
    pixmap1 = QPixmap('pygame_basic/probe_project/probe_1.png')
    pixmap2 = QPixmap('pygame_basic/probe_project/probe_2.png')
    pixmap3 = QPixmap('pygame_basic/probe_project/probe_3.png')
    pixmap4 = QPixmap('pygame_basic/probe_project/probe_4.png')  

    # 이미지를 아이콘으로 변환
    icon = QIcon(pixmap)
    icon1 = QIcon(pixmap1)
    icon2 = QIcon(pixmap2)
    icon3 = QIcon(pixmap3)
    icon4 = QIcon(pixmap4)

    # 버튼 생성 및 아이콘 설정
    
    btn = QPushButton()
    btn.setIcon(icon1)
    btn1 = QPushButton()
    btn1.setIcon(icon1)
    btn2 = QPushButton()
    btn2.setIcon(icon2)
    btn3 = QPushButton()
    btn3.setIcon(icon3)
    btn4 = QPushButton()
    btn4.setIcon(icon4)

    # 버튼 보여주기
    #btn1.show()
    #btn2.show()

    # 이미지 위젯 생성
    label = QLabel()
    label.setPixmap(pixmap)
    label.setFixedSize(pixmap.size())

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


    # 그리드 레이아웃 생성
    layout1 = QGridLayout()
    layout1.addWidget(label, 1, 1)
    layout1.addWidget(label1, 0, 0)
    layout1.addWidget(label2, 0, 2)
    layout1.addWidget(label3, 2, 0)
    layout1.addWidget(label4, 2, 2)

    # 위젯 생성 및 레이아웃 설정
    widget = QWidget()
    widget.setLayout(layout1)

    # 윈도우에 위젯 추가
    widget.show()

    app.exec_()