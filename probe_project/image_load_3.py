from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QLabel, QGridLayout, QWidget

if __name__ == '__main__':
    app = QApplication()

    # 이미지 파일 로드
    pixmap1 = QPixmap('probe_project/image1.png')
    pixmap2 = QPixmap('probe_project/image2.png')
    #pixmap3 = QPixmap('image3.png')
    #pixmap4 = QPixmap('image4.png')
    #pixmap5 = QPixmap('image5.png')
    #pixmap6 = QPixmap('image6.png')
    #pixmap7 = QPixmap('image7.png')
    #pixmap8 = QPixmap('image8.png')
    #pixmap9 = QPixmap('image9.png')

    # 이미지 위젯 생성
    label1 = QLabel()
    label1.setPixmap(pixmap1)
    label2 = QLabel()
    label2.setPixmap(pixmap2)
    #label3 = QLabel()
    #label3.setPixmap(pixmap3)
    #label4 = QLabel()
    #label4.setPixmap(pixmap4)
    #label5 = QLabel()
    #label5.setPixmap(pixmap5)
    #label6 = QLabel()
    #label6.setPixmap(pixmap6)
    #label7 = QLabel()
    #label7.setPixmap(pixmap7)
    #label8 = QLabel()
    #label8.setPixmap(pixmap8)
    #label9 = QLabel()
    #label9.setPixmap(pixmap9)

    # 그리드 레이아웃 생성
    grid = QGridLayout()
    grid.addWidget(label1, 0, 0)
    grid.addWidget(label2, 0, 1)
    #grid.addWidget(label3, 0, 2)
    #grid.addWidget(label4, 1, 0)
    #grid.addWidget(label5, 1, 1)
    #grid.addWidget(label6, 1, 2)
    #grid.addWidget(label7, 2, 0)
    #grid.addWidget(label8, 2, 1)
    #grid.addWidget(label9, 2, 2)

    # 위젯 생성 및 레이아웃 설정
    widget = QWidget()
    widget.setLayout(grid)

    # 윈도우에 위젯 추가
    widget.show()

    app.exec_()
