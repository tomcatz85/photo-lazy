__author__ = 'tomcat'
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QAction, QMenuBar, QMessageBox, QPushButton, QStatusBar, QFileDialog, QCheckBox, QHBoxLayout, QVBoxLayout, QMainWindow, QProgressBar, QApplication)
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

       self.progressBar = QProgressBar(self)
       self.progressBar.setRange(0, 1)
       self.statusBar = QStatusBar(self)
       self.statusBar.addWidget(self.progressBar)
       #self.statusBar.showMessage('Ready')

       HBox = QHBoxLayout()
       HBox.addWidget(self.OpenButton)
       HBox.addWidget(self.CheckBoxInst)
       HBox.addWidget(self.CheckBoxVK)

       VBox = QVBoxLayout()
       VBox.addLayout(HBox)
       VBox.addWidget(self.ConvertButton)

       self.setLayout(VBox)

       self.setGeometry(500, 500, 500, 500)
       self.setWindowTitle('protoGUI')
       self.show()

    def OpenFolder(self):
       home = os.getenv('HOME')
       self.fname = QFileDialog.getExistingDirectory(self, 'Select Folder', home)

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
        prefix = 'Inst_'
        os.chdir(self.fname)
        if not os.path.exists(prefix):
            os.mkdir(prefix, mode=0o755)
        for image in glob.glob('*.jpg'):
            with Image(filename=image) as original:
                original.transform(resize="%dx%d>" % (width, height))
                os.chdir(prefix)
                original.save(filename=image)
                os.chdir('..')

    def ConvertVK(self):
        width = 800
        height = 500
        prefix = 'VK_'
        print(self.fname)
        os.chdir(self.fname)
        if not os.path.exists(prefix):
            os.mkdir(prefix, mode=0o755)
        for image in glob.glob('*.jpg'):
            with Image(filename=image) as original:
                original.transform(resize="%dx%d>" % (width, height))
                os.chdir(prefix)
                original.save(filename=image)
                os.chdir('..')

    def onStart(self):
        self.progressBar.setRange(0, 0)
        self.PreConvert.start()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())