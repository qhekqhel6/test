import sys
from PySide2.QtWidgets import (QApplication, QWidget, QSpinBox, QSlider, QProgressBar, QHBoxLayout)
from PySide2.QtCore import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = QWidget()

    spin = QSpinBox()
    spin.setRange(0,100)

    slider = QSlider(Qt.Horizontal)
    slider.setRange(0,100)

    progressBar = QProgressBar()
    progressBar.setAlignment(Qt.AlignCenter)
    progressBar.setRange(0,100)

    spin.valueChanged.connect(slider.setValue)    # valuChanged(int), setValue(int)
    slider.valueChanged.connect(spin.setValue)
    spin.valueChanged.connect(progressBar.setValue)

    layout = QHBoxLayout()
    layout.addWidget(spin)
    layout.addWidget(slider)
    layout.addWidget(progressBar)


    form.setLayout(layout)
    form.setWindowTitle('SpinSliderProgressDemo')

    form.show()
    app.exec_()