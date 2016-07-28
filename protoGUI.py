__author__ = 'tomcat'
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QAction, QMenuBar, QMessageBox, QPushButton, QStatusBar, QFileDialog, QCheckBox, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtGui import QIcon

class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
       self.statusBar = QStatusBar()

       self.OpenButton = QPushButton('Open Folder')
       self.OpenButton.clicked.connect(self.OpenFolder)

       self.ConvertButton = QPushButton('Convert')
       self.ConvertButton.clicked.connect(self.Convert)

       self.CheckBoxInst = QCheckBox('Instagram', self)
       self.CheckBoxVK = QCheckBox('VK.com', self)

       HBox = QHBoxLayout()
       HBox.addStretch(0)
       HBox.addWidget(self.OpenButton)
       HBox.addWidget(self.CheckBoxInst)
       HBox.addWidget(self.CheckBoxVK)

       VBox = QVBoxLayout()
       VBox.addStretch(0)
       VBox.addLayout(HBox)
       VBox.addWidget(self.ConvertButton)

       self.setLayout(VBox)

       self.setGeometry(500, 500, 500, 500)
       self.setWindowTitle('protoGUI')
       self.show()
    def OpenFolder(self):
       fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

    def Convert(self):
        f=1

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())