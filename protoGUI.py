__author__ = 'tomcat'
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QAction, QMenuBar, QMessageBox, qApp, QPushButton, QStatusBar, QGridLayout, QApplication)
from PyQt5.QtGui import QIcon

class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
       self.statusBar = QStatusBar()

       self.OpenButton = QPushButton('Open Folder')

       grid = QGridLayout()
       grid.setSpacing(10)

       grid.addWidget(self.OpenButton, 1, 0)
#       grid.addWidget(titleEdit, 1, 1)

 #      grid.addWidget(author, 2, 0)
  #     grid.addWidget(authorEdit, 2, 1)

   #    grid.addWidget(review, 3, 0)
    #   grid.addWidget(reviewEdit, 3, 1, 5, 1)

       self.setLayout(grid)

       self.setGeometry(500, 500, 500, 500)
       self.setWindowTitle('protoGUI')
       self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())