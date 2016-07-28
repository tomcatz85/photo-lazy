__author__ = 'tomcat'
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QAction, QMenuBar, QMessageBox, QPushButton, QStatusBar, QFileDialog, QCheckBox, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication)
from wand.image import Image
import os
import glob

class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
       self.OpenButton = QPushButton('Open Folder')
       self.OpenButton.clicked.connect(self.OpenFolder)

       self.ConvertButton = QPushButton('Convert')
       self.ConvertButton.clicked.connect(self.PreConvert)

       self.CheckBoxInst = QCheckBox('Instagram', self)
       self.CheckBoxVK = QCheckBox('VK.com', self)

       self.statusBar = QStatusBar(self)
       self.statusBar.showMessage('Ready')

       HBox = QHBoxLayout()
       HBox.addWidget(self.OpenButton)
       HBox.addWidget(self.CheckBoxInst)
       HBox.addWidget(self.CheckBoxVK)

       VBox = QVBoxLayout()
       VBox.addLayout(HBox)
       VBox.addWidget(self.ConvertButton)
#       VBox.addWidget(self.statusBar)

       self.setLayout(VBox)

       self.setGeometry(500, 500, 500, 500)
       self.setWindowTitle('protoGUI')
       self.show()

    def OpenFolder(self):
       self.fname = QFileDialog.getExistingDirectory(self, 'Select Folder', '/home/tomcat/PycharmProjects/photo-lazy')

    def PreConvert(self):
        if self.CheckBoxInst.isChecked():
            self.ConvertInst()
        if self.CheckBoxVK.isChecked():
            self.ConvertVK()
        if self.CheckBoxInst.isChecked()*self.CheckBoxVK.isChecked():
            self.ConvertInst()
            self.ConvertVK()

    def ConvertInst(self):
        width = 612
        height = 612
        Prefix = 'Inst_'
        if not os.path.exists(Prefix):
            os.mkdir(Prefix, mode=0o755)
        for self.fname in glob.glob('*.jpg'):
            with Image(filename=self.fname) as original:
                original.transform(resize="%dx%d>" % (width, height))
                os.chdir(Prefix)
                original.save(filename=self.fname)
                os.chdir('..')

    def ConvertVK(self):
        width = 800
        height = 500
        Prefix = 'VK_'
        if not os.path.exists(Prefix):
            os.mkdir(Prefix, mode=0o755)
        for self.fname in glob.glob('*.jpg'):
            with Image(filename=self.fname) as original:
                original.transform(resize="%dx%d>" % (width, height))
                os.chdir(Prefix)
                original.save(filename=self.fname)
                os.chdir('..')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())