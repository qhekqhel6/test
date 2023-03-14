from PySide2.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, 
                               QMenu, QMenuBar, QDialog, QLabel, QLineEdit, 
                               QGroupBox,QCheckBox, QPushButton,QGridLayout,
                               QHBoxLayout,QVBoxLayout)
from PySide2.QtGui import QIcon,QDoubleValidator
#import GridDialog_rc

import sys

class GridDialog(QDialog):
    def __init__(self,x,y,useGrid,useSnap,parent):
        QDialog.__init__(self,parent)
        xLabel = QLabel("&X:")
        yLabel = QLabel("&Y:")
        self.xLineEdit = QLineEdit(str(x))
        self.yLineEdit = QLineEdit(str(y))
        xLabel.setBuddy(self.xLineEdit)
        yLabel.setBuddy(self.yLineEdit)

        validator = QDoubleValidator(self)
        validator.setBottom(0.)
        self.xLineEdit.setValidator(validator)
        self.yLineEdit.setValidator(validator)

        self.useGridGroupBox = QGroupBox("Use &Grid")
        self.useGridGroupBox.setCheckable(True)
        self.useGridGroupBox.setChecked(useGrid)

        self.useSnapCheckBox = QCheckBox("Use &Snap")
        self.useSnapCheckBox.setChecked(useSnap)
        self.useSnapCheckBox.setEnabled(useGrid)

        okButton = QPushButton("&Ok")
        okButton.setIcon(QIcon(":/ok.png"))
        okButton.setDefault(True)

        cancelButton = QPushButton("&Cancel")
        cancelButton.setIcon(QIcon(":/cancel.png"))

        gridLayout = QGridLayout()
        gridLayout.addWidget(xLabel,0,0)
        gridLayout.addWidget(self.xLineEdit,0,1)
        gridLayout.addWidget(yLabel,1,0)
        gridLayout.addWidget(self.yLineEdit,1,1)
        self.useGridGroupBox.setLayout(gridLayout)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.useGridGroupBox)
        mainLayout.addWidget(self.useSnapCheckBox)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle('Set Grid')

        # toggled(bool) - setEnabled(bool)
        self.useGridGroupBox.toggled.connect(self.useSnapCheckBox.setEnabled)
        okButton.clicked.connect(self.accept)     # clicked() - accept()
        cancelButton.clicked.connect(self.reject)  # clicked() - reject()


    def gridInfo(self):
        x = float(self.xLineEdit.text())
        y = float(self.yLineEdit.text())
        useGrid = self.useGridGroupBox.isChecked()
        useSnap = self.useSnapCheckBox.isChecked()

        return (x,y,useGrid,useSnap)

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        action = QAction('set grid',self)
        action.triggered.connect(self.setGrid)

        myMenu = self.menuBar().addMenu("&action")
        myMenu.addAction(action)

        self.x = 10
        self.y = 10
        self.useGrid = True
        self.useSnap = False

    def setGrid(self):
        gridDialog = GridDialog(self.x,self.y,self.useGrid,self.useSnap,self)
        if gridDialog.exec():
            self.x, self.y, self.useGrid, self.useSnap = gridDialog.gridInfo()

            log = "Ok : useGrid ="+str(self.useGrid) + \
                  ", useSnap = " + str(self.useSnap) + \
                  ", x= " + str(self.x) + ", y = " + str(self.y)
            self.textEdit.append(log)      
        else:
            self.textEdit.append("Cancel")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.resize(400,300)
    mainWindow.show()

    mainWindow.setWindowTitle("Test GridDialog")

    mainWindow.show()
    app.exec_()
