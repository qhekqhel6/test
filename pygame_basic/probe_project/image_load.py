from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QPushButton

app = QApplication()

# 이미지 파일 로드
pixmap = QPixmap('image.png')

# 이미지를 아이콘으로 변환
icon = QIcon(pixmap)

# 버튼 생성 및 아이콘 설정
button = QPushButton()
button.setIcon(icon)

# 버튼 보여주기
button.show()


app.exec_()