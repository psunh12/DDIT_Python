import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize


form_class = uic.loadUiType("pyqt_omok10.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flag_bw = True
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                btn2 = QPushButton(self)
                btn2.setIcon(QtGui.QIcon('0.png'))
                btn2.setIconSize(QSize(40, 40))  
                btn2.setGeometry(40*i, 40*j, 40, 40) 
                btn2.clicked.connect(self.myclick)
        
        
        self.show()


        
    def myclick(self) :
        if self.flag_bw:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag_bw = not self.flag_bw


        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()