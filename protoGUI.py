__author__ = 'tomcat'
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QAction, QMenuBar, QMessageBox, QPushButton, QStatusBar, QFileDialog, QCheckBox, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from wand.image import Image
import glob

class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
       self.statusBar = QStatusBar()

       self.OpenButton = QPushButton('Open Folder')
       self.OpenButton.clicked.connect(self.OpenFolder)

       self.ConvertButton = QPushButton('Convert')
       self.ConvertButton.clicked.connect(self.PreConvert)

       self.CheckBoxInst = QCheckBox('Instagram', self)
       #self.CheckBoxInst.checkState.connect(self.InstagramWH)
       self.CheckBoxVK = QCheckBox('VK.com', self)
       #self.CheckBoxVK.stateChanged.connect(self.VKWH)

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
       self.fname = QFileDialog.getExistingDirectory(self, 'Select Folder', '/home/tomcat/PycharmProjects/photo-lazy')

    def PreConvert(self):
        if self.CheckBoxInst.isChecked():
            width = 612
            height = 612
            Prefix = 'Inst_'
            self.Convert(width, height, Prefix)
            return
        elif self.CheckBoxVK.isChecked():
            width = 800
            height = 500
            Prefix = 'VK_'
            self.Convert(width, height, Prefix)
        else:
           return

    def Convert(self, width, height, Prefix):
        for self.fname in glob.glob('*.jpg'):
            with Image(filename=self.fname) as original:
                original.transform(resize="%dx%d>" % (width, height))
                #            outerImg.format = original.format.lower()
                #            outerImg.composite(original, left=int((width - original.width)/2), top=int((height-original.height)/2))
                #            original.resize(height=612, width=612)
                original.save(filename=Prefix + self.fname)

#    def InstagramWH(self, state):
#        if state == Qt.Checked:
#            global width
#            width = 612
#            global height
#            height = 612
#            global Prefix
#            Prefix = 'Inst_'
#            self.ConvertButton.clicked.connect(self.Convert)
#            return
#        else:
#            return

 #   def VKWH(self, state):
 #       if state == Qt.Checked:
 #           global width
 #           width = 800
 #           global height
 #           height = 500
 #           global Prefix
 #           Prefix = 'VK_'
 #           self.ConvertButton.clicked.connect(self.Convert)
 #           return
 #       else:
 #           return

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())